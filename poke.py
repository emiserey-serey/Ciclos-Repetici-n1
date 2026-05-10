#mayor que >, menor que <
import os, random
os.system("cls")
cantidad_combates = 0
contador_victoria = 0
contador_derrota = 0
pokemon_agua = 0
pokemon_fuego = 0
pokemon_planta = 0
try:
    while cantidad_combates <=0: 
        cantidad_combates = int(input("ingrese cantidad de combates\n"))
        if cantidad_combates <=0:
            print("Ingrese número mayor a 0")
    for x in range (cantidad_combates):
        nombre_entrenador = ""
        tipo_pokemon = ""
        while len (nombre_entrenador) <3:
            nombre_entrenador = input("ingrese nombre de entrenador\n")
            if len (nombre_entrenador) <3:
                print("debe tener mas de 3 caracteres")
        while len (tipo_pokemon) <= 0 or (tipo_pokemon != 'F' and tipo_pokemon != 'A' and tipo_pokemon != 'P'):
            tipo_pokemon = input("ingrese tipo de pokemon\n").upper()
            if len(tipo_pokemon) <=0:
                print("debes ingresar un carácter")
            elif tipo_pokemon != 'P' and tipo_pokemon != 'A' and tipo_pokemon != 'F':
                print("sólo existen los pokemones: A, F, P")
            else:
                break
        poder_aleatorio = random.randint(1, 20)
        #obtener bonificaciones
        if tipo_pokemon == 'F':
            bonificacion = 3
            pokemon_fuego = pokemon_fuego + 1
        elif tipo_pokemon == 'A':
            bonificacion = 2
            pokemon_agua = pokemon_agua + 1
        else:
            bonificacion = 1
            pokemon_planta = pokemon_planta +1
        
        poder_total = poder_aleatorio + bonificacion
        if poder_total >= 18:
            batalla = "Victoria"
            contador_victoria = contador_victoria + 1
        elif poder_total >= 10 and poder_total <18:
            batalla = "Batalla difícil" 
        else:
            batalla = "Derrota" 
            contador_derrota = contador_derrota + 1
    print(f"Cantidad de batallas: {cantidad_combates}")
    print(f"Cantidad de wins: {contador_victoria}")
    print(f"Cantidad de loses: {contador_derrota}")
    print(f"Tipo de pokemon fuego: {pokemon_fuego}")
    print(f"Tipo de pokemon agua: {pokemon_agua}")
    print(f"Tipo de pokemon planta: {pokemon_planta}")
except:
    print("valor debe ser numerico")