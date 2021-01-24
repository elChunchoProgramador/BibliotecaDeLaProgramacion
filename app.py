from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL
from datetime import datetime
 

app = Flask(__name__)

mysql = MySQL()
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "sistema"
mysql.init_app(app)


@app.route("/")
def inicio():
    return render_template("rutas/index.html")

#--------------------------------------------------------------------------------- Python
@app.route("/masPython")
def masPython():
    return render_template("recursosLenguajes/masPython.html")

@app.route("/instalaride")
def intalarIde():
    return render_template("recursosLenguajes/pythonRecursos/instalaride.html")


#--------------------------------------------------------------------------------- Python

@app.route("/create")
def crear():
    return render_template("rutas/create.html")

"""@app.route("/probando")
def probando():
    return render_template("/rutas/footer.html")"""


@app.route('/store', methods=['POST'])
def storage():
    _nombre = request.form["txtNombre"] # obtenemos los valores insertados en el formulario
    _correo = request.form["txtCorreo"] # obtenemos los valores insertados en el formulario
    _foto = request.files["txtFoto"] # obtenemos los valores insertados en el formulario
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if _foto.filename != "":
        nuevoNombre = tiempo + _foto.filename
        _foto.save("imagenUsuario/" + nuevoNombre)

        sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);"
        datos = (_nombre, _correo, nuevoNombre)

    else:
        sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);"
        datos = (_nombre, _correo, _foto.filename)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return render_template("rutas/index.html")


if __name__ == "__main__":
    app.run(debug=True)