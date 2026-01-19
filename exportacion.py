import procesos as func
def resultados_csv(diccionarios):
    dicx = func.orden_alfabetico(diccionarios)
    totales, dicc_palabras, dicc_letras, dicc_signos, dicc_numeros = dicx
    
    # Realizando el archivo "full_resultados(orden_alfabetico).csv"
    with open("ResultadosCsv\\full_resultados(orden_alfabetico).csv","w",encoding="utf-8-sig") as resultados:
        
        resultados.write("Tipo de dato,Conteo\n")
        for key in totales:
            resultados.writelines(f"{key},{totales[key]}\n")
        resultados.write("\n")
        
        resultados.write("Palabra,Conteo\n")
        for key in dicc_palabras:
            resultados.writelines(f"{key},{dicc_palabras[key]}\n")
        resultados.write("\n")
        
        resultados.write("Letra,Conteo\n")
        for key in dicc_letras:
            resultados.writelines(f"{key},{dicc_letras[key]}\n")
        resultados.write("\n")
        
        resultados.write("Signo,Conteo\n")
        for key in dicc_signos:
            resultados.writelines(f'" {key} ",{dicc_signos[key]}\n')
        resultados.write("\n")
        
        resultados.write("Número,Conteo\n")
        for key in dicc_numeros:
            resultados.writelines(f"{key},{dicc_numeros[key]}\n")
        
    
    # Reordendando los diccionarios para la creación de los csv.    
    dicx = func.orden_decreciente(diccionarios)    
    totales, dicc_palabras, dicc_letras, dicc_signos, dicc_numeros = dicx
        
    with open("ResultadosCsv\\Resumen.csv","w",encoding="utf-8-sig") as resultados:
        resultados.write("Tipo de dato,Conteo\n")
        for key in totales:
            resultados.writelines(f"{key},{totales[key]}\n")
        resultados.write("\n")
    
    with open("ResultadosCsv\\Palabras_top_100.csv","w",encoding="utf-8-sig") as resultados:
        resultados.write("Palabra,Conteo\n")
        contador = 0
        for item in dicc_palabras.items():
            if contador == 100:
                break
            contador += 1
            resultados.writelines(f"{item[0]},{item[1]}\n")
    
    with open("ResultadosCsv\\Letras.csv","w",encoding="utf-8-sig") as resultados:
        resultados.write("Letra,Conteo\n")
        for key in dicc_letras:
            resultados.writelines(f"{key},{dicc_letras[key]}\n")

    with open("ResultadosCsv\\Signos.csv","w",encoding="utf-8-sig") as resultados: 
        resultados.write("Signo,Conteo\n")
        for key in dicc_signos:
            resultados.writelines(f'" {key} ",{dicc_signos[key]}\n')

    with open("ResultadosCsv\\Números.csv","w",encoding="utf-8-sig") as resultados:         
        resultados.write("Número,Conteo\n")
        for key in dicc_numeros:
            resultados.writelines(f"{key},{dicc_numeros[key]}\n")
        
# Los 5 archivos en orden decreciente y palabras y letras top 50

#El archivo con full_resultado en orden alfabetico