# para que dê certo a rede neural instale o tensorFlow com o comando abaixo
# pip install tensorflow keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential([Dense(4, input_dim=2, activation='relu'), Dense(1, activation='sigmoid')])
model.compile(optimizer='adam', loss='binary_crossentropy')
