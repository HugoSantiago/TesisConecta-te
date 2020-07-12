import csv

with open('studentInfoPOS.csv', 'r') as inp, open ('studentInfoPOS2.csv','w') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out, delimiter=',')
    writer.writerow(next(reader))

    for row in reader:
        lista = []
        lista.append(row[0])
        lista.append(row[1])
        lista.append(row[2])
        lista.append(row[3])
        lista.append(row[4])
        lista.append(row[5])
        lista.append(row[6])
        lista.append(row[7])
        lista.append(row[8])
        lista.append(row[9])
        lista.append(row[10])
        lista.append(row[11])
        value = ""
        if row[12] == "Withdrawn" or row[12] == "Distinction":
            value = "Fail"
            lista.append(value)
        else:
            lista.append(row[12])
        writer.writerow(lista)

