import csv 

with open('pogresoPOS2.csv', 'r') as inp, open ('pogresoPOS3PorcentajeCatego5.csv','w') as out:
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
                    b = round((aa/total), 3)
                    res = ""
                    if b == 0:
                        res = "No hay participacion"
                    if b > 0 and b <= 0.2:
                        res = "Participacion baja"
                    if b > 0.2 and b <= 0.4:
                        res = "Participacion Media-baja"
                    if b > 0.4 and b <= 0.6:
                        res = "Participacion Media"
                    if b > 0.6 and b <= 0.8:
                        res = "Participacion Alta"
                    if b > 0.8 and b <= 1:
                        res = "Participacion Muy alta"
#                    if b < 0.05:
#                        res = "0 - 5"
#                    if b >= 0.05 and b < 0.1:
#                        res = "5 - 10"
#                    if b >= 0.1 and b < 0.15:
#                        res = "10 - 15"
#                    if b >= 0.15 and b < 0.2:
#                        res = "15 - 20"
#                    if b >= 0.2 and b < 0.25:
#                        res = "20 - 25"
#                    if b >= 0.25 and b < 0.3:
#                        res = "25 - 30"
#                    if b >= 0.3 and b < 0.35:
#                        res = "30 - 35"
#                    if b >= 0.35 and b < 0.4:
#                        res = "35 - 40"
#                    if b >= 0.4 and b < 0.45:
#                        res = "40 - 45"
#                    if b >= 0.45 and b < 0.5:
#                        res = "45 - 50"
#                    if b >= 0.5 and b < 0.55:
#                        res = "50 - 55"
#                    if b >= 0.55 and b < 0.6:
#                        res = "55 - 60"
#                    if b >= 0.6 and b < 0.65:
#                        res = "60 - 65"
#                    if b >= 0.65 and b < 0.7:
#                        res = "65 - 70"
#                    if b >= 0.7 and b < 0.75:
#                        res = "70 - 75"
#                    if b >= 0.75 and b < 0.8:
#                        res = "75 - 80"
#                    if b >= 0.8 and b < 0.85:
#                        res = "80 - 85"
#                    if b >= 0.85 and b < 0.9:
#                        res = "85 - 9"
#                    if b >= 0.9 and b < 0.95:
#                        res = "9 - 95"
#                    if b >= 0.95 and b <= 1:
#                        res = "95 - 100"
                    lista.append(res)
                except:
                    lista.append(a)
            writer.writerow(lista)

