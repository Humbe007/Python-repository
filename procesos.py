def es_numero(char):
    if char.isnumeric():
        return True
    else:
        return False

def es_letra(char):
    if char.isalpha():
        return True
    else:
        return False
        
def es_signo(char):
    if not char.isnumeric() and not char.isalpha():
        return True
    else:
        return False

def sacar_palabras(string):
    """
    Esta función saca 'palabras' de una cadena de texto, ignorando signos y números.
    
    Ejemplo: si string = "\str,345.in3g" (Como pueden ver hay tres cadenas: "str","in" y "g" pero con otros signos y numeros de por medio)
    Lo que devolveria para ese string seria la siguiente lista: ["str","in","g"]
    """
    
    palabras = []
    string = list(string)
    pasos = 0
    for i in range(len(string)):
        
        if pasos > 0 :
            pasos -= 1
            continue

        elif es_signo(string[i]):
            continue
        elif es_numero(string[i]):
            continue
        elif es_letra(string[i]):    
            palabra = string[i]
            indi = i 

            while True:
                indi += 1
                if indi >= len(string) or not es_letra(string[indi]): #Para el indice len(string), la cadena de texto ya se habra acabado, por ejemplo para hola, el indice 4 no tendra nada, por eso ahi rompe el while
                    palabras += [palabra]
                    break
                elif es_letra(string[indi]):
                    pasos += 1
                    palabra += string[indi]
                    continue
                else:
                    break
    return palabras

def sacar_numeros(string):
    string = list(string)
    numeros = []
    pasos = 0
    for i in range(len(string)): #Añadiendo números ('92' se agrega como '92', no como '9,2')
        if pasos > 0:
            pasos -= 1
            continue
        
        elif es_letra(string[i]):
            continue
        elif es_signo(string[i]):
            continue
        elif es_numero(string[i]):
            numero = string[i]
            indi = i
            while True:
                indi += 1
                if indi >= len(string) or not es_numero(string[indi]):
                    numeros += [int(numero)]
                    break
                elif es_numero(string[indi]):
                    pasos += 1
                    numero += string[indi] 
                    continue
                else:
                    break
            
    return numeros

def crear_diccionarios(libro):
     # Declarando diccionarios:    
    dicc_palabras = {} 
    dicc_letras = {}
    dicc_signos = {} 
    dicc_numeros = {}
    
    for linea in libro:
        
        linea = linea.lower()
        linea = linea.strip()
        linea = linea.split()
        
        for palabra in linea:
            palabra_ = sacar_palabras(palabra)
            for palabras in palabra_:
                dicc_palabras[palabras] = 0
    
            for num in sacar_numeros(palabra):
                dicc_numeros[num] = 0
            
            for char in palabra:
                if es_letra(char):
                    dicc_letras[char] = 0
               
                elif es_signo(char):
                    dicc_signos[char] = 0
                    
    return [dicc_palabras, dicc_letras, dicc_signos, dicc_numeros]

def cantidades_lineas_palabras_letras_signos_numeros(libro,diccionarios):

    dicc_palabras, dicc_letras, dicc_signos, dicc_numeros = diccionarios
    totales = {
    "Total Palabras" : 0,
    "Total Letras" : 0,
    "Total Líneas" : 0,
    "Total Números" : 0,
    "Total Signos" : 0,
    }

    for linea in libro: 
        totales["Total Líneas"] += 1
        
        linea = linea.lower()
        linea = linea.strip()
        linea = linea.split()

        for palabra in linea:
            
            for palabras in sacar_palabras(palabra): # Añadiendo palabras
                dicc_palabras[palabras] += 1
                totales["Total Palabras"] += 1
            
            for numeros in sacar_numeros(palabra):
                dicc_numeros[numeros] += 1 
                totales["Total Números"] += 1
            
            for char in palabra:
                if es_letra(char):
                    dicc_letras[char] += 1
                    totales["Total Letras"] += 1
                elif es_signo(char):
                    dicc_signos[char] += 1
                    totales["Total Signos"] += 1
    diccionarios = totales, dicc_palabras, dicc_letras, dicc_signos, dicc_numeros
    return diccionarios


def orden_decreciente(diccionarios):
    dicxis = []
    for diccionario in range(0,len(diccionarios)):
        diccionario_seleccionado = diccionarios[diccionario]
        dicxi_temporal = {}
        for item in sorted(diccionario_seleccionado.items(), key=lambda x : x[1],reverse= True):
            dicxi_temporal[item[0]] = item[1]
        dicxis.append(dicxi_temporal)
        
    totales = dicxis[0]
    dicc_palabras = dicxis[1]
    dicc_letras = dicxis[2]
    dicc_signos = dicxis[3]
    dicc_numeros = dicxis[4]
    diccionarios = [totales, dicc_palabras, dicc_letras, dicc_signos, dicc_numeros]
    return diccionarios

def orden_alfabetico(diccionarios):
    dicxis = []
    for diccionario in range(0,len(diccionarios)):
        diccionario_seleccionado = diccionarios[diccionario]
        dicxi_temporal = {}
        for item in sorted(diccionario_seleccionado.items(), key=lambda x : x[0]):
            dicxi_temporal[item[0]] = item[1]
        dicxis.append(dicxi_temporal)
        
    totales = dicxis[0]
    dicc_palabras = dicxis[1]
    dicc_letras = dicxis[2]
    dicc_signos = dicxis[3]
    dicc_numeros = dicxis[4]
    diccionarios = [totales, dicc_palabras, dicc_letras, dicc_signos, dicc_numeros]
    return diccionarios
