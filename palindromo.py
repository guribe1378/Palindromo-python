"""
Palíndromo
es una palabra que se lee igual en un sentido que en otro
se utiliza una lista y sus propiedades extend y reverse
"""
def palindromo(palabra):
    palabra=input("Igresa una palabra: ")
    lista=[]
    lista.extend(palabra)
    lista.reverse()
    strpalabra=''.join(lista)
    if palabra==strpalabra:
        print("La palabra " + "'" + palabra +"'"+  " es palíndromo")
    else:
        print("La palabra " + "'" + palabra +"'"+ " no es palíndromo")

    
palindromo("palabra") 