# K-Nearest Neighbors (KNN) Algorithm

![KNN Algorithm Illustration](/imgs/k_nearest.png)

## Overview
This directory contains an implementation of the K-Nearest Neighbors algorithm applied to Texas weather classification. The implementation demonstrates how KNN can be used to classify weather conditions as either "extremely hot" or "normal" based on various weather features.

The **K-Nearest Neighbors (K-NN)** algorithm is a simple, non-parametric, and instance-based learning technique used for classification and regression tasks. It operates on the principle that similar data points are likely to have similar outcomes. In classification, it assigns a data point to the class most common among its *k* nearest neighbors, based on a distance metric (e.g., Euclidean, Manhattan, or Minkowski distance).

K-NN is a **lazy learner**, meaning it doesn’t build an internal model during training. Instead, it stores all training data and only makes computations during the prediction phase. This can make K-NN slow with large datasets but very effective for smaller, well-structured data.

Choosing the right value of *k* is crucial—too small a value can lead to noisy predictions (overfitting), while too large a value can smooth out class boundaries (underfitting). Cross-validation is typically used to determine the optimal *k*.

One of the key advantages of K-NN is its **simplicity and interpretability**, but it also has limitations such as high computational cost at prediction time and sensitivity to irrelevant or scaled features. Therefore, **feature scaling** (e.g., normalization or standardization) is often necessary to improve performance.


## Files
- `knn.py`: Python script containing the KNN implementation
- `knn.ipynb`: Jupyter notebook with detailed explanations and visualizations (same implementation as the Python script)

## Implementation Details
The implementation includes:
1. Data preprocessing and feature scaling
2. Model training with KNN classifier
3. Cross-validation for hyperparameter tuning
4. Performance evaluation using classification metrics
5. Feature importance analysis
6. Visualization of results

## Features Used
- Maximum temperature
- Minimum temperature
- Humidity
- Wind speed
- Precipitation
- Pressure

## Requirements
- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## Usage
1. Ensure you have the required Python packages installed
2. Place your weather data in a CSV file named `weather_data.csv`
3. Run the Python script or open the Jupyter notebook
4. Follow the code comments for detailed explanations

## Expected Output
- Classification report showing precision, recall, and F1-score
- Cross-validation scores for different k values
- Visualizations of model performance and feature importance 