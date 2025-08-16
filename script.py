import sys
import ollama

if len(sys.argv) < 2:
    print("Usage: python script.py \"<requirement text>\"")
    sys.exit(1)

requirement = sys.argv[1]

print(f"📌 Requirement: {requirement}\n")

prompt = f"""
Generate detailed test cases (both positive and negative) for the following requirement:

{requirement}

Format the response as:
1. Test Case ID
2. Description
3. Steps
4. Expected Result
"""

response = ollama.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": prompt}]
)


print("✅ Generated Test Cases:\n")
print(response['message']['content'])
