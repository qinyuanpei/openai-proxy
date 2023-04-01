import openai
 
openai.api_key = 'sk-'
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",#gpt-3.5-turbo-0301
    messages=[
    {"role": "user", "content": "ʲô"}
    ],
    temperature=0.5,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    )
print(response.choices[0].message.content)
