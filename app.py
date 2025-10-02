from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "clave_secreta")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'jimenezbarrera1011@gmail.com'
app.config['MAIL_PASSWORD'] = 'xvkc gwfn qdqa zplk'
app.config['MAIL_DEFAULT_SENDER'] = 'jimenezbarrera1011@gmail.com'
mail = Mail(app)

info_evento = {
    1: {
        "nombre": "Rally MTB Rural 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": "Competencia de MTB rural con recorrido de caminos rurales, sierras y senderos en dos modalidades: 30 km y 80 km.",
        "fecha": "24 de Octubre de 2025",
        "horario": "08:00 AM",
        "lugar": "Tandil, Buenos Aires",
        "tipo_carrera": "MTB Rural",
        "modalidad_costo": {
            "corta": {"nombre": "Recorrido Corta Distancia (30 km)", "valor": "100"},
            "larga": {"nombre": "Recorrido Larga Distancia (80 km)", "valor": "200"}
        },
        "kit_carrera": [
            "Camiseta técnica oficial del evento",
            "Número de participante y fijaciones",
            "Medalla conmemorativa de finisher"
        ],
        "auspiciantes": [
            "Villavicencio",
            "Gatorade",
            "nike",
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        telefono = request.form.get("telefono", "No proporcionado")
        modalidad = request.form.get("modalidad")
        
        nombre_modalidad = "Corta - 30km" if modalidad == "corta" else "Larga - 80km"
        
        cuerpo_email = f"""
        NUEVA INSCRIPCIÓN - RALLY MTB RURAL 2025

        DATOS DEL PARTICIPANTE:

        Nombre: {nombre}
        Email: {email}
        Teléfono: {telefono}
        Modalidad seleccionada: {nombre_modalidad}
        """

        msg = Message(
            subject = "Nueva Inscripción: " + nombre + " - " + nombre_modalidad,
            recipients=['ajimenezb@fi.uba.ar'],
            body=cuerpo_email
        )
        mail.send(msg)
        flash("¡Inscripción enviada correctamente")
        return redirect('/contact')
    return render_template('contact.html')

if __name__ == "__main__":
    app.run("localhost", port=8080, debug=True)