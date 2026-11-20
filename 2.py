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


baseline = "Write a one-paragraph bio of Ada Lovelace."
enhanced = """
You are a computer science history teacher.
Write a short biography of Ada Lovelace for first-year B.Tech students.
Include her full name, contribution to computing, association with
Charles Babbage, and one important achievement.
Use simple English, approximately 150 words, in one paragraph.
"""
print("BASELINE OUTPUT")
print(ask_ai(baseline))
print("\nENHANCED OUTPUT")
print(ask_ai(enhanced))
