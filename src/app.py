from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
# url_for('static', filename='index.css')

#ruta de la pagina principal
@app.route("/")
def index():
   asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
   info = {
		'nombre': 'Juan Carlos Ruiz Montaño',
		'edad': 20,
		'carrera': 'Ingeniería en Sistemas Computacionales',
		'semestre': 9,
		'telefono': '331 123 4567',
		'asignaturas': asignaturas,
		'lenasignatura' : len(asignaturas),
	}
   return render_template("index.html", info=info)

#ruta de error 404
@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html'), 404

if __name__ == "__main__":
   app.run(debug=True, port=5000)
