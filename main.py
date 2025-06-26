from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ScamSniper backend is live!"}

class ScamCheckRequest(BaseModel):
    url: str

@app.post("/check")
def check_site(data: ScamCheckRequest):
    url = data.url.lower()

    scam_keywords = ["vip", "bonus", "crypto", "giveaway", "double your money", "airdrop", "investment", "guaranteed returns"]
    is_scam = any(keyword in url for keyword in scam_keywords)

    return {
        "url": data.url,
        "is_scam": is_scam,
        "confidence": "high" if is_scam else "low",
        "message": "⚠️ This site looks suspicious." if is_scam else "✅ No red flags detected."
    }
