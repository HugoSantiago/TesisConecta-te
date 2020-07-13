import csv

with open('studentVlePOS.csv', 'r') as inp, open ('studentVlePOS2.csv','w') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out, delimiter=',')

    #Id del estudiante
    idStudent = ''
    #id del recurso
    idSide = ''
    #Suma de clicks acumulada de los dias positivos 
    acumG = 0
    #Suma de clicks acumulada de los dias negativos
    acumN = 0
    #Header para el output
    writer.writerow(['ID', 'code_module','code_presentation','id_student','id_site','acumG','acumN'])
    #Saltar el header
    next(reader)
    #contador just for fun
    i = 0

    for row in reader:
        idStudent = row[3]
        idSide = row[4]
        acumG = 0
        acumN = 0 
        with open('studentVlePOS.csv') as inp2:
            reader2 = csv.reader(inp2)
            next(reader2)
            for row2 in reader2:
                #Son el mismo estudiante interactando con el mismo recurso y la fecha es positiva
                if ( idStudent == row2[3] and idSide == row2[4] and int(row2[5]) >= 0 ):
                    acumG += int(row2[6])
                #Son el mismo estudiante interactando con el mismo recurso y la fecha es negativa
                if ( idStudent == row2[3] and idSide == row2[4] and int(row2[5]) < 0 ):
                    acumN += int(row2[6])
        i += 1
        print(i)
        writer.writerow([row[0], row[1], row[2], idStudent, idSide, acumG, acumN])   

            


    
