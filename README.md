
# Simple LLM & NER App

This project is a self-contained web application that processes user text to perform two key AI tasks. It uses **spaCy** to identify and highlight named entities (like people, organizations, and locations) and then uses a locally-run **Hugging Face** language model to generate a concise summary. The entire system is powered by a **FastAPI** backend and presented through a simple web interface.

## Application Screenshot
![Application Screenshot](./demo.png)

This is what the final application looks like in action.

## Tech Stack

* *   **Backend**: Python, FastAPI
* *   **NLP**: spaCy, Hugging Face Transformers
* *   **Frontend**: HTML, CSS, JavaScript
* *   **Server**: Uvicorn

## Quick Start Guide

Follow these steps to get the project running on your computer.

### Step 1: Setup Environment

First, clone the repository and create a Python virtual environment to keep dependencies clean.

Bash

```
git clone <your-repository-url>
cd <project-folder>
python3 -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

### Step 2: Install Dependencies

Next, install all the required Python libraries and the spaCy language model using these two commands.

```
# Install all libraries from the requirements file
pip install -r requirements.txt

# Download the small English model for NER
python -m spacy download en_core_web_sm
```

### Step 3: Start the API Server  
     uvicorn main:app --reload

* * *

**Project Note:** This application uses the Hugging Face `transformers` library to run the LLM locally. This approach was chosen to create a fully self-contained project that does not require installing external software like Ollama, making setup easier.
