<img width="1536" height="1024" alt="AWS translation chatbot workflow diagram" src="https://github.com/user-attachments/assets/56ebeba7-3adb-4bd7-9cf4-0db8c6cb613d" />

# 🌍 AWS Language Translation Chatbot

A serverless chatbot built using AWS services that translates user input into different languages in real time.

---

## 🚀 Overview

This project uses Amazon Lex to create an intelligent chatbot that allows users to input text and receive translations in a specified language. 
The chatbot processes user input, sends it to AWS Lambda for backend logic, and uses Amazon Translate to generate accurate translations.

---

## 🧠 How It Works

1. User enters text into the chatbot  
2. Amazon Lex detects the intent and extracts slots (text + language)  
3. AWS Lambda processes the request  
4. Amazon Translate converts the text into the target language  
5. The translated text is returned to the user  

---

## 🛠️ AWS Services Used

- **Amazon Lex** – Chatbot creation and conversation flow  
- **AWS Lambda** – Backend processing (Python)  
- **Amazon Translate** – Text translation  
- **AWS IAM** – Access control and permissions  

---

## 📁 Project Structure
├── lambda/
│ └── translate.py # Python Lambda function for translation
├── README.md

## ⚙️ Lambda Function (Translation - Python)

This Lambda function:
- Extracts user input from Amazon Lex
- Validates the input and selected language
- Translates text using Amazon Translate
- Returns the translated text to the chatbot

python
import boto3

🔐 IAM Permissions
Ensure your Lambda role includes:
AmazonTranslateFullAccess
(Optional) Custom least-privilege policy for production

🧪 How to Test
Deploy the Lambda function
Create an Amazon Lex bot
Define:
Intent: TranslationIntent
Slots: text, language
Connect Lex → Lambda (Fulfillment)
Test with sample inputs in the Lex console

📌 Example
Input:
Translate "How are you?" to Spanish

Output:
¿Cómo estás?

💡 Future Improvements
Add text-to-speech (Amazon Polly) as an optional feature
Build a frontend UI (React or mobile app)
Support dynamic language detection and suggestions
Store translation history (DynamoDB)

👨‍💻 Author
Asa Gordon
Computer Science Student @ UTSA
Aspiring Software / Cloud Engineer

⭐️ Show Your Support
If you found this project helpful, feel free to star the repo!
