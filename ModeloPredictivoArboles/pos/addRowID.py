import csv

with open ('pogresoPOS3PorcentajeCatego5.csv') as inp, open('pogresoPOS3PorcentajeCatego5Version5.csv', 'w') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out, delimiter=',')
    writer.writerow(['ID'] + next(reader))
    writer.writerows([i] + row for i, row in enumerate(reader, 1))
