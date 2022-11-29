def downloadFromURL(url, filename, sep=',', delim='\n', encoding='utf-8', mainpath = 'C:/Users/Alderete/Desktop/'):
    
    #para que funcione correctamente tenemos que instalar 
    #pip install openpyxl(para poder crear excel)
    #pip install xlwt(Para poder crear .json)

    import urllib3
    import pandas as pd 


    medals_url = url 
    http = urllib3.PoolManager()
    r = http.request('GET', medals_url)
    r_status = r.status
    recuest = r.data

    #Elobjeto response contiene un string binario, 
    #sasi que lo convertimos a un string descodificandolo en UTF-8
    str_data = recuest.decode(encoding)

    #Dividimos el string en una lista con cada fila de strings
    lines = str_data.split(delim)

    #Extraemos la primera linea que es la que tiene la cabecera
    col_names = lines[0].split(sep)
    n_col = len(col_names)

    #Creo un directorio vacio donde ira la informacion procesada desde la url externa
    counter = 0 
    main_dict = {}
    for col in col_names:
        main_dict[col] = []

    #Procesamos fila a fila la informacion para ir rellenando el diccionario con los datos
    for line in lines:
        #nos saltamos la primera linea que es la cabecera
        if (counter > 0):
            #Dividimos cada linea por una coma comoelemento separador 
            values = line.strip().split(sep)
            #añadimos cada valor a su columna en el diccionario
            for i in range(n_col):
                main_dict[col_names[i]].append(values[i])
        counter += 1
    print('El dataset tiene {} columnas y {} filas'.format(n_col, counter))

    #Convertimos el diccionario procesado a Data Frame y comprobamos que los datos son correctos
    df = pd.DataFrame(main_dict)
    print(df.head())

    #Elegimos el nombre de el archivo que vamos a guardar y la ruta
    
    #filename = 'Medallas.'
    fullpath = mainpath + filename

    #lo guardamos en csv, xlsx y json
    df.to_csv(fullpath+'.csv')
    df.to_excel(fullpath+'.xlsx')
    df.to_json(fullpath+'.json')

    return df
