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


puzzle = """
Five students—Asha, Bharat, Charan, Divya and Esha—stand in a line
from position 1 to position 5.
1. Asha is to the left of Bharat.
2. Charan is in position 3.
3. Divya is immediately to the right of Bharat.
4. Esha is not at either end.
Find the order from position 1 to position 5.
"""
direct = "Solve this puzzle and give the final order:\n" + puzzle
reasoning = """
Solve this following puzzle.
Let's do step by step.
Expalin the reasoning before the final answer.
Provide the final order fo five students from position 1 to position 5.
""" + puzzle


# Sub-question 1 
sub1_prompt = f""" 
Read the following logic puzzle. 
{puzzle} 
Sub-question 1: 
Who must be in position 3 ?
Give only the answer and a short explanation. 
""" 
sub1_output = ask_ai(sub1_prompt)

# Sub-question 2 
sub2_prompt = f""" 
Solve the following logic puzzle. 
{puzzle} 
Previous result: 
{sub1_output} 
Sub-question 2: 
Which positions are possible for bharat and divya ? """
sub2_output = ask_ai(sub2_prompt)

# Sub-question 3 
sub3_prompt = f""" 
Solve the following logic puzzle.
{puzzle} 
Previous result 1: 
{sub1_output} 
Previous result 2: 
{sub2_output} 
Sub-question 3: 
Where can esha stand ? 
""" 
sub3_output = ask_ai(sub3_prompt)

# Sub-question 4 – Combine 
sub4_prompt = f""" 
You are given a logic puzzle and the results of three previous sub-questions. 
Puzzle: 
{puzzle} 
Sub-question 1 result: 
{sub1_output} 
Sub-question 2 result: 
{sub2_output} 
Sub-question 3 result: 
{sub3_output} 
Sub-question 4: 
Combine the previous results and provide the final order of Asha, Bharat, Charan, Divya and Esha from position 1 to position 5. 
Return only the final order and a one-sentence justification. """ 
decomposed_output = ask_ai(sub4_prompt)

print("DIRECT ANSWER")
print(ask_ai(direct))
print("\nREASONING-ORIENTED")
print(ask_ai(reasoning))
print("\nSub-question 1:")
print(ask_ai(sub1_prompt)) 
print("\nSub-question 2:") 
print(sub2_output) 
print("\nSub-question 3:") 
print(sub3_output)
print("\nTASK DECOMPOSITION")
print(decomposed_output)
