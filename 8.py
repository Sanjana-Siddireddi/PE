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


bullet_prompt = """
List five benefits of daily exercise.
Use exactly five bullet points, one benefit per point.
Use simple English. Do not use a table.
"""
table_prompt = """
Create a Markdown table about three benefits of daily exercise.
Use exactly two columns: Benefit and Description.
Include exactly three benefit rows. Do not add text outside the table.
"""
bullets = ask_ai(bullet_prompt)
table = ask_ai(table_prompt)
print("BULLET LIST")
print(bullets)
print("\nMARKDOWN TABLE")
print(table)
bullet_count = sum(1 for line in bullets.splitlines()
 if line.strip().startswith(("-", "*")))
print("\nBullet points detected:", bullet_count)
print("Markdown table detected:", "|" in table and "---" in table)
table_line = sum(1 for line in table.splitlines()
                  if line.strip())
print(table_line)
