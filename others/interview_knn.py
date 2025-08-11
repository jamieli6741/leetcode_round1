import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error


class BaseRegressor:
    """
    Abstract Base Class for regression models
    """
    def fit(self, X, y):
        pass

    def predict(self, X):
        pass

    def get_model_name(self):
        pass


class LinearRegressionModel(BaseRegressor):
    def __init__(self):
        self.model = LinearRegression()
        self.fitted = False

    def fit(self, X, y):
        self.model.fit(X, y)
        self.fitted = True
        return self
    
    def predict(self, X):
        if not self.fitted:
            raise ValueError("Model must be fitted before prediction")
        return self.model.predict(X)
    
    def get_model_name(self):
        return "Linear Regression"
    
    def get_model_params(self):
        if not self.fitted:
            return None
        return {
            'slope': self.model.coef_[0],
            'intercept': self.model.intercept_
        }
    

class KNNRegressionModel(BaseRegressor):
    def __init__(self, n_neighbors=3):
        self.model = KNeighborsRegressor(n_neighbors=n_neighbors)
        self.n_neighbors = n_neighbors
        self.fitted = False

    def fit(self, X, y):
        self.model.fit(X, y)
        self.fitted = True
        return self
    
    def predict(self, X):
        if not self.fitted:
            raise ValueError("Model must be fitted before prediction")
        return self.model.predict(X)
    
    def get_model_name(self):
        return f"KNN Regression with k={self.n_neighbors}"
        


class RegressionSolver:
    """
    Main solver class that can work with different regression algorithms
    """
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.trained_models = {}  # Store trained models and their results

    
    def train_model(self, name:str, model: BaseRegressor):
        """Train a model and store results"""
        print(f"\nTraining {name} : {model.get_model_name()} ...")

        # Fit model
        model.fit(self.X, self.y)

        # Evaluate model
        y_pred = model.predict(self.X)
        r2 = r2_score(self.y, y_pred)
        mse = mean_squared_error(self.y, y_pred)
        rmse = np.sqrt(mse)

        # Store results
        self.trained_models[name] = {
            'model': model,
            'r2': r2,
            'mse': mse,
            'rmse': rmse,
            'predictions': y_pred
        }

        # Print results
        print(f"R2 score: {r2:.4f}")
        print(f"RMSE: {rmse:.4f}")
        
        # Show linear regression params
        if hasattr(model, 'get_model_params'):
            params = model.get_model_params()
            if params:
                print(f"Equation: height = {params['slope']:.4f} * age + {params['intercept']:.4f}")

        return self.trained_models[name]

    def predict_with_model(self, model_name:str, target_value):
        """Make predictions using a specific trained model"""
        if model_name not in self.trained_models:
            raise ValueError(f"Model '{model_name}' not found. Available models: {list(self.trained_models.keys())}")
        
        model = self.trained_models[model_name]['model']
        if isinstance(target_value, (int, float)):
            target_X = np.array([[target_value]])
        else:
            target_X = np.array(target_value).reshape(-1, 1)

        predictions = model.predict(target_X)
        return predictions[0] if len(predictions) == 1 else predictions
    


# Load data
reg_data = pd.read_csv('regression_data.csv')
cls_data = pd.read_csv('classification_data.csv')
ages = reg_data['age'].tolist()
heights = reg_data['height'].tolist()

X = reg_data[['age']].values
y = reg_data['height'].values

# Initialize solver
solver = RegressionSolver(X, y)

# Linear regression 
linear_model = LinearRegressionModel()
linear_results = solver.train_model("Linear", linear_model)
linear_pred = linear_model.predict([[55]])
print(linear_pred)

# KNN with k=3
knn3_model = KNNRegressionModel(n_neighbors=3)
knn3_results = solver.train_model("KNN_k3", knn3_model)
knn3_pred = knn3_model.predict([[55]])
print(knn3_pred)
