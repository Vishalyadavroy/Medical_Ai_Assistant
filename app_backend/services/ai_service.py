import os 
from openai import OpenAI
from app_backend.utils.prompts import MEDICAL_SYSTEM_PROMPT

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_medical_answer(question:str) ->str:
    models = client.models.list()
    for model in models.data:
        print(model.id)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system" ,  "content":MEDICAL_SYSTEM_PROMPT},
            {"role":"user" , "content":question}
        ],
        temperature = 0.3
    )
    return response.choices[0].message.content
