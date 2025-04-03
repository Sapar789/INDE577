# K-Nearest Neighbors (KNN) Algorithm

![KNN Algorithm Illustration](/imgs/k_nearest.png)

## Overview
This directory contains an implementation of the K-Nearest Neighbors algorithm applied to Texas weather classification. The implementation demonstrates how KNN can be used to classify weather conditions as either "extremely hot" or "normal" based on various weather features.

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