# website-security-header-analyser
## Overview
A Python tool that checks whether a website includes important security headers that protect against common web attacks. This project demonstrates practical web security knowledge and aligns with OWASP best practices — perfect for cybersecurity placements.


## 🚀 Features
- Sends a HTTP request to any website
- Checks for the presence of key security headers
- Flags missing headers with explanations
- Helps identify potential vulnerabilities
- Fully commented code
- No external setup required


## 🔍How It Works
The tool performs the following steps:
- Sends an HTTP GET request to the target website
- Retrieves the response headers
- Compares them against a list of recommended security headers
- Displays which headers are present or missing
- Provides explanations for missing headers
This helps users understand how secure a website is and what improvements can be made.

## 🖥️ Usage
- Run the script
- Enter a website URL
- View which security headers are present and which are missing

## 📂 Code Overview
The script uses:
- requests.get() → sends HTTP requests
- response.headers → retrieves website headers
- A dictionary → stores required headers and descriptions
- A loop → checks each header and prints results
The code is fully commented so as to explain each step clearly.


## 🔧 Future Improvements
- Add support for JSON export
- Add a website grade/score system
  
## 📸 Screenshots
<img width="512" height="299" alt="Screenshot 2026-10-14 183553" src="https://github.com/user-attachments/assets/29c4d2e8-e38d-4055-896c-3ea650e97922" />


## 🎯 What I Learned
This project helped me to understand:
- How security headers protect web applications
- Why missing headers increase vulnerability
- How browsers enforce security policies
- How to analyse HTTP responses using Python

