import google.generativeai as genai
import os


# Configure the Gemini API
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize the model
llm = genai.GenerativeModel('gemini-pro')

# Make the API call
response = llm.generate_content("who is Prime minister of pakistan")
print(response.text)