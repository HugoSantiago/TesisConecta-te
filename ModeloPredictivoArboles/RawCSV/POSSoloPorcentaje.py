import csv 

with open('pogresoPOS2.csv', 'r') as inp, open ('pogresoPOS3PorcentajeSoloporcentaje.csv','w') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out, delimiter=',')

    writer.writerow(next(reader))
    
    for row in reader:
        
        if row[0] is "":
            continue
        else:
            lista = []
            total = float(row[24]) + float(row[25])
            for a in row:
                try:
                    aa = float(a)
                    b = (aa/total)
                    res = str(b)
                    lista.append(res)
                except:
                    lista.append(a)
            writer.writerow(lista)

