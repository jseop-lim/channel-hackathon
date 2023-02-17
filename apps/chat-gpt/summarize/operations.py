import os
import openai

openai.api_key = os.getenv("OPEN_API_KEY")


def summarize(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""summarize this in 3 lines:
        
        {text}""",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response
