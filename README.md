# Simple LLM & NER App

A simple web application that takes a user prompt, identifies named entities with **spaCy**, and generates a summary with a local **Hugging Face** LLM, all served via a **FastAPI** backend.

## Tech Stack
- **Backend**: Python, FastAPI
- **NLP**: spaCy, Hugging Face Transformers
- **Frontend**: HTML, CSS, JavaScript

## Demo
![Application Screenshot](https://i.imgur.com/8QexgS3.png)
*(Replace this with a link to your own screenshot, e.g., `./screenshots/demo.png`)*

---

## Quick Start Guide

Follow these steps to run the project locally.

### 1. Setup Environment
Clone the repository, create a virtual environment, and activate it.
```bash
git clone <your-repository-url>
cd <project-folder>
python3 -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
### 2. Install Dependencies

In your terminal, run the following commands to install the necessary Python libraries and the spaCy language model.

```bash
# Install all libraries from the requirements file
pip install -r requirements.txt

# Download the small English model for NER
python -m spacy download en_core_web_sm

### Step 3: Start the API Server

This step runs the backend engine of your project.

1.  **Action:** In your terminal, run the single command below:
    ```bash
    uvicorn main:app --reload
    ```

2.  **Result to Expect:**
    * **First Time Only:** You will see a progress bar as the language model downloads. Please wait for it to finish.
    * **Success Message:** Your server is ready when the terminal shows a line like `Uvicorn running on http://127.0.0.1:8000`.

    > **❗️ Important:** Do not close this terminal. Your server must be running for the application to work.

### Step 4: Open and Use the Application

This step launches the user interface in your web browser.

1.  **Action:** Go to your project folder where your files are saved (`main.py`, `index.html`, etc.).
2.  **Launch:** Find and **double-click** the `index.html` file.

3.  **Result to Expect:**
    * The application will immediately open in your default web browser (like Chrome or Safari).
    * You can now type in the input box and use the app.