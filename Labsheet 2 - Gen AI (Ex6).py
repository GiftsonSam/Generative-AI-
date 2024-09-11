from openai import OpenAI
client = OpenAI(api_key="test")

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
   
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is OpenAI"
                    }
                    ]
            },
  
        ]
  
    )

except OpenAI().AuthenticationError as e:
    print(f"AuthenticationError : {e}")
 
