# **🤖 Gemini API Educational Content Generator**

This project demonstrates how to programmatically interact with the Google Gemini API using Python to generate educational and creative text-based content.

The primary goal of this repository is to provide a clean, runnable example of API usage for students and developers.

## **Prerequisites**

Before starting, ensure you have the following installed on your system:

* **Python 3.x**  
* **A Gemini API Key** (obtained from Google AI Studio)

## **🚀 Setup and Installation**

Follow these steps to set up your project environment and install the required Python library. Using a virtual environment (venv) is strongly recommended to isolate dependencies.

### **1\. Create and Activate the Virtual Environment**

Open your terminal (or VS Code's integrated terminal) in the project directory and execute the commands below:

\# 1\. Create the virtual environment named .venv  
python \-m venv .venv

\# 2\. Activate the environment (select the command based on your Windows shell)  
\# For PowerShell (PS):  
.venv\\Scripts\\Activate.ps1  
\# For Command Prompt (cmd.exe):  
.venv\\Scripts\\activate

Upon successful activation, your terminal prompt will display (.venv).

### **2\. Install Dependencies**

With the virtual environment active, install the official Google GenAI SDK:

pip install google-genai

## **⚙️ Configuration**

The main script, bot.py, is configured to directly use your API key for immediate functionality.

The key is set in the bot.py file like this:

client \= genai.Client(api\_key="GEMINI\_API\_KEY")

**⚠️ Security Warning:** This method is quick for testing, but for any production application, **always** load your API key from a secure environment variable (e.g., $env:GEMINI\_API\_KEY) to prevent accidental leakage.

## **▶️ Usage**

To run the script and generate content, ensure your virtual environment is active and execute:

python bot.py

### **Script Functionality**

The script performs two example API calls:

1. **Educational:** Explains the concept of "Net Present Value" (NPV).  
2. **Creative:** Generates a short poem about Python programming.