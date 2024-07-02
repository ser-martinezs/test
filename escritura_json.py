import json
# Datos JSON
datos = {
"nombre": "Esteban",
"edad": 25,
"comuna": "Santiago",
"estudios": ["colegio Arturo Prat", "liceo el bosque",
"Duoc UC", "Diplomado Duoc UC"]
}# Abre el archivo, w es escritura
with open('archivo.json', 'w') as archivo:
	json.dump(datos, archivo)
