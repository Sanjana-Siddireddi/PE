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

p1 = "Summarize the plot of Romeo and Juliet."
p2 = """
Summarize Romeo and Juliet in exactly two sentences.
Use simple English suitable for a school student.
"""
p3 = """
Summarize Romeo and Juliet in exactly two sentences.
Mention Verona, the conflict between two rival families,
the love of Romeo and Juliet, and how the tragedy shows
the destructive nature of hatred. Use simple English.
"""
for title, prompt in [("ITERATION 1", p1), ("ITERATION 2", p2), ("ITERATION 3", p3)]:
 print("\n" + title)
 print(ask_ai(prompt))
