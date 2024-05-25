import numpy as np
from sklearn.metrics import roc_auc_score
import pandas as pd

from expression import roc_auc as my_roc_auc_score


# Функция для генерации данных
def generate_data(n_samples=100, imbalance_ratio=0.5):
    n_class_0 = int(n_samples * imbalance_ratio)
    n_class_1 = n_samples - n_class_0

    X_class_0 = np.random.normal(loc=0.0, scale=1.0, size=(n_class_0, 2))
    X_class_1 = np.random.normal(loc=1.0, scale=1.0, size=(n_class_1, 2))

    y_class_0 = np.zeros(n_class_0)
    y_class_1 = np.ones(n_class_1)

    X = np.vstack((X_class_0, X_class_1))
    y = np.concatenate((y_class_0, y_class_1))

    indices = np.arange(n_samples)
    np.random.shuffle(indices)

    X = X[indices]
    y = y[indices]

    return X, y


# Генерация данных с различной балансировкой
data_50_50 = generate_data(imbalance_ratio=0.5)
data_70_30 = generate_data(imbalance_ratio=0.7)
data_90_10 = generate_data(imbalance_ratio=0.9)


# Сравнение результатов с использованием scikit-learn
for data, ratio in zip([data_50_50, data_70_30, data_90_10], [0.5, 0.7, 0.1]):
    X, y = data
    y_scores = X[:, 0]  # Используем первый признак как предсказание

    my_score = my_roc_auc_score(y_true=y, probabilities=y_scores)
    sklearn_score = roc_auc_score(y_true=y, y_score=y_scores)

    print(f"Balance ratio: {ratio}")
    print(f"My ROC-AUC Score: {my_score}")
    print(f"sklearn ROC-AUC Score: {sklearn_score}")
    print("-----------")