print('<----------Bienvenido------------->')
Doc = input("Ingrese documento -> ")

with open(Doc, 'r') as file:
    contenido = file.readlines()

class Movies:
    def __init__(self,name,actors,year,gender):
        self.name = name
        self.actors = actors
        self.year = year
        self.gender = gender
    def mostrar(self):
        print(self.name,self.actors,self.year,self.gender)
    def mostrarActors(self):
        print(self.actors)      

print("<--------------------------------->")
print("<             MENU                >")
print("1. Gestionar peliculas")
print("2. Filtrado")
print("3. Graficar")
print("4. salir")
print("<--------------------------------->")
opc = input("Ingrese opcion: ")
peliculas=[]
for linea in contenido:
    datos = linea.split(";")
    pelicula = Movies(datos[0],datos[1],datos[2],datos[3])
    peliculas.append(pelicula)
if opc == "1":
    for i  in range(len(peliculas)):
        if peliculas[i].mostrar() != None:
            print(peliculas[i].mostrar())
elif opc == "2":
    print("Holi :3")
elif opc == "3":
    print("opcion 3")
elif opc == "4":
    print("opcion 4")
else:
    print("opcion invalida rata inutil >:p ")