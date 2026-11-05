print("Ejercicio 8: Revisa tu gamertag")
print("Fátima Isabella Pagno Castillo")
print("07276005")

#Pedimos el gamertag
gamertag = input("Escribe tu gamertag: ")

#Contadores: empiezan en 0
vocales = 0
numeros = 0
caracteres = 0

#"Para cada" letra del gamertag...
for letra in gamertag:
    print("|", letra)
    
    #Contamos este caracter
    caracteres = caracteres + 1
    
    #¿La letra ESTÁ en el grupo de vocales?
    if letra in "aeiouAEIOU":
        vocales = vocales + 1
        
    #¿La letra ESTÁ en el grupo de números?
    if letra in "0123456780":
        numeros = numeros + 1
        
#Ya revisamos todas las letras: mostramos el resumen
print("==== RESUMEN ====")
print("Caracteres:", caracteres)
print("Vocales:", vocales)
print("Números:", numeros)

#¿No tiene ningún número?
if numeros == 0:
    print("Consejo: agrégale un número para que sea único")
else:
    print("¡Buen gamertag!")