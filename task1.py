
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.

import numpy as np
import matplotlib.pyplot as plt
def pearson_correlation(x, y):
    n = len(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    std_x = np.std(x)
    std_y = np.std(y)
    covariance = np.sum((x - mean_x) * (y - mean_y))
    correlation = covariance / (n * std_x * std_y)
    return correlation
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])
correlation = pearson_correlation(x, y)
print(f"Pearson correlation: {correlation}")
plt.scatter(x, y, color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Pearson Correlation')
plt.text(1, 5, f'Correlation: {correlation:.2f}', color='red')
plt.plot([np.min(x), np.max(x)], [np.min(y), np.max(y)], color='green')
plt.show()