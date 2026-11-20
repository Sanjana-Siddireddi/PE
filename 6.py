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


baseline = """
Explain how a college student can manage monthly expenses.
Give five practical suggestions.
"""
role = """
You are a financial advisor who specializes in helping college students.
Explain how a college student can manage monthly expenses.
Give five practical suggestions in simple English.
"""
negative = """
You are a financial advisor who specializes in helping college students.
Explain how a college student can manage monthly expenses.
Give five practical suggestions in simple English.
Do not mention brand names, recommend financial products, or include advertisements.
"""
print("BASELINE")
print(ask_ai(baseline))
print("\nROLE-BASED")
print(ask_ai(role))
print("\nROLE + NEGATIVE")
print(ask_ai(negative))
