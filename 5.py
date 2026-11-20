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


sentences = [
 "The laboratory session was very interesting.",
 "The software installation failed several times.",
 "The class started at 10 AM.",
 "The teacher explained the experiment clearly.",
 "The computer stopped working during the experiment."
]
zero_prompt = """
Classify each sentence as Positive, Negative, or Neutral.
Return only the labels in order. Do not explain.
""" + "\n".join(sentences)
few_prompt = """
Classify sentiment as Positive, Negative, or Neutral.
Examples:
The laboratory was excellent. -> Positive
The computer was not working. -> Negative
The class started at 10 AM. -> Neutral
Now classify these sentences. Return only labels in order:
""" + "\n".join(sentences)
print("ZERO-SHOT")
print(ask_ai(zero_prompt))
print("\nFEW-SHOT")
print(ask_ai(few_prompt))
