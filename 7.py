from google.colab import userdata
from openai import OpenAI
client = OpenAI(api_key=userdata.get("OPENAI_API_KEY"), base_url="https://api.groq.com/openai/v1")
def ask_ai(prompt):
 response = client.responses.create(
 model="openai/gpt-oss-120b",
 input=prompt
 )
 return response.output_text
print("Setup complete!")


article = """
Cloud computing provides servers, storage, databases, networking and software
through the Internet. Its service models are IaaS, PaaS and SaaS. Benefits
include scalability, flexibility, resource sharing and reduced maintenance.
Security, privacy, availability and data management are important concerns.
"""
basic = "Summarize this article:\n" + article
cycle1 = f"""
Summarize this article in approximately 100 words.
Use exactly five bullet points and simple English.
Include the definition, service models, benefits, scalability and security.
Article: {article}
"""
cycle2 = f"""
You are a computer science teacher.
Summarize this article for first-year B.Tech students in approximately 100 words.
Use exactly five numbered points. Include:
1. Meaning of cloud computing
2. IaaS, PaaS and SaaS
3. Benefits
4. Scalability
5. Security and privacy concerns
Do not add facts outside the article.
Article: {article}
"""
for title, prompt in [("BASIC", basic), ("REFINEMENT CYCLE 1", cycle1), ("REFINEMENT CYCLE 2", cycle2)]:
 print("\n" + title)
 print(ask_ai(prompt))
