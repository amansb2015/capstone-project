from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
client = OpenAI()

@app.get("/")
def root_controller():
    return {"status": "healthy"}

@app.get("/chat")
def chat_controller(prompt: str = "What is the capital of France?"):
    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"response": response.output_text}