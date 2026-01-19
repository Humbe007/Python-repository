### 🟢 Proyecto — Contador de palabras avanzado
"""
**Objetivo:** análisis de texto avanzado.

**Enunciado**
De un libro tienes que obtener el siguiente resultado:

Crear 1 archivo csv con los siguientes 3 conjuntos de datos: 

    1- Con:
Tipo de dato, Conteo
Palabra, 152
Numeros, 8
etc
    2- Con:
Palabra, Conteo
Capitulo, 4
etc
    3- Con:
Letra/Signo/Número, Conteo

""" 
#Reglas:
"""
* No usar librerias externas
"""
import procesos as func
import exportacion as expo
with open("Libro\\libro.txt", encoding= "UTF-8") as _libro_:
    
    # Leyendo el libro (conviertiendolo a str):
    libro = _libro_.readlines()
    
    diccionarios = func.crear_diccionarios(libro)
    
    diccionarios = func.cantidades_lineas_palabras_letras_signos_numeros(libro,diccionarios)    

    datos_orden_alfabetico = func.orden_alfabetico(diccionarios) #Aqui se guardan en orden alfabetico (Solo para demostrar que se pueden guardar)    

    datos_conteo_decreciente = func.orden_decreciente(diccionarios) #Aqui se guardan en orden de conteo decreciente  (Solo para demostrar que se pueden guardar) 
    
    expo.resultados_csv(diccionarios)
   
#  Aqui "diccionarios = func.orden_decreciente(diccionarios)" y aqui "diccionarios = func.orden_alfabetico(diccionarios)"
# La variable diccionarios contiene una lista con 5 diccionarios:

# diccionario[0] = totales (Primer tabla en los csv)

# diccionario[1] = conteo_de_palabras (Segunda tabla en los csv)

# diccionario[2] = conteo_de_letras (Tercera tabla en los csv)

# diccionario[3] = conteo_de_signos (Cuarta tabla en los csv)

# diccionario[4] = conteo_de_numeros (Quinta tabla en los csv)