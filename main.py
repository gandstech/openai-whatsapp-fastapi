from fastapi import FastAPI, Request, Response, status
import os
from dotenv import load_dotenv
load_dotenv()
import bot


app = FastAPI()

@app.get("/python-fastapi/webhook/facebook")
async def facebookWebhookVerify(request: Request, response: Response):
    params = request.query_params._dict
    mode = params["hub.mode"]
    token = params["hub.verify_token"]
    challenge = params["hub.challenge"]
    if (mode and token) :
        if (mode == "subscribe" and token == os.getenv('VERIFYTOKEN')) :
            print("WEBHOOK_VERIFIED")
            return int(challenge)
        else :
            response.status_code = 403
            return ""

@app.post("/python-fastapi/webhook/facebook")
async def facebookWebhook(request: Request):
    body = await request.json()
    if(len(body.get('entry')) and body.get('entry')[0]["changes"]) :
        changes = body.get('entry')[0]["changes"]
        message = changes[0]["value"]["messages"][0] if 'messages' in changes[0]["value"] else False
        if message and message["type"] == "text" :
            message_to_send = bot.OpenArtificialIntelligence(message["text"]["body"])
            bot.sendTextMessage(message_to_send)
    return 'Hello GandS!'