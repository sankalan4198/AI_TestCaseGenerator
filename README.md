AI Test Case Generator
This project automates test case generation from plain English software requirements using Large Language Models (LLMs). It leverages Ollama + llama3 (or any supported LLM) to convert requirements into structured JSON test cases.
🚀 Features
- Input requirements via command line
- Generates structured JSON test cases
- Includes: Test Case ID, Description, Preconditions, Steps, Expected Result
- Lightweight and extensible (can be integrated with Excel, databases, or APIs)
🛠️ Installation
1. Clone this repo:
git clone https://github.com/<your-username>/ai-testcase-generator.git
cd ai-testcase-generator
2. Create & activate a virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
3. Install dependencies:
pip install -r requirements.txt
4. Install Ollama and pull a model (e.g., llama3):
ollama pull llama3

▶️ Usage
Run the script with a requirement:
python script.py "As a user, I should be able to reset my password using my registered email"
📋 Example Output
[
  {
    "id": "TC001",
    "description": "Verify password reset with a registered email",
    "preconditions": "User has an existing account with a registered email",
    "steps": [
      "Navigate to the login page",
      "Click on 'Forgot Password'",
      "Enter registered email",
      "Click 'Submit'"
    ],
    "expected": "Password reset link should be sent to the registered email"
  },
  {
    "id": "TC002",
    "description": "Verify error handling for unregistered email",
    "preconditions": "No account exists with the entered email",
    "steps": [
      "Navigate to the login page",
      "Click on 'Forgot Password'",
      "Enter unregistered email",
      "Click 'Submit'"
    ],
    "expected": "System should show an error message: 'Email not found'"
  }
]

🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

