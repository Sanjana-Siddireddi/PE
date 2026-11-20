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


import json
import yaml
dataset = """
The dataset contains three books :
1. Title: The Alchemist
   Author: Paulo Coelho
   Publication Year: 1988
2. Title: 1984
   Author: George Orwell
   Publication Year: 1949
3. Title: Pride and Prejudice
   Author: Jane Austen
   Publication Year: 1813
   """
json_prompt = f"""
Convert this book dataset into JSON.
Return only valid JSON with a top-level books array.
Each book must have title, author and publication_year.
No Markdown or explanation.
Dataset: {dataset}
"""
json_text = ask_ai(json_prompt)
print("JSON OUTPUT")
print(json_text)
try:
 print("Parsed JSON:", json.loads(json_text))
 print("JSON is valid.")
except json.JSONDecodeError as e:
 print("Invalid JSON:", e)
yaml_prompt = f"""
Convert this dataset into YAML with a top-level books list.
Each book must have title, author and publication_year.
Return only valid YAML, no Markdown or explanation.
Dataset: {dataset}
"""
yaml_text = ask_ai(yaml_prompt)
print("\nYAML OUTPUT")
print(yaml_text)
try:
 print("Parsed YAML:", yaml.safe_load(yaml_text))
 print("YAML is valid.")
except yaml.YAMLError as e:
 print("Invalid YAML:", e)
