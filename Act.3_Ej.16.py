print("Ejercicio 16: Cambios en tu playlist")
print("Fátima Isabella Pagno Castillo")
print("07276005")

#La playlist inicial
playlist = ["Flowers", "Calm Down", "Ella Baila Sola", "Anti-Hero", "Titi Me Preguntó"]

#Mostramos la playlist numerada
print("==== MI PLAYLIST ====")
for i in range(len(playlist)):
    print(i + 1, ".", playlist[i])
    
numero = int(input("¿Qué número de canción quieres cambiar? "))

#Validamos que el número existe
if numero < 1:
    print("Ese número no existe")
elif numero > len(playlist):
    print("Ese número no existe")
else:
    #Casillero = número - 1
    casillero = numero - 1
    actual = playlist[casillero]
    print("Vas a cambiar:", actual)
    
    #Pedimos la nueva canción: mientras esté vacía, se repite
    nueva = input("Escribe la nueva canción: ")
    while nueva == "":
        print("No puede estar vacía")
        nueva = input("Escribe la nueva canción: ")
        
    #¿La nueva canción YA ESTÁ en la playlist?
    if nueva in playlist:
        print("|", nueva, "ya está en tu playlist")
    else:
        #Reemplazamos lo que hay en ese casillero
        playlist[casillero] = nueva
        print("|", actual, "cambió por", nueva)
        
    #¿Quiere mover esta canción al primer lugar?
    mover = input("¿La quieres mover al primer lugar? (s/n): ")
    if mover == "s":
        #Intercambiamos el casillero 0 con el casillero elegido
        playlist[0], playlist[casillero] = playlist[casillero], playlist[0]
        print("Ahora está en el primer lugar")
        
#Mostramos la playlist final
print("==== PLAYLIST FINAL ====")
for i in range(len(playlist)):
    print(i + 1, ".", playlist[i])