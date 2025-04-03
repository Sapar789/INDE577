# Perceptron for Texas Weather Classification

![](https://www.researchgate.net/profile/Md-Al-Masrur-Khan/publication/372405916/figure/fig7/AS:11431281175096725@1689583258129/Illustration-of-a-single-neuron-perceptron.png)



This section demonstrates the implementation of the Perceptron algorithm for classifying weather conditions in Texas, specifically focusing on identifying rainy vs. non-rainy days. The goal is to understand how a single-layer neural network can learn to classify weather patterns.

## Overview
The Perceptron is one of the simplest forms of artificial neural networks, consisting of a single layer of weights and a threshold activation function. In this implementation, we build a Perceptron from scratch to classify weather conditions, demonstrating the fundamentals of neural network learning..

## Texas Weather Data Features
The following features are used for classification:
- Temperature
- Humidity
- Wind speed
- Atmospheric pressure
- Cloud cover percentage
- Previous day's precipitation
- Dew point
- Wind direction

## Implementation Details
The notebook `perceptron.ipynb` contains:
1. Perceptron implementation from scratch
2. Data preprocessing and feature scaling
3. Training loop implementation
4. Decision boundary visualization
5. Model evaluation and convergence analysis

## Libraries Used
- numpy: For numerical operations and Perceptron implementation
- pandas: For data manipulation
- matplotlib: For visualization
- scikit-learn: For data preprocessing and evaluation

## Story Hook
Can a single neuron learn to distinguish between rainy and non-rainy days? The Perceptron algorithm helps us understand how simple neural networks can learn to classify weather patterns based on basic meteorological features.

## References
1. National Centers for Environmental Information (NCEI) - Weather Data Source
2. "Neural Networks and Deep Learning" by Michael Nielsen
3. "Pattern Recognition and Machine Learning" by Christopher M. Bishop
4. "Deep Learning" by Ian Goodfellow, Yoshua Bengio, and Aaron Courville

## Learning Objectives
- Understand the Perceptron algorithm and its limitations
- Learn to implement a neural network from scratch
- Master data preprocessing for neural networks
- Practice visualization of decision boundaries
- Gain insights into weather pattern classification 