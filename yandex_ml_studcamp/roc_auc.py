import numpy as np


def roc_auc(probabilities, y_true):
    y_proba = np.array(probabilities)
    y_true = np.array(y_true)
    print(f'{y_proba = }')
    print(f'{y_true = }')

    # сортировка данных по probabilities повозрастанию
    sorted_indices = np.argsort(y_proba)[::-1]
    y_proba = np.array(y_proba)[sorted_indices]
    y_true = np.array(y_true)[sorted_indices]
    print(f'{y_proba = }')
    print(f'{y_true = }')
    TPRs = []
    FPRs = []

    TPR_prev = 0
    FPR_prev = 0

    S = 0

    # подсчет ROC_AUC
    for i in range(len(y_true) + 1):
        # i - порог
        # для любого j < i будем считать, что y_proba[j] — положительный класс

        TP = 0
        FP = 0
        FN = 0
        TN = 0

        for j in range(len(y_true)):
            if j < i and y_true[j] == 1:
                TP += 1
            if j >= i and y_true[j] == 0:
                TN += 1
            if j < i and y_true[j] == 0:
                FP += 1
            if j >= i and y_true[j] == 1:
                FN += 1

        TPR = TP / (TP + FN)
        FPR = FP / (FP + TN)
        print(f'{TPR = }, {FPR = }')

        if FPR != 0:
            x = FPR - FPR_prev
            y = TPR
            s = x * y
            S += s

        TPRs.append(TPR)
        FPRs.append(FPR)

        TPR_prev = TPR
        FPR_prev = FPR

    # TPRs.append(1.0)
    # FPRs.append(1.0)

    import matplotlib.pyplot as plt

    plt.scatter(y=TPRs, x=FPRs)
    plt.show()

    return S


# Пример использования
probabilities = [0.1, 0.4, 0.35, 0.8]
y_true = [0, 0, 1, 1]

# probabilities = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# y_true = [1, 1, 0, 1, 0, 0, 1, 0, 0]

# probabilities = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# y_true = [1, 1, 1, 1, 0, 0, 0, 0, 0]

S = roc_auc(probabilities, y_true)

print(S)  # Должно вывести 0.75

from sklearn.metrics import roc_auc_score

print(roc_auc_score(y_score=probabilities, y_true=y_true))
