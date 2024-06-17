# RMBG-1.4 & Gradio Interface & API

This project removes background from images using the BriaRMBG model.

## Setup

### Prerequisites

Make sure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

#### Installing Poetry

- **Windows**:
  1. Open PowerShell as an administrator.
  2. Run the following command:
     ```sh
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
     ```

- **Linux / macOS**:
  1. Open a terminal.
  2. Run the following command:
     ```sh
     curl -sSL https://install.python-poetry.org | python3 -
     ```

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/WpythonW/RMBG-1.4-Interface.git
   cd RMBG-1.4-Interface
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

Replace `GradioInterface.py` with the name of your main script file if it is different.
```

### Проверка файла `pyproject.toml`

Убедись, что твой файл `pyproject.toml` выглядит следующим образом:

```toml
[tool.poetry]
name = "rmbg-1-4"
version = "0.1.0"
description = "A project for removing background from images"
authors = ["Your Name <you@example.com>"]
packages = [{include = "app"}]

[tool.poetry.dependencies]
python = "^3.11"
gradio = "^2.3.7"
opencv-python-headless = "^4.5.1.48"
numpy = "1.21.0"
pillow = "^8.2.0"
fastapi = "^0.68.0"
uvicorn = "^0.15.0"
briarmbg = "^0.1.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### Шаги по настройке и установке

1. **Создание структуры проекта:**

   ```sh
   cd D:/RMBG-1.4-Interface
   mkdir app
   mkdir app/models
   move GradioInterface.py app/
   move briarmbg.py app/
   move model.pth app/models/
   echo > app/__init__.py
   ```

2. **Инициализация Poetry и добавление зависимостей:**

   ```sh
   poetry init
   poetry add gradio opencv-python-headless numpy==1.21.0 pillow fastapi uvicorn briarmbg
   ```

3. **Создание файла `poetry.lock`:**

   ```sh
   poetry lock
   ```

4. **Добавление файлов в Git и коммит:**

   ```sh
   git add app pyproject.toml poetry.lock
   git commit -m "Added app folder and pyproject.toml with dependencies"
   git push origin main --force
   ```

### Инструкции для `README.md`

Добавь следующие инструкции в файл `README.md`:

```markdown
# RMBG-1.4 & Gradio Interface & API

This project removes background from images using the BriaRMBG model.

## Setup

### Prerequisites

Make sure you have [Poetry](https://python-poetry.org/docs/#installation) installed.

#### Installing Poetry

- **Windows**:
  1. Открой PowerShell от имени администратора.
  2. Запусти команду:
     ```sh
     (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
     ```

- **Linux / macOS**:
  1. Открой терминал.
  2. Запусти команду:
     ```sh
     curl -sSL https://install.python-poetry.org | python3 -
     ```

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/WpythonW/RMBG-1.4-Interface.git
   cd RMBG-1.4-Interface
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

Replace `GradioInterface.py` with the name of your main script file if it is different.
```

Diese Schritte helfen dir, die Struktur deines Projekts zu ändern und den `pyproject.toml` korrekt zu erstellen und zu aktualisieren. (Эти шаги помогут тебе изменить структуру проекта и корректно создать и обновить `pyproject.toml`.)
