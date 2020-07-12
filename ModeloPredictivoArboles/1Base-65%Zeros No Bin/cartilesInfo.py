import csv
import pandas as pd

df = pd.read_csv("datos2013b.csv")
colSum2013b = []
for x in df.keys():
    colSum2013b.append(df[x].sum())

df = pd.read_csv("datos2013j.csv")
colSum2013j = []
for x in df.keys():
    colSum2013b.append(df[x].sum())
    
df = pd.read_csv("datos2014b.csv")
colSum2014b = []
for x in df.keys():
    colSum2013b.append(df[x].sum())

df = pd.read_csv("datos2014j.csv")
colSum2014j = []
for x in df.keys():
    colSum2013b.append(df[x].sum())

lineas = df.keys()

listaA = ['urlC', 'forumngC', 'homepageC','outcontentC','subpageC', 'resourceC','sharedsubpageC', 'pageC', 
'questionaarieC', 'ouwikiC','htmlactivityC', 'ouelluminateC','dataplusC', 'externalquizC','repeatactivityC', 'dualpanelC','quizC','glossaryC',
'oucollaborateC','folderC','acumnegC', 'acumgC']

lineas = list(lineas) + listaA

with open('datos2013b.csv', 'r') as inp, open ('datos2013bProcesados.csv','w') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out, delimiter=',')
    next(reader)
    writer.writerow(lineas)
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
        
