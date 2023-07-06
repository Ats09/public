import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Задаем параметры для H0 (нулевая гипотеза)
mu_0 = 0  # Среднее значение
sigma_0 = 1  # Стандартное отклонение

# Задаем параметры для H1 (альтернативная гипотеза)
mu_1 = 1  # Среднее значение
sigma_1 = 1  # Стандартное отклонение

# Задаем диапазон значений для оси x
x = np.linspace(-5, 5, 1000)

# Вычисляем плотности вероятности для H0 и H1
pdf_h0 = stats.norm.pdf(x, loc=mu_0, scale=sigma_0)
pdf_h1 = stats.norm.pdf(x, loc=mu_1, scale=sigma_1)

# Определяем границы для ошибок первого и второго рода
threshold = 1.96  # Значение z-статистики для уровня значимости 0.05 (двусторонний тест)

# Вычисляем области для ошибок первого и второго рода
area_h0_2 = np.sum(pdf_h1[x < -threshold])
area_h1_1 = np.sum(pdf_h0[x < -threshold])

# Рисуем графики
plt.plot(x, pdf_h0, label='H0')
plt.plot(x, pdf_h1, label='H1')

# Закрашиваем области для ошибок первого и второго рода
plt.fill_between(x[x < -threshold], pdf_h0[x < -threshold], color='red', alpha=0.3, label='Ошибка 1-го рода')
plt.fill_between(x[x > threshold], pdf_h0[x > threshold], color='red', alpha=0.3)
plt.fill_between(x[x > -threshold], pdf_h1[x > -threshold], color='blue', alpha=0.3, label='Ошибка 2-го рода')
plt.fill_between(x[x < threshold], pdf_h1[x < threshold], color='blue', alpha=0.3)

# Отображаем легенду и названия осей
plt.legend()
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')

# Отображаем график
plt.show()