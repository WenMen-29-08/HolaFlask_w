## Importamos flask
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

## Definimos la ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"

## Ahora tomamos la segunda ruta y la reemplazamos por el siguiente ejemplo
## 1.) Haga un programa que calcule el promedio de notas sabiendo que tienen un valor de
## 30%, 30% y 40% respectivamente.
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1> <hr>"  
    
    ## Tomamos la tercera ruta y la reemplazamos por el siguiente ejemplo
## 2.) Un programa que al capturar la edad de una persona diga si es:
## Menor de edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad < 18:
        R = "menor de edad"
    elif edad < 60:
        R = "Adulto"
    else:
        R = "Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

    
    ## Creamos otra ruta ruta relizamos el siguiente ejemplo
## 3.) Programa que crea arreglos con valores aleatorios
## Importamos la libreria numpy si no existe la instalamos con: pip install numpy
import numpy as np

@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0, columnas=0, filas=0):
    if filas == 0:
        arreglo = np.random.randint(valores, size=columnas)
    else:
        arreglo = np.random.randint(valores, size=(filas, columnas))

    return f"<h1>El arreglo aleatorio es: {arreglo}</h1> <hr>"





# Ejercicio 1: Calcular ecuación
@app.route("/ecuacion/<float:x>/<float:z>")
def ecuacion(x, z):
    Y = x * z + z + x

    return f"<h1>El resultado de la ecuacion es: {Y:.2f}</h1><hr>"


# Ejercicio 2: Tabla de multiplicar
@app.route("/tabla/<int:num>")
def tabla(num):
    R = "<h1>Tabla de multiplicar</h1>"

    for i in range(1, 11):
        R += f"{num} x {i} = {num * i}<br>"

    return R + "<hr>"


import math

# Ejercicio 3: Area del circulo
# Ejercicio: Área del círculo
@app.route("/areas/circulo/<float:radio>")
def circulo(radio):
    R = math.pi * radio ** 2

    return f"<h1>El area del circulo es: {R:.2f}</h1><hr>"


# Area del cuadrado
@app.route("/areas/cuadrado/<float:lado>")
def cuadrado(lado):
    R = lado * lado

    return f"<h1>El area del cuadrado es: {R:.2f}</h1><hr>"


# Area del triangulo
@app.route("/areas/triangulo/<float:base>/<float:altura>")
def triangulo(base, altura):
    R = (base * altura) / 2

    return f"<h1>El area del triangulo es: {R:.2f}</h1><hr>"
if __name__ == '__main__':
    ## El valor True indica que la app se deja en modo debug
    app.run(debug=True)