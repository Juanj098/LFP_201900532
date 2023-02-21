import os

print('<----------Bienvenido------------->')
Doc = input("Ingrese documento -> ")

with open(Doc, 'r') as file:
    contenido = file.readlines()

class Movies:
    def __init__(self,name,actors,year,gender,x):
        self.name = name
        self.actors = actors
        self.year = int(year)
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

    def actores2(self):
        for u in range(len(self.actors)):
            return self.actors[u].strip()  
        
    def actores3(self):
        return len(self.actors)

    def actores4(self, item):
        return self.actors[item].strip()
    
    def actores(self):
        for u in range(len(self.actors)):
            print("-",self.actors[u].strip())
    
    def yearDato(self):
        return self.year

    def generDato(self):
        return self.gender


print("<--------------------------------->")
print("<             MENU                >")
print("1. Gestionar peliculas")
print("2. Filtrado")
print("3. Graficar")
print("4. salir")
print("<--------------------------------->")
opc = input("Ingrese opcion: ")
os.system("cls")
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
#-->
while opc != "4":
    if opc == "1":#Gestionar peliculas

        print("---------Gestionar peliculas---------")
        print("a.Mostrar peliculas")
        print("b.Mostrar actores")
        print("-------------------------------------")
        opc2 = input("ingrese opcion: ")
        os.system("cls")
        while opc2 != "s":
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
                os.system("cls")
                opc3=int(opc3)
                print("<----------------------------------->")
                print("Actores")
                for y in range(len(peliculas)):
                    if opc3 == peliculas[y].id():
                        if peliculas[y].actores() != None:
                            print(peliculas[y].actores())
            else:
                print("Opcion Invalida")
            print("")
            print("")
            print("---------Gestionar peliculas---------")
            print("a.Mostrar peliculas")
            print("b.Mostrar actores")
            print("<----------------------------------->")
            print("             (S) Salir               ")
            print("<----------------------------------->")
            opc2 = input("ingrese opcion: ")
            os.system("cls")

#-->
            
    elif opc == "2":#filtrado
        print("<---------------------------->")
        print("a.Actor")
        print("b.Año de estreno")
        print("c.Genero")
        print("<---------------------------->")
        opc4=input("Ingrese opcion de filtro: ")
        os.system("cls")
        #->
        while opc4 != "s":
            if opc4 == "a": #actor

                arr2=[]
                diccionarioF = {}
        
                print("<------------------------------>")
                for b in range(len(peliculas)):
                    for c in range(int(peliculas[b].actores3())):
                        if peliculas[b].actores4(c) != None:
                            comodin = peliculas[b].actores4(c)
                            arr2.append(comodin)
                arr2.sort()
                for palabra in arr2:
                    if palabra in diccionarioF:
                        diccionarioF[palabra] += 1
                    else:
                        diccionarioF[palabra] = 1
                for palabra in diccionarioF:
                    print("-",palabra)
                print("<------------------------------->")
                opc5 = input("Ingrese nombre de actor: ")
                os.system("cls")
                print(opc5)
                print("<------------------------------->")

                for n in range(len(peliculas)):
                    for m in range(int(peliculas[n].actores3())):
                        if peliculas[n].actores4(m) != None:
                            if opc5 == peliculas[n].actores4(m) or opc5 == peliculas[n].actores4(m).lower():
                                peliculas[n].mostrar()
                        
            elif opc4 == "b": #estreno
                anios = []
                diccionarioF2 = {}
                print("<------------------------------>")
                for y in range(len(peliculas)):
                    if peliculas[y].yearDato() != None:
                        an = peliculas[y].yearDato()
                        anios.append(an)
                anios.sort()
                for ye in anios:
                    if ye in diccionarioF2:
                        diccionarioF2[ye] += 1
                    else:
                        diccionarioF2[ye] = 1
                for p in diccionarioF2:
                    print("-",p)
                print("<------------------------------>")
                opc6 = input("Ingrese año de estreno: ")
                os.system("cls")
                print(opc6)
                print("<------------------------------>")
                for yy in range(len(peliculas)):
                    if peliculas[yy].yearDato() != None:
                        if peliculas[yy].yearDato() == int(opc6):
                            if peliculas[yy].mostrar() != None:
                                print(peliculas[yy].mostrar())

            elif opc4 == "c": #Genero

                genero=[]
                diccionarioF3 ={}
                print("<------------------------------>")
                for q in range(len(peliculas)):
                    if peliculas[q].generDato() != None:
                        generos = peliculas[q].generDato().strip()
                        genero.append(generos)
                for gen in genero:
                    if gen in diccionarioF3:
                        diccionarioF3[gen]+=1
                    else:
                        diccionarioF3[gen]=1
                for g in diccionarioF3:
                    print("-",g)
                print("<------------------------------>")
                opc7 = input("Ingrese Genero: ")
                os.system("cls")
                print(opc7)
                print("<------------------------------>")
                for pe in range(len(peliculas)):
                    if peliculas[pe].generDato()!=None:
                        if opc7 == peliculas[pe].generDato().lower().strip() or opc7 == peliculas[pe].generDato().strip():
                            if peliculas[pe].mostrar()!=None:
                                print(peliculas[pe].mostrar())  
            else:
                print("opcion invalida")
            print("<----------------------------------->")
            print("a.Actor")
            print("b.Año de estreno")
            print("c.Genero")
            print("<----------------------------------->")
            print("             (S) Salir               ")
            print("<----------------------------------->")
            opc4=input("Ingrese opcion de filtro: ")
            os.system("cls")
        #->
    elif opc == "3":#Grafica
        print("opcion 3")
    else:
        print("opcion invalida ")
    print("<--------------------------------->")
    print("<             MENU                >")
    print("1. Gestionar peliculas")
    print("2. Filtrado")
    print("3. Graficar")
    print("4. salir")
    print("<--------------------------------->")
    opc = input("Ingrese opcion: ")
    os.system("cls")
    if opc == "4":
        print("<--------------------------------->")
        print("<               :)                >")
        print("<--------------------------------->")




