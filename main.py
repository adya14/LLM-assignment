# main.py

import spacy
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline  # The key library for the local LLM

# --- 1. INITIALIZE THE FASTAPI APP ---
app = FastAPI(
    title="LLM NER API",
    description="An API that uses spaCy for NER and a local transformer for LLM responses."
)

# --- 2. SET UP CORS ---
# This allows your frontend (running in the browser) to communicate with your backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],
)

# --- 3. LOAD THE AI MODELS ---
# This section will run when the server starts.
print("Loading models... Please wait.")

# Load spaCy NER Model
try:
    nlp = spacy.load("en_core_web_sm")
    print("✅ spaCy NER model loaded successfully.")
except OSError:
    print("❌ spaCy model not found. Please run: python -m spacy download en_core_web_sm")
    nlp = None

# Load Local LLM using Hugging Face Transformers
# The first time this runs, it will download the model automatically.
llm_summarizer = None
try:
    # "t5-small" is a lightweight model perfect for this task.
    # The "pipeline" function simplifies using models for specific tasks.
    llm_summarizer = pipeline("summarization", model="t5-small")
    print("✅ Hugging Face summarization model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading Hugging Face model: {e}")

print("--- All models loaded. API is ready! ---")


# --- 4. DEFINE THE DATA MODEL FOR THE REQUEST ---
class PromptRequest(BaseModel):
    prompt: str

# --- 5. CREATE THE API ENDPOINT ---
@app.post("/process-prompt/")
async def process_prompt(request: PromptRequest):
    """
    Receives text, detects named entities, generates a summary, and returns both.
    """
    user_prompt = request.prompt
    print(f"\nProcessing prompt: '{user_prompt}'")

    # --- Part A: Named Entity Recognition with spaCy ---
    entities = []
    if nlp:
        doc = nlp(user_prompt)
        # Extract text and label for each detected entity
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
        print(f"Detected entities: {entities}")
    else:
        print("NER model not available.")

    # --- Part B: LLM Response with Transformers ---
    llm_response = ""
    if llm_summarizer:
        try:
            # The summarizer expects a list of texts; we provide one.
            # We set length constraints for a concise summary.
            result = llm_summarizer(user_prompt, max_length=50, min_length=10, do_sample=False)
            llm_response = result[0]['summary_text']
            print(f"LLM Summary: {llm_response}")
        except Exception as e:
            print(f"Error during LLM inference: {e}")
            llm_response = "Sorry, I couldn't generate a response."
    else:
        llm_response = "LLM model not available."

    # --- Part C: Return the combined result ---
    return {
        "detected_entities": entities,
        "llm_response": llm_response
    }