# 🎹 Piano Virtual en Python

Este es un **piano virtual** que permite tocar notas musicales utilizando el teclado de la computadora.  
Cada tecla del teclado está mapeada a una nota musical, y al presionar una de ellas, se reproduce el sonido correspondiente.

---

## 🛠️ **Requisitos Previos**
Antes de ejecutar el programa, asegúrate de tener instalado:

- **Python 3.7+** 

---
## Crear un Entorno Virtual

Es recomendable usar un entorno virtual para evitar conflictos con otras librerías.
Windows (PowerShell)

python -m venv venv
venv\Scripts\activate

Mac/Linux

python -m venv venv
source venv/bin/activate

Si el entorno virtual está activado, verás (venv) al inicio de la línea en la terminal.

## Instalar Dependencias

Ejecuta el siguiente comando para instalar pygame y otras dependencias necesarias:

pip install -r requirements.txt

Si en algún momento deseas actualizar requirements.txt, usa:

pip freeze > requirements.txt

## Verificar los Archivos de Sonido

Asegúrate de que en la carpeta sounds/ existen los archivos .wav:

sounds/do.wav
sounds/re.wav
sounds/mi.wav
sounds/fa.wav
sounds/sol.wav
sounds/la.wav
sounds/si.wav

## Ejecutar el Programa

Para correr el piano virtual, usa este comando en la terminal:

python src/main.py

