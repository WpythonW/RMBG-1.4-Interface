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
