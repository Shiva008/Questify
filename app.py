from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
load_dotenv()
import os
openai.api_key = os.getenv('OPENAI_API_KEY')
prompt = """
You are a AI system that conducts engaging and unbiased user research interviews. It should introduce the purpose, generate insightful follow-up questions based on user feedback, adapt naturally, and avoid bias. Evaluate based on question quality, dynamic adaptation, and user experience. Bonus for summarizing responses and integrating sentiment analysis.
Add your own question also.
When the user types 'end,' end the conversation and provide feedback. Include some fields where the user can improve. Take reference from the chat and give the user an honest review.
"""

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"]
    if user_input.lower() == "end":
        return "Conversation ended."
    
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_input}
    ]
    response = get_chat_response(messages)
    return response

def get_chat_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run(debug=True)
