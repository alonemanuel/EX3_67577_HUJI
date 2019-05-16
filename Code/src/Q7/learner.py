from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

N_OF_ITER = 10


class Learner:
    def __init__(self, X_data, y_data):
        logger("Initing")
        self._X_data = X_data
        self._y_data = y_data
        self._X_train = None
        self._X_test = None
        self._y_train = None
        self._y_test = None
        self._classifier = None

    def split_to_train_test(self, split_ratio):
        logger("Splitting to train and test")
        split = train_test_split(self._X_data, self._y_data, split_ratio)
        self._X_train, self._X_test = split[0], split[1]
        self._y_train, self._y_test = split[2], split[3]

    def fit_logistic(self):
        logger("Fitting logistic")
        self._classifier = LogisticRegression().fit(self._X_train,
                                                    self._y_train)

    def plot_roc(self):
        logger("Plotting ROC")
        self.split_to_train_test(1000 / self._X_data.shape[0])
        self.fit_logistic()
        predicts = self._classifier.predict_proba(self._X_test)
        np.sort(predicts)
        n_pos = self.get_n_pos()

    def get_n_pos(self):
        return np.count_nonzero(self._y_test)


    def plot_more_roc(self):
        logger("Plotting more ROCs")
        for i in range(10):
            self.plot_roc()



def logger(*args):
    print('Log: ', end='')
    for arg in args:
        print(arg, end='')
    print()