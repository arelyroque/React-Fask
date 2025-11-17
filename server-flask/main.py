#impotar flask
from flask import Flask
# importar CORS
from flask_cors import CORS 

#crear una instancia de flask
app = Flask(__name__)
#habilitar CORS en la aplicacion
CORS(app)

#definir una ruta para la raiz
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__': #punto de entrada de la aplicacion
    app.run(debug=True) #ejecutar la aplicacion en modo debug 

