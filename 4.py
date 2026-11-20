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


prompt_1_bad = """
Explain Python.
"""
prompt_1_good = """
You are a Python programming instructor.
Explain the Python programming language to first-year B.Tech CSE students.
Include:
1. Definition of Python
2. Three important features
3. Three common applications
Use simple English and present the answer using headings and bullet points.
"""

prompt_2_bad = """
Summarize the project.
"""

prompt_2_good = """
Summarize the following project for a B.Tech project report in approximately 100 words.
Project Title: Smart Campus Attendance System
Project Description:
The project uses face recognition to automatically record student attendance. A camera captures the student's face, the system compares it with registered student data, and attendance is recorded in a database.
Include the objective, basic working process and main benefit. Use simple academic English.
"""

prompt_3_bad = """
Give information about three programming languages. """

prompt_3_good = """
Create a Markdown table comparing exactly three programming languages: Python, Java and C++.
Use the following columns:
Language | Main Use | Key Feature | Difficulty Level
Provide exactly one row for each programming language. Do not add information outside the table.
"""

print("CASE 1 – AMBIGUITY")
print("\nFAULTY OUTPUT:")
print(ask_ai(prompt_1_bad))
print("\nREFINED OUTPUT:")
print(ask_ai(prompt_1_good))
print("\n\n")
print("CASE 2 – MISSING CONTEXT")
print("\nFAULTY OUTPUT:")
print(ask_ai(prompt_2_bad))
print("\nREFINED OUTPUT:")
print(ask_ai(prompt_2_good))
print("\n\n")
print("=" * 70)
print("CASE 3 – FORMAT ERROR")
print("=" * 70)
print("\nFAULTY OUTPUT:")
print(ask_ai(prompt_3_bad))
print("\nREFINED OUTPUT:")
print(ask_ai(prompt_3_good))
