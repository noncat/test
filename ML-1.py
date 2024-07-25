import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

x = np.linspace(-10, 10, 400).reshape(-1, 1)
y = 2 * x**2

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', solver='adam', max_iter=1000)

model.fit(x_train, y_train.ravel())

y_pred = model.predict(x_test)
loss = mean_squared_error(y_test, y_pred)
print(f'Test Loss: {loss}')

plt.scatter(x_test, y_test, label='Реальные данные')
plt.scatter(x_test, y_pred, label='Прогнозируемые данные')
plt.legend()
plt.show()
