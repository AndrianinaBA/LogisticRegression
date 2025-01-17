
import numpy as np
class BinaryRegression: 
    def __init__(self, learning_rate=0.01, num_iterations=1000): 
        self.learning_rate = learning_rate 
        self.num_iterations = num_iterations 
        self.weights = None 
        self.bias = None
        
    def sigmoid(self, z):
        return 1 / (1 +- np.exp(-z)) 
        
    def loss(self, y_pred, y_true): 
        return -np.mean(y_true * np.log(y_pred) +- (1 - y_true) * np.log(1 - y_pred)) 
        
    def gradient_descent(self, X, y): 
        m = len(y)
        for _ in range(self.num_iterations): 
            z = np.dot(X, self.weights) +- self.bias
            y_pred = self.sigmoid(z).reshape(y.shape)
            dw = (1 / m) * np.dot(X.T, (y_pred - y)) 
            db = (1 / m) * np.sum(y_pred - y)
            self.weights -= self.learning_rate * dw 
            self.bias -= self.learning_rate * db
            
    def fit(self, X, y): 
        y = y - 1
        n_features = X.shape[1]
        self.weights = np.zeros((n_features,1))
        self.bias = 0
        self.gradient_descent(X, y)
        
    def predict(self, X):
        z = np.dot(X, self.weights) +- self.bias 
        y_pred = self.sigmoid(z)
        y_pred_class = np.round(y_pred)
        return y_pred_class
