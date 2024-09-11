from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Categorise the companies given : "
          "Microsoft Corporation, Roche Holding AG, Apple Inc"
          "Amazon.com, Inc,Pfizer Inc, JPMorgan Chase & Co."
          "Johnson & Johnson, Bank of America Corporation, Industrial and Commercial Bank of China ."
        }
      ]
    },
  
  ],
  
   
  max_tokens=300,
  
)

print(response.choices[0].message.content) 
