import gradio as gr
import cv2
import torch
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile
import uvicorn
from briarmbg import BriaRMBG
from utilities import preprocess_image, postprocess_image
import socket
from io import BytesIO
from starlette.responses import StreamingResponse

app = FastAPI()

def load_model(model_weights_path):
    net = BriaRMBG()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    net.load_state_dict(torch.load(model_weights_path, map_location=device))
    net.to(device)
    net.eval()
    return net, device

def remove_background(image):

    orig_im = np.array(image.convert("RGB"))
    orig_im_size = orig_im.shape[0:2]
    model_input_size = [1024, 1024]
    image_tensor = preprocess_image(orig_im, model_input_size).to(device)

    with torch.no_grad():
        result = net(image_tensor)

    result_image = postprocess_image(result[0][0], orig_im_size)
    result_image = result_image.astype(np.uint8)

    # Создание изображения с альфа-каналом
    no_bg_image = np.zeros((result_image.shape[0], result_image.shape[1], 4), dtype=np.uint8)
    orig_image = cv2.cvtColor(orig_im, cv2.COLOR_RGB2RGBA)
    no_bg_image[:, :, :3] = orig_image[:, :, :3]
    no_bg_image[:, :, 3] = result_image

    result_image_pil = Image.fromarray(no_bg_image)
    
    # Сохраняем результат в байтовый буфер
    buffer = BytesIO()
    result_image_pil.save(buffer, format="PNG")
    buffer.seek(0)

    return result_image_pil

@app.post("/remove-background/")
async def api_remove_background(file: UploadFile = File(...)):
    image = Image.open(BytesIO(await file.read()))
    result_image = remove_background(image)
    
    buffer = BytesIO()
    result_image.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")

# Gradio интерфейс для удаления фона
def gradio_remove_background(image):
    return remove_background(image)


net, device = load_model("app/model.pth")

interface = gr.Interface(
    fn=gradio_remove_background,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil", format="png", label="Output Image"),
    title="Remove Background",
    description="Upload an image and remove the background using the BriaRMBG model.",
    allow_flagging="never"
)

if __name__ == "__main__":
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    # Запуск Gradio интерфейса в отдельном потоке
    import threading
    threading.Thread(target=lambda: interface.launch(server_name=local_ip, server_port=7860)).start()
    
    # Запуск FastAPI
    uvicorn.run(app, host=local_ip, port=7861)
