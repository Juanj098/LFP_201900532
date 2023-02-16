print('----------Bienvenido-------------')
Doc= input("Ingrese documento ->")

with open(Doc, 'r') as file:
    contenido = file.readlines()

peliculas=[]
class Movies:
    def __init__(self,name,actors,year,gender):
        self.name = name
        self.actors = actors
        self.year = year
        self.gender = gender
    def mostrar(self):
        print(self.name,self.actors,self.year,self.gender)
    def MostrarActors(self):
        pass        

for linea in contenido:
    datos = linea.split(";")
    pelicula = Movies(datos[0],datos[1],datos[2],datos[3])
    peliculas.append(pelicula)
for i  in range(len(peliculas)):
    print([i],peliculas[i].mostrar())


