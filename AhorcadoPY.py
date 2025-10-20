import random
import os

def titulo():
    print("""
        ▓▓▓▓▓▓░  ▓▓░ ▓▓░  ▓▓▓▓▓▓░  ▓▓▓▓▓▓░  ▓▓▓▓▓▓░  ▓▓▓▓▓▓░  ▓▓▓▓░       ▓▓▓▓░   ▓▓▓▓░   ▓▓░   ▓▓░ 
        ▓▓░ ▓▓░  ▓▓░ ▓▓░  ▓▓░  ▓▓░ ▓▓░ ▓▓░  ▓▓░      ▓▓░ ▓▓░  ▓▓░  ▓▓░  ▓▓░  ▓▓░  ▓▓░ ▓▓░  ▓▓░ ▓▓░  
        ▓▓▓▓▓▓░  ▓▓▓▓▓▓░  ▓▓░  ▓▓░ ▓▓▓▓░    ▓▓░      ▓▓▓▓▓▓░  ▓▓░  ▓▓░  ▓▓░  ▓▓░  ▓▓▓▓░      ▓▓░   
        ▓▓░ ▓▓░  ▓▓░ ▓▓░  ▓▓▓▓▓▓░  ▓▓░ ▓▓░  ▓▓▓▓▓▓░  ▓▓  ▓▓░  ▓▓▓▓░       ▓▓▓▓░   ▓▓░        ▓▓░    by JavierMGB
    """)

def dibujar_persona(intentos):
    estado_persona = [  
        """
            ______
           |      |
           |      O
           |     \|/
           |      |
           |     / \ 
        __/|\_______________
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        """,
        """
            ______
           |      |
           |      O
           |     \|/
           |      |
           |     /
        __/|\_______________
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        """,
        """
            ______
           |      |
           |      O
           |     \|/
           |      |
           |
        __/|\_______________
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        """,
        """
            ______
           |      |
           |      O
           |     \|
           |      |
           |
        __/|\_______________
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        """,
        """
            ______
           |      |
           |      O
           |      |
           |      |
           |
        __/|\_______________
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        """,
        """
            ______
           |      |
           |      O
           |
           |
           |
        __/|\_______________
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        """,
        """
            ______
           |      |
           |
           |
           |
           |
        __/|\_______________
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        """
    ]

    return estado_persona[intentos]

def limpiar_pantalla():
    os.system("cls")

def obtener_palabra():
    palabras = [  "casa", "perro", 
                  "mesa", "escuela", 
                  "sol", "árbol", 
                  "comida", "agua", 
                  "libro", "ventana", 
                  "amigo", "coche", 
                  "puerta", "reloj", 
                  "ciudad", "flor", 
                  "playa", "montaña", 
                  "familia", "trabajo"]
    
    return random.choice(palabras).upper()

palabra = obtener_palabra()
huecos = "_" * len(palabra)
acertado = False
letras_acertadas = []
palabras_acertadas = []
intentos = 6

print("\033[1;37m¡Juguemos al Ahorcado!")


while not acertado and intentos > 0:
    titulo()
    print(dibujar_persona(intentos))
    print(huecos)
    print("\n")

    adivinanza = input("Por favor, adivina una letra o palabra: ").upper().strip()

    
    if not adivinanza.isalpha():
        print("No es una adivinanza válida.")
        continue

    if len(adivinanza) == 1:

        if adivinanza in letras_acertadas:
            print("Ya adivinaste la letra", adivinanza)

        elif adivinanza not in palabra:
            print(adivinanza, "no está en la palabra.")
            intentos -= 1
            letras_acertadas.append(adivinanza)
        else:
            print("¡Bien hecho,", adivinanza, "está en la palabra!")
            letras_acertadas.append(adivinanza)
            word_as_list = list(huecos)
            indices = [i for i, letter in enumerate(palabra) if letter == adivinanza]

            for index in indices:
                word_as_list[index] = adivinanza
            huecos = "".join(word_as_list)

            if "_" not in huecos:
                acertado = True

   
    elif len(adivinanza) == len(palabra):

        if adivinanza in palabras_acertadas:
            print("Ya adivinaste la palabra", adivinanza)

        elif adivinanza != palabra:
            print(adivinanza, "no es la palabra.")
            intentos -= 1
            palabras_acertadas.append(adivinanza)

        else:
            acertado = True
            huecos = palabra

    else:
        print("No es una adivinanza válida.")

    limpiar_pantalla()


print(dibujar_persona(intentos))
print(huecos)

if acertado:
    print("¡Felicidades, adivinaste la palabra!")

else:
    print("Lo siento, te quedaste sin intentos. La palabra era " + palabra)

    
