import openai
  
  
def get_gpt_summary(message, api_key):
    openai.api_key  = api_key
    messages = [ {"role": "system", "content": 
                "Jesteś inteligentnym polskim opisywaczem produktów na stronę internetową OutletRTVAGD. \
                User daje ci opis, który musisz krótko i treściwie(od 25 do 250 słów) streścić oraz podać \
                najważniejsze właściwośći(od 3 do 8) w oddzielnych punktach"} ]

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    
    return reply
