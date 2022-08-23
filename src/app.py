from flask import Flask, render_template, url_for, request, redirect, request

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

#ruta con parametros
@app.route("/perfil/<nombre>")
def perfil(nombre):
	return render_template("perfil.html", name=nombre)

#ruta con parametros
@app.route("/perfil/<nombre>/<int:edad>/<string:carrera>")
def perfil_detallado(nombre, edad, carrera):
	info = {
		'nombre': nombre,
		'edad': edad,
		'carrera': carrera,
	}
	return render_template("perfil.html", data=info)

#ruta de error 404
#@app.errorhandler(404) #omitido por el decorador directo en la funcion
def page_not_found(error):
   return render_template('404.html'), 404
	#return redirect(url_for('index')) #redireccionar a la pagina principal

def ruta_parametros(p1):
	print(request)
	print(request.args)
	#obtener el valor de un parametro
	print(request.args.get('p1'))
	print(request.args.get('p2'))
	p1 = request.args.get('p1')
	return render_template("parametros.html", p1)

if __name__ == "__main__":
	app.add_url_rule('/parametros', view_func = ruta_parametros)
	app.register_error_handler(404, page_not_found)
	app.run(debug=True, port=5000)
