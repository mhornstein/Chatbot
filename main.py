from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    if user_input.lower() == 'dummy input':
        server_reply = 'Hi'
    else:
        server_reply = 'Bye'
    return render_template('chat.html', user_input=user_input, server_reply=server_reply)

if __name__ == '__main__':
    app.run(debug=True)
