# Decision Trees for Texas Weather Classification

This section demonstrates the implementation of Decision Trees for classifying weather conditions in Texas, specifically focusing on identifying stormy weather patterns. The goal is to understand which weather features are most important for predicting storm conditions.

## Overview
Decision Trees are powerful classification algorithms that make predictions by learning simple decision rules from the data features. In this implementation, we use Decision Trees to classify weather conditions and identify the most important meteorological features that contribute to storm formation.

## Texas Weather Data Features
The following features are used for classification:
- Temperature (current and previous day)
- Humidity levels
- Wind speed and direction
- Barometric pressure
- Precipitation history
- Cloud cover
- Atmospheric stability indices

## Implementation Details
The notebook `decision_trees.ipynb` contains:
1. Data preprocessing and feature engineering
2. Decision Tree model implementation
3. Feature importance analysis
4. Tree visualization and interpretation
5. Model evaluation and pruning

## Libraries Used
- scikit-learn: For Decision Tree implementation
- pandas: For data manipulation
- numpy: For numerical operations
- matplotlib: For visualization
- graphviz: For tree visualization
- seaborn: For enhanced visualizations

## Story Hook
What weather conditions lead to storm formation in Texas? Decision Trees help us identify the key meteorological features and their thresholds that are most predictive of stormy weather.

## References
1. National Centers for Environmental Information (NCEI) - Weather Data Source
2. scikit-learn Documentation - DecisionTreeClassifier
3. "Introduction to Machine Learning with Python" by Andreas C. Müller and Sarah Guido
4. "Machine Learning: A Probabilistic Perspective" by Kevin P. Murphy

## Learning Objectives
- Understand how Decision Trees work for classification
- Learn to interpret feature importance in weather prediction
- Master tree visualization and pruning techniques
- Practice model evaluation and optimization
- Gain insights into storm prediction patterns 