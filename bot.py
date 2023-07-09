import openai
import os
import requests
openai.api_key = os.getenv('OPENAI_TOKEN')


def OpenArtificialIntelligence(prompt) :
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return chat_completion.choices[0].message.content

def sendTextMessage(message) : 
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": os.getenv('TEST_PHONE_NUMBER'),
            "type": "text",
            "text": {
                "body": message
            }
        }
    response = requests.post('https://graph.facebook.com/v15.0/103136212562162/messages', headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer '+os.getenv('FACEBOOK_API')
            }, json=data)
    return response

