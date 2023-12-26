from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    user_state = request.form['userState']  # Retrieve the user state from the form

    # Logic to determine the server's reply based on user input and state
    if user_input.lower() == 'dummy' and user_state == 'initialState':
        server_reply = 'Hi'
        new_state = 'greeted'  # Update the state as needed
    else:
        server_reply = 'Bye'
        new_state = 'default'

    # Include the updated state in the response
    return render_template('chat.html', user_input=user_input, server_reply=server_reply, user_state=new_state)

if __name__ == '__main__':
    app.run(debug=True)
