# RMBG-1.4 & Gradio interface & api
This project removes background from images using the BriaRMBG model.

## Setup

### Prerequisites

Make sure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/WpythonW/RMBG-1.4-Interface.git
   cd repo
   ```

2. Install dependencies:

   ```sh
   poetry install
   ```

3. Install PyTorch:

   - For Windows with GPU:
     ```sh
     poetry run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
     ```

   - For Windows without GPU:
     ```sh
     poetry run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
     ```

   - For macOS:
     ```sh
     poetry run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
     ```

   - For Linux:
     ```sh
     poetry run pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
     ```

### Usage

Run the FastAPI server and Gradio interface:

```sh
poetry run python app/GradioInterface.py
```
