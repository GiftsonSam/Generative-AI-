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
          "text": """Below are several social media posts. For each post, please analyze the sentiment expressed and classify it as either positive, negative, or neutral. Provide a brief explanation for your classification"
                  "1. Just got my hands on the new XPhone - absolutely loving the camera and battery life! 📸🔋 #TechLove
2. Disappointed with the XPhone. Its pricey and not much different from the last model. Expected more. 😕 #TechTalk
3. XPhones latest update is a game-changer for mobile gaming. The graphics are just incredible! 🎮💯
4. Cant believe I waited this long for the XPhone... its underwhelming and overpriced. Back to my old phone, I guess. 😒
5. The XPhone has exceeded my expectations. Fast, sleek, and the new AI features are a standout! 🚀 #Innovation"""

        }
      ]
    },
  
  ],
  
   
)



print(response.choices[0].message.content) 
