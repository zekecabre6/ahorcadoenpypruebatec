""" 
En este punto se pide implementar una versión del conocido juego Ahorcado. El programa debe cumplir los siguientes puntos:

Primero pide a un jugador la palabra a adivinar por input.
Después toma las letras que elige el otro jugador por input también.
El jugador tiene 5 vidas, si las pierde todas, pierde.
Se tiene que ir mostrando el avance del juego, mostrando las letras ya probadas y como se va completando la palabra a adivinar
Por ejemplo:

letras usadas: a,o,p
estado de la palabra a adivinar: _o_a """



def jugar_ahorcado():
    palabra_a_adivinar= input("Ingrese la palabra a adivinar! ").lower()
    letras_usadas = []
    vidas = 5
    
    while vidas >0:
        letra = input("Ingrese una letra: ").lower()
        
        if letras_usadas.count(letra) > 0:
            print("Ya usaste esa letra, proba con otra! ")
        else:
            letras_usadas.append(letra)
            if letra in palabra_a_adivinar:
                print("correcto! la letra esta dentro de la palabra")
            else:
                vidas -= 1
                print("Incorrecto, perdes una vida")
                
                
            estado_palabra = ""
            for letra_palabra in palabra_a_adivinar:
                if letra_palabra in letras_usadas:
                    estado_palabra += letra_palabra + " "
                else: 
                    estado_palabra += "_" + " "
                    
        print("Letras usadas: ", ", ".join(letras_usadas))
        print("Estado de la palabra a adivinar: ", estado_palabra)
        print("Vidas restantes", vidas)
        if all(letra_palabra in letras_usadas for letra_palabra in palabra_a_adivinar):
            print("Felicidades Ganaste el juego!!!!!!, la palabra es: ", palabra_a_adivinar)
            return
    print("perdiste. la palabra completa era: ", palabra_a_adivinar)
    
jugar_ahorcado()