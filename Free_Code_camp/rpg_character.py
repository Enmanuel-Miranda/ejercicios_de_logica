full_dot = '●'
empty_dot = '○'

def create_character(name, fuerza, inteligencia, carisma):

    # Validamos el nombre
    if not isinstance(name, str):
        return ("The character name should be a string")

    elif name == "":
        return ("The character should have a name")

    elif len(name) > 10:
        return ( "The character name is too long")

    elif " " in name:
        return("The character name should not contain spaces")

    valores = [fuerza, inteligencia, carisma]
    text = ['STR','INT','CHA']
    dots_list = []

    # Validamos lso stats
    for i in valores:

        if type(i) != int:
            return "All stats should be integers"
  
        if i <= 0:
            return "All stats should be no less than 1"
            
        elif i > 4:
            return "All stats should be no more than 4"
            
        elif sum(valores) < 6:
            return "The character should start with 7 points"
            

    for i in valores:
        d_full = full_dot * i
        d_empty = empty_dot * (10 - i)
        dots = d_full + d_empty
        dots_list.append(dots)

    valores = list(zip(text, dots_list))

    lista_puntos  =[f"{nombre} {punto}" for nombre,punto in valores]
    
    cadena = name + "\n" + "\n".join(lista_puntos)

    return cadena





personaje = create_character("len", 3, 2, 2)
print(personaje)