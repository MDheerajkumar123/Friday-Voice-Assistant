from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.intent_handler import handle_command

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CommandInput(BaseModel):
    command: str
    nickname: str | None = None  # Nickname for the user
    email: str | None = None     # Optional during setup
    password: str | None = None  # Optional during setup
    recipient: str | None = None
    subject: str | None = None
    message: str | None = None


@app.post("/process")
async def process_command(data: CommandInput):
    try:
        payload = {
            "nickname": data.nickname,
            "email": data.email,
            "password": data.password,
            "recipient": data.recipient,
            "subject": data.subject,
            "message": data.message,
        }

        response = handle_command(data.command, payload)

        if isinstance(response, dict):
            reminder = response.get("reminder", {})
            return JSONResponse(content={
                "text": response.get("text", ""),
                "url": response.get("url", ""),
                "app": response.get("app", ""),  # ✅ Added this line
                "audio": response.get("audio", ""),
                "reminder": {
                    "task": reminder.get("task"),
                    "timestamp": reminder.get("timestamp")
                } if reminder else None
            })

        elif isinstance(response, list):
            full_text = " ".join([item.get("text", "") for item in response])
            combined_audio = "".join([item.get("audio", "") for item in response])
            return JSONResponse(content={
                "text": full_text,
                "url": "",
                "app": "",  # ✅ Ensure key is present even if empty
                "audio": combined_audio,
                "reminder": None
            })

        elif isinstance(response, bytes):
            return JSONResponse(content={
                "text": "Response received",
                "url": "",
                "app": "",  # ✅ Ensure key is present even if empty
                "audio": response.decode("utf-8"),
                "reminder": None
            })

        else:
            return JSONResponse(content={
                "text": "OK",
                "url": "",
                "app": "",  # ✅ Ensure key is present even if empty
                "audio": "",
                "reminder": None
            })
#
    except Exception as e:
        print("[ERROR - /process]:", e)
        raise HTTPException(status_code=500, detail="Internal server error.")

