from flask import Flask, render_template, request

app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página Quiénes Somos
@app.route('/about')
def about():
    return render_template('about.html')

# Página de Servicios
@app.route('/services')
def services():
    return render_template('services.html')

# Página de Noticias
@app.route('/news')
def news():
    return render_template('news.html')

# Página de Contacto con manejo del formulario POST
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí puedes agregar la lógica para procesar los datos, enviarlos por correo o guardarlos en la base de datos
        return f"Gracias {name}, hemos recibido tu mensaje."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
