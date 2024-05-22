import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    
    while True:
        guess = int(input("Adivina el número (entre 1 y 20): "))
        
        if guess == secret_number:
            print("¡Felicidades! ¡Has adivinado el número!")
            break
        print("Demasiado bajo." if guess < secret_number else "Demasiado alto.")

guess_the_number()
