from sklearn.linear_model import LogisticRegression

class Learner:
    def __init__(self, train, test):
        self._train_x = train[0]
        self._train_y = train[1]
        self._test_x = test[0]
        self._test_y = test[1]
    def learn(self):
        _classifier = LogisticRegression().fit(self._train_x, self._train_y)
        
