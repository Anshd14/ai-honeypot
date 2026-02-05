from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from honeypot.detector import ScamDetector
from honeypot.persona import DecoyPersona
from honeypot.logger import MetadataLogger
from honeypot.reporter import Reporter
from fastapi import FastAPI, Request, Header, HTTPException
from honeypot.auth import APIKeyAuth

app = FastAPI()
auth = APIKeyAuth()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Templates
templates = Jinja2Templates(directory="templates")
# Core components
detector = ScamDetector()
persona = DecoyPersona()
logger = MetadataLogger()
reporter = Reporter()
# --- API Endpoint ---
@app.post("/handoff")
async def handoff(request: Request,authorization: str=Header(None)):
    # Check API key
    if not authorization or not auth.is_valid(authorization.replace("Bearer ", "")):
        raise HTTPException(status_code=401, detail="Invalid or expired API key")

    data = await request.json()
    message = data.get("message", "")
    is_scam, scam_type = detector.analyze(message)

    if not is_scam:
        return {"status": "safe", "response": "No scam detected."}

    response = persona.respond(message)
    metadata = logger.collect(message, response, scam_type)
    reporter.send(metadata)
    return {"status": "scam_detected", "response": response, "metadata": metadata}


# --- Web Interface ---
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.post("/web-handoff", response_class=HTMLResponse)
async def web_handoff(request: Request, message: str = Form(...)):
    is_scam, scam_type = detector.analyze(message)
    if not is_scam:
        return templates.TemplateResponse("result.html", {
            "request": request,
            "status": "safe",
            "response": "No scam detected.",
            "metadata": {}
        })
    response = persona.respond(message)
    metadata = logger.collect(message, response, scam_type)
    reporter.send(metadata)
    return templates.TemplateResponse("result.html", {
        "request": request,
        "status": "scam_detected",
        "response": response,
        "metadata": metadata
    })
