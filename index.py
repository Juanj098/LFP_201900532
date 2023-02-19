
print('<----------Bienvenido------------->')
Doc = input("Ingrese documento -> ")

with open(Doc, 'r') as file:
    contenido = file.readlines()

class Movies:
    def __init__(self,name,actors,year,gender,x):
        self.name = name
        self.actors = actors
        self.year = year
        self.gender = gender
        self.x = x

    def mostrar(self):
        print("Pelicula:",self.name)
        print("Actores:",self.actors)
        print("Año de estreno:",self.year)
        print("Genero:",self.gender)

    def mostrarActors(self):
        print(self.actors)    

    def mostrarPelis(self):
        print(self.x,self.name)  
    
    def id(self):
        return self.x
        
    
    def actores(self):
        for u in range(len(self.actors)):
            print(self.actors[u].strip())
    


print("<--------------------------------->")
print("<             MENU                >")
print("1. Gestionar peliculas")
print("2. Filtrado")
print("3. Graficar")
print("4. salir")
print("<--------------------------------->")
opc = input("Ingrese opcion: ")
peliculas=[]
actoresAr = []
cont = 0
for linea in contenido:
    datos = linea.split(";")
    person = datos[1].split(",")
    actoresAr.append(person)
    pelicula = Movies(datos[0],actoresAr[cont],datos[2],datos[3],cont)
    cont= cont+1
    peliculas.append(pelicula)
if opc == "1":#Gestionar peliculas
    print("--------Gestionar peliculas--------")
    print("a.Mostrar peliculas")
    print("b.Mostrar actores")
    print("-----------------------------------")
    opc2 = input("ingrese opcion: ")
    if opc2 == "a":
    #imprime peliculas y datos
        for i  in range(len(peliculas)):
            if peliculas[i].mostrar() != None:
                print(peliculas[i].mostrar())
    elif opc2 =="b":
    #imprime actores 
        print("<----------------------------------->")
        for x in range(len(peliculas)):
            if peliculas[x].mostrarPelis() != None:
                print(peliculas[x].mostrarPelis())  
        print("<----------------------------------->")
        opc3 = input("Ingrese No. de pelicula: ")
        opc3=int(opc3)
        for y in range(len(peliculas)):
            if opc3 == peliculas[y].id():
                if peliculas[y].actores() != None:
                    print(peliculas[y].actores())
    else:
        print("Opcion Invalida")

elif opc == "2":#filtrado
    print("Holi :3")
elif opc == "3":#Grafica
    print("opcion 3")
elif opc == "4":
    print("opcion 4")
else:
    print("opcion invalida rata inutil >:p ")