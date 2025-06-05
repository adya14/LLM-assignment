Simple LLM & NER App
====================

This project is a self-contained web application that processes user text to perform two key AI tasks. It uses **spaCy** to identify and highlight named entities (like people, organizations, and locations) and then uses a locally-run **Hugging Face** language model to generate a concise summary. The entire system is powered by a **FastAPI** backend and presented through a simple web interface.

Application Screenshot
----------------------

This is what the final application looks like in action.

**Note:** To use your own screenshot, save an image file (e.g., demo.png) in a screenshots folder within your project and update the link above to ./screenshots/demo.png.

Tech Stack
----------

*   **Backend**: Python, FastAPI
    
*   **NLP**: spaCy, Hugging Face Transformers
    
*   **Frontend**: HTML, CSS, JavaScript
    
*   **Server**: Uvicorn
    

Quick Start Guide
-----------------

Follow these steps to get the project running on your computer.

### Step 1: Setup Environment

First, clone the repository and create a Python virtual environment to keep dependencies clean.

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone   cd   python3 -m venv venv  source venv/bin/activate  # On Windows use: .\venv\Scripts\activate   `

### Step 2: Install Dependencies

Next, install all the required Python libraries and the spaCy language model using these two commands.

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Install all libraries from the requirements file  pip install -r requirements.txt  # Download the small English model for NER  python -m spacy download en_core_web_sm   `

### Step 3: Start the API Server

This step runs the backend engine of your project.

1.  Bashuvicorn main:app --reload
    
2.  **❗️ Important:** Do not close this terminal. Your server must be running for the application to work.
    
    *   **First Time Only:** You will see a progress bar as the language model downloads. Please wait for it to finish.
        
    *   **Success Message:** Your server is ready when the terminal shows a line like Uvicorn running on http://127.0.0.1:8000.
        

### Step 4: Open and Use the Application

This is the final step to launch the user interface.

1.  **Action:** Go to your project folder where your files are saved (main.py, index.html, etc.).
    
2.  **Launch:** Find and **double-click** the index.html file.
    
3.  **Result to Expect:**
    
    *   The application will immediately open in your default web browser (like Chrome or Safari).
        
    *   You can now type in the input box and use the app.
        

**Project Note:** This application uses the Hugging Face transformers library to run the LLM locally. This approach was chosen to create a fully self-contained project that does not require installing external software like Ollama, making setup easier.