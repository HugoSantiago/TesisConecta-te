import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

reg = linear_model.LogisticRegression()

df = pd.read_csv("Documentsporcentajes.csv")

lstx = df[df.columns[:-6]].as_matrix()
lsty = df[df.columns[-1]].as_matrix()

x_train , x_test, y_train, y_test = train_test_split(lstx, lsty)

reg.fit(x_train, y_train)

print (reg.score(x_test,y_test))
