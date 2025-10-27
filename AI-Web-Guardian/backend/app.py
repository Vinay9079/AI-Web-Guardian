from fastapi import FastAPI
from pydantic import BaseModel
from nsfw_detector import classify_content
import google.generativeai as genai
import os

app = FastAPI()

# 🔑 Set your Gemini API key (Google AI)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

class URLRequest(BaseModel):
    url: str

@app.post("/analyze")
async def analyze(req: URLRequest):
    url = req.url.lower()

    # Quick keyword filter
    if any(word in url for word in ["porn", "sex", "xxx", "escort"]):
        return {"safe": False, "message": "🚫 Unsafe or adult content blocked by AI Guardian."}

    # Gemini-based content analysis (for better accuracy)
    prompt = f"Analyze this URL: {url}. Does it contain adult, scam, or harmful content? Reply safe/unsafe."
    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(prompt)
    text = result.text.lower()

    if "unsafe" in text:
        return {"safe": False, "message": "⚠️ Potentially harmful or manipulative content detected!"}

    # Additional local check
    result2 = classify_content(url)
    if result2 == "unsafe":
        return {"safe": False, "message": "🚫 Blocked: Unsafe content detected by AI filter."}

    return {"safe": True, "message": "✅ Safe browsing!"}
