#lista desordeb
listamal = [2,1,3,4,5,3,9]

#definir tamañp 
longitud = len(listamal)
for i in range(longitud):
   # print ("Esto es i",i)prueba de que hace

    for j in range(longitud-1):
        #print("Esto es j",j) prueba de que se mueve
        #Comparacion 
        if listamal[j] > listamal[j+1]:
            #intercambio, con asignacion simultanea a, b = b, a
            listamal[j], listamal[j+1] = listamal[j+1], listamal[j]
            


print(listamal)
