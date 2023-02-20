txt = "Lorem ipsum dolor dolor sit amet, consectetur adipisicing elit. Iusto corporis odio itaque quisquam adipisci tempora praesentium beatae laboriosam dolores soluta? Voluptate sit eaque accusamus aliquid quia culpa illum ipsum assumenda?".lower()
arr =txt.split(" ")
arr.sort()
unicos=[]
veces=[]
contador = 1
arr.append(" ")
for i in range(len(arr)-1):
    if arr[i+1] == arr[i] :
        contador=contador+1   
    else:
        unicos.append(arr[i])
        veces.append(contador)
        contador = 1
for x in range(len(unicos)):
    print(unicos[x],"->",veces[x])




