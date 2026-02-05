from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from honeypot.detector import ScamDetector
from honeypot.persona import DecoyPersona
from honeypot.intelligence import IntelligenceExtractor
from honeypot.logger import MetadataLogger
from honeypot.reporter import Reporter
from honeypot.auth import APIKeyAuth

app = FastAPI()
auth = APIKeyAuth()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

detector = ScamDetector()
persona = DecoyPersona()
extractor = IntelligenceExtractor()
logger = MetadataLogger()
reporter = Reporter()

@app.post("/honeypot")
async def honeypot(request: Request, x_api_key: str = Header(None)):
    if not x_api_key or not auth.is_valid(x_api_key):
        raise HTTPException(status_code=401, detail="Invalid or expired API key")

    data = await request.json()
    session_id = data.get("sessionId")
    message = data["message"]["text"]
    history = data.get("conversationHistory", [])

    is_scam, scam_type = detector.analyze(message)

    if not is_scam:
        return {"status": "safe", "reply": "No scam detected."}

    reply = persona.respond(message)
    intelligence = extractor.extract(message)
    metadata = logger.collect(session_id, message, reply, scam_type)

    response = {
        "status": "success",
        "reply": reply,
        "intelligence": intelligence,
        "metadata": metadata
    }

    # Final callback if conversation is complete
    if len(history) >= 5:  # Example threshold
        payload = {
            "sessionId": session_id,
            "scamDetected": True,
            "totalMessagesExchanged": len(history) + 1,
            "extractedIntelligence": intelligence,
            "agentNotes": "Scammer used urgency tactics and payment redirection"
        }
        reporter.send_final(payload)

    return response

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})