import numpy as np
from openai import OpenAI
client = OpenAI()

doc1 = "Climate change is a pressing global crisis that requires urgent action. Rising sea levels, extreme weather events, and biodiversity loss are just a few of the devastating consequences of this environmental issue."
doc2 = "The Industrial Revolution marked a significant turning point in human history, characterized by rapid technological advancements and increased industrialization. This period led to significant economic growth but also contributed to environmental pollution and social inequality."
doc3 = "Artificial intelligence (AI) has the potential to revolutionize various industries, from healthcare to transportation. However, the development and deployment of AI also raise ethical concerns, such as job displacement and privacy violations."
plag_text = "The Industrial Revolution was a pivotal era in human history, characterized by rapid technological advancements and increased industrialization. This period led to significant economic growth but also contributed to environmental pollution and social inequality. Climate change, a pressing global issue, is a direct consequence of human activities during and after the Industrial Revolution. Rising sea levels, extreme weather events, and biodiversity loss are just a few of the devastating consequences of this environmental crisis. While artificial intelligence (AI) offers immense potential to improve our lives, it also raises ethical concerns, such as job displacement and privacy violations."

docs = [plag_text, doc1, doc2, doc3]
response = client.embeddings.create(
    model = "text-embedding-ada-002",
    input = docs

    )
plag_embd = response.data[0].embedding

for i in range(1, len(docs)):
    embd = response.data[i].embedding
    sim_score = np.dot(plag_embd,embd) * 100
    print("Similarity between plag text and doc{0} is {1}%".format(1,sim_score))
    
