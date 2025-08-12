import csv
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import matplotlib.pyplot as plt



def load_data(data_file: str):
    with open(data_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    df = pd.DataFrame(data)

    # convert the numeric columns
    df['age'] = pd.to_numeric(df['age'])
    df['tumor_size_mm'] = pd.to_numeric(df['tumor_size_mm'])
    df['biomarker_CA125'] = pd.to_numeric(df['biomarker_CA125'])

    return df


def preprocess_data(df: pd.DataFrame):
    """Encode categorical variables and prepare features"""
    # create label encoders for categorical variables
    label_encoders = {}
    categorical_cols = ['ER_status', 'stage', 'hospital']

    for col in categorical_cols:
        le = LabelEncoder()
        df[col + '_encoded'] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    # prepare feature matrix X and target vector y
    feature_cols = ['age', 'tumor_size_mm', 'biomarker_CA125', 
                    'ER_status_encoded', 'stage_encoded', 'hospital_encoded']
    X = df[feature_cols].values
    y = df['diagnosis'].values

    return X, y, feature_cols, label_encoders


def build_decision_tree(X, y, feature_names):
    """Build and train decision tree classifier"""
    # Split data into training and testing sets
    """I'm using an 80-20 split, which is standard in medical ML. 
    With limited patient data, this balance ensures sufficient training samples while maintaining a meaningful test set for validation.
    Stratification is critical in medical datasets where class imbalance is common. 
    This ensures both training and test sets maintain the same proportion of diagnoses, preventing bias in our evaluation."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=27, stratify=y)

    # Create decision tree classifier
    """I chose Gini impurity over entropy because it's computationally faster and works well for binary and multi-class medical classification problems. 
    Gini measures the probability of misclassifying a randomly chosen sample.
    A depth of 5 creates interpretable decision paths while preventing overfitting. 
    In medical contexts, we need doctors to understand the decision logic - a 5-level tree is still comprehensible.
    I require at least 5 samples before splitting a node. 
    This ensures statistical significance and prevents the tree from making decisions based on too few patients, which could be dangerous in medical applications.
    Each leaf must contain at least 3 samples. This prevents overfitting to individual patients and ensures our predictions are based on meaningful patient groups.
    """
    dt_classifier = DecisionTreeClassifier(
        criterion='gini',
        max_depth=5,
        min_samples_split=5,
        min_samples_leaf=3,
        random_state=27
    )

    # Train the model
    """The fit method learns the optimal decision boundaries from our training data using the CART algorithm."""
    dt_classifier.fit(X_train, y_train)

    print(f"Tree depth: {dt_classifier.get_depth()}")
    print(f"Number of leaves: {dt_classifier.get_n_leaves()}")

    return dt_classifier, X_train, X_test, y_train, y_test


def evaluate_model(model, X_train, X_test, y_train, y_test, feature_names):
    """Comprehensive model evalutation"""
    # Make predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Calculate accuracies
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)

    print(f"Training Accuracy: {train_accuracy:.3f}")
    print(f"Test Accuracy: {test_accuracy:.3f}")

    # Feature importance analysis
    feature_importance = model.feature_importances_
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': feature_importance
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    for _, row in importance_df.iterrows():
        print(f"{row['feature']}: {row['importance']:.3f}")
    
    return y_test_pred, importance_df


# Visualize results
def visualize_results(y_test, y_test_pred, importance_df):
    """Create visualizations for model interpretation"""
    print("Creating visualizations...")
    
    # Confusion Matrix
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    cm = confusion_matrix(y_test, y_test_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    
    # Feature Importance
    plt.subplot(1, 2, 2)
    plt.barh(importance_df['feature'], importance_df['importance'])
    plt.title('Feature Importance')
    plt.xlabel('Importance Score')
    plt.tight_layout()
    
    plt.show()


def main():
    data_file = r'others/simulated_medical_dataset.csv'

    try:
        # read data
        data = load_data(data_file)

        # data preprocess
        X, y, feature_names, label_encoders = preprocess_data(data)

        # build model
        model, X_train, X_test, y_train, y_test = build_decision_tree(X, y, feature_names)

        # evaluate model
        evaluate_model(model, X_train, X_test, y_train, y_test, feature_names)

        # visualize results (if needed)
        visualize_results(y_test, y_pred, importance_df)
    except FileNotFoundError:
        print(f"Error: Could not find file '{data_file}'")
        print("Please ensure the file path is correct.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



if __name__ == '__main__':
    main()
