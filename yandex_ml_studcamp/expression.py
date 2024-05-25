import numpy as np


def roc_auc(probabilities, y_true):
    # преобразуем в numpy arrays
    y_proba = np.array(probabilities)
    y_true = np.array(y_true)

    # сортировка данных по probabilities по возрастанию
    sorted_indexes = np.argsort(y_proba)[::-1]
    # y_proba = y_proba[sorted_indexes]
    y_true = y_true[sorted_indexes]

    roc_auc_value: np.float64 = np.float64(0.0)  # итоговая площадь
    FPR_prev = 0  # понадобится для вычисления площади
    for i in range(len(y_true) + 1):  # подсчет ROC_AUC
        # i - порог
        # для любого j < i будем считать, что y_proba[j] — положительный класс

        # считаем по определению TP, FP, FN, TN при пороге = i
        TP, FP, FN, TN = 0, 0, 0, 0
        for j in range(len(y_true)):
            if j < i and y_true[j] == 1:
                TP += 1
            if j >= i and y_true[j] == 0:
                TN += 1
            if j < i and y_true[j] == 0:
                FP += 1
            if j >= i and y_true[j] == 1:
                FN += 1

        # считаем по определению TPR, FPR при пороге = i

        if TP + FN == 0:
            pass
        if FP + TN == 0:
            pass

        TPR = TP / (TP + FN)
        FPR = FP / (FP + TN)

        # считаем площадь
        if FP != 0:  # тоже самое, что и "FPR != 0"
            # если точка ROC-кривой сдвинулась вправо по оси FPR,
            # то добавим площадь, которая образуется за счет этого сдвига, в итоговый результат
            x: np.float64 = np.float64(FPR - FPR_prev)  # сдвиг по оси x (FPR)
            y: np.float64 = np.float64(TPR)  # координата по оси y (TPR)
            delta_s: np.float64 = np.float64(x * y)  # площадь
            roc_auc_value += delta_s

        FPR_prev = FPR
    return roc_auc_value

# probabilities = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# y_true = [1, 1, 0, 1, 0, 0, 1, 0, 0]
#
# probabilities = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# y_true = [1, 1, 1, 1, 0, 0, 0, 0, 0]
#
#
# from sklearn.metrics import roc_auc_score
# roc_auc_mine = roc_auc(probabilities, y_true)
# roc_auc_real = roc_auc_score(y_score=probabilities, y_true=y_true)
# print(roc_auc_mine)
# print(roc_auc_real)
