import sys
import json
import subprocess

# Get requirement from command line
requirement = sys.argv[1] if len(sys.argv) > 1 else "No requirement provided"
print(f"Requirement: {requirement}\n")

# ---- STEP 1: Call Ollama and get AI response ----
prompt = f"""
Generate 2-3 test cases for the following requirement in JSON format:
Requirement: {requirement}

Each test case should have:
- id
- description
- preconditions
- steps
- expected
"""

result = subprocess.run(
    ["ollama", "run", "llama3"],
    input=prompt,
    text=True,
    capture_output=True
)

response_text = result.stdout.strip()
print("Raw AI Output:\n", response_text, "\n")

try:
    start = response_text.find("[")
    end = response_text.rfind("]") + 1
    json_str = response_text[start:end]
    generated_cases = json.loads(json_str)
except Exception as e:
    print("Error parsing AI output:", e)
    generated_cases = []

# ---- STEP 3: Print test cases ----
if generated_cases:
    print("Generated Test Cases:\n")
    for case in generated_cases:
        print(f"ID: {case.get('id', '')}")
        print(f"Description: {case.get('description', '')}")
        print(f"Preconditions: {case.get('preconditions', '')}")
        print(f"Steps: {case.get('steps', '')}")
        print(f"Expected: {case.get('expected', '')}")
        print("-" * 50)
else:
    print("⚠️ No test cases generated.")
