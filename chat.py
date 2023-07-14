import openai
  
  
def get_gpt_summary(message, api_key):
    openai.api_key  = api_key
    
    messages = [ {"role": "system", "content": 
                "Jesteś inteligentnym polskim opisywaczem produktów na stronę internetową OutletRTVAGD. \
                User daje ci opis, który musisz krótko streścić (od 25 do 250 słów) oraz podać \
                w oddzielnych punktach właściwośći(od 3 do 8)"} ]

    messages.append(
        {"role": "user", "content": message},
    )
    
    chatgpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
        
    reply = chatgpt.choices[0].message.content
    
    
    return reply
