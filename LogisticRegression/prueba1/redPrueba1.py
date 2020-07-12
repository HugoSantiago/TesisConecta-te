import numpy as np
import tensorflow as tf
import tflearn
import pandas as pd
from sklearn.model_selection import train_test_split

#----- Preparacion de los sets de datos
df = pd.read_csv("Documentsporcentajes.csv")
lstx = df[df.columns[:-6]].as_matrix()
lsty = df[df.columns[-1]].as_matrix()
x_train , x_test, y_train, y_test = train_test_split(lstx, lsty)
#----- Parametros de la red
inputs = 22
layer1 = 15
layer2 = 15
classes = 2
#----- Crear el modelo
def crear_modelo():
    tf.reset_default_graph()
    net = tflearn.input_data([None, inputs])
    net = tflearn.fully_connected(net, layer1, activation='ReLU')
    net = tflearn.fully_connected(net, layer2, activation='ReLU')
    net = tflearn.fully_connected(net, classes, activation='softmax')
    net = tflearn.regression(net, optimizer='sgd', learning_rate=0.01, loss='categorical_crossentropy')
    modelo = tflearn.DNN(net)
    return modelo 
#----- Creacion 
modelo = crear_modelo()
modelo.fit(x_train, y_train, validation_set= 0.1, show_metric= True, batch_size=500, n_epoch=100)
#----- Predicciones
predicciones = np.array(modelo.predict(x_test).argmax(axis=1))
correctas = y_test.argmax(axis=1)
certeza = np.mean(predicciones == correctas, axis=0)
print("La certeza es de: ", certeza)
