def ImprimeAnimalAscii(opcion):
    delfin = '''
                                                                   .--.
                                    _______             .-"  .'
                            .---u"""       """"---._  ."    %
                        .'                        "--.    %
                    __.--'  o                          "".. "
                    (____.                                  ":
                    `----.__                                 ".
                            `----------__                     ".
                                ".   . ""--.                 ".
                                    ". ". bIt ""-.              ".
                                    "-.)        ""-.           ".
                                                    "".         ".
                                                        "".       ".
                                                            "".      ".
                                                                "".    ".
                                        ^~^~^~^~^~^~^~^~^~^~^~^~^"".  "^~^~^~^~^
                                                                ^~^~^~^  ~^~
                                                                    ^~^~^~
          
    
    
    '''
    perro = '''
           __
      (___()'`;
      /,    /`
      \\"--\\
    
    
    '''
    elefante = '''
                        ____
                   .---'-    \
      .-----------/           \
     /           (         ^  |   __
&   (             \        O  /  / .'
'._/(              '-'  (.   (_.' /
     \                    \     ./
      |    |       |    |/ '._.'
       )   @).____\|  @ |
   .  /    /       (    | mrf
  \|, '_:::\  . ..  '_:::\ ..\). 
    
    '''

    if (opcion == 1):
        return delfin
    elif (opcion == 2):
        return perro
    elif (opcion == 3):
        return elefante        
    elif (opcion == 4):
        return "Gracias por tu visita"
    else: 
        return "Opcion invalida, elige un numero del menu"


while True:
    print("1. Delfin")
    print("2. Perro")
    print("3. Elefante")
    print("4. Salir del programa")
    opcion = int(input("Escoge el numero de tu opcion: "))    
    respuesta = ImprimeAnimalAscii(opcion)
    print(respuesta)
    if (opcion == 4):
        break