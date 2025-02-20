""" Discriptive Statistics 
This Focuses on summarizing and describing the data we have about our AI models. The analyze_model_performance() function calculates Measures of central Tendency, Dispersion Measures, Quartile Analysis"""

import numpy as np 
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def analyze_model_performance(model_accuracies, model_name):
    """Analyze and display descriptive statistics for an AI model's performance data
    
    Parameters:
    model_accuracies: List of accuracy scores from different runs/epochs
    model_name: Name of the model for reporting purposes"""
    
    # Converting to numpy array for calculations and measures of centeral tendencies
    accuracies = np.array(model_accuracies)
    
    mean_accuracy = np.mean(accuracies)
    median_accuracy = np.median(accuracies)
    mode_accuracy = stats.mode(accuracies)[0][0]
    
    # Calculating central tendency measures
    std_dev = np.std(accuracies)
    variance = np.var(accuracies)
    range_accuracy = np.ptp(accuracies)
    
    # Quartiles
    q1, q3 = np.percentile(accuracies, [25,75])
    iqr = q3 - q1
    
    print(f"\nDescriptive Statistics for {model_name}")
    print("=" * 50)
    print(f"Central Tendency Measures:")
    print(f"Mean Accuracy: {mean_accuracy:.4f}")
    print(f"Median Accuracy: {median_accuracy:.4f}")
    print(f"Mode Accuracy: {mode_accuracy:.4f}")
    
    print(f"\nDispersion Measures:")
    print(f"Standard Deviation: {std_dev:.4f}")
    print(f"Variance: {variance:.4f}")
    print(f"Range: {range_accuracy:.4f}")
    
    print(f"\nQuartile Analysis:")
    print(f"First Quartile (Q1): {q1:.4f}")
    print(f"Third Quartile (Q3): {q3:.4f}")
    print(f"Interquartile Range (IQR): {iqr:.4f}")
    
    return {
        'mean': mean_accuracy,
        'std_dev': std_dev,
        'quartiles': (q1, median_accuracy, q3)
    }

if __name__ == "__main__":
    # Simulate accuracy scores for two different AI models
    np.random.seed(42)
    model_a_scores = np.random.normal(0.85, 0.03, 100)  # Model A with 85% mean accuracy
    model_b_scores = np.random.normal(0.87, 0.03, 100)  # Model B with 87% mean accuracy
    
    # Analyze individual model performance
    stats_a = analyze_model_performance(model_a_scores, "Model A")
    stats_b = analyze_model_performance(model_b_scores, "Model B")
    