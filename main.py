from flask import Flask, render_template, request, redirect, url_for, flash
import chatbot
app = Flask(__name__)

@app.route('/')
def Chat_bot():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    mensajes_in = []
    b = chatbot.chatBot()
    if request.method == 'POST':

        contador = request.form['contador_final']

        for i in range(int(contador)):
            mensaje = request.form[str(i)]

            mensajes_in.append(mensaje)

        user = request.form['input']

        mensajes_in.append(user)

        respuesta = b.get_respuesta(user)

        mensajes_in.append(respuesta)
        
    
    return render_template('index.html', mensajes = mensajes_in)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
