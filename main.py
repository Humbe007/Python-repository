### 🟢 Proyecto — Contador de palabras avanzado
"""
De un libro se obtiene el siguiente resultado:

Crear los siguientes archivos.csv: 
    1-
Tipo de dato, Conteo
Palabra     ,  152
Numeros     ,   8
etc

    2-
Palabra , Conteo
Capitulo,  102
kill    ,  85
jupiter ,  78
etc

    3- :
Letra, Conteo
a    ,   10
b    ,   4
c    ,   7
etc

    4-
Signo , Conteo
.     ,   7
,     ,   5
¿     ,   3
etc
    5-
Número , Conteo
1      ,   5
6      ,   9
2      ,    5
etc

6- Que contenga los 5 anteriores
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
