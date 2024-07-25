import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import matplotlib.pyplot as plt

def generate_data(num_samples):
    x = np.linspace(-10, 10, num_samples)
    y = 2 * x + 5
    return x, y

x_train, y_train = generate_data(100)
x_test, y_test = generate_data(20)

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

model = Sequential()
model.add(Dense(64, input_dim=x_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(optimizer=SGD(learning_rate=0.01), loss='mean_squared_error')

history = model.fit(x_train, y_train, epochs=100, validation_split=0.2, verbose=1)

loss = model.evaluate(x_test, y_test, verbose=1)
print(f'Model loss on test data: {loss}')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

y_pred = model.predict(x_test)
plt.subplot(1, 2, 2)
plt.scatter(x_test, y_test, color='blue', label='True Values')
plt.scatter(x_test, y_pred, color='red', label='Predicted Values')
plt.plot(x_test, y_test, color='blue', linestyle='--', label='True Line')
plt.title('True vs Predicted Values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()

# Потери в 0.0795 на тестовых данных могут быть интерпретированы как хорошие,
# для линейной регрессии, потери в этой величине могут быть интерпретированы как низкие.
# Формула y = 2 * x + 5