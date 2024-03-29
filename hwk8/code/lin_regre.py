import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Monthly memory size data for the process (in megabytes)
memory_size_mb = np.array([50, 293, 763, 1097, 1355, 1567, 1745, 1900, 2037, 2159, 2269, 2370])

# Time in months
months = np.arange(1, len(memory_size_mb) + 1)

# Conversion of memory size to gigabytes for comparison with the 2.8 GB limit
memory_size_gb = memory_size_mb / 1024

# Logarithmic decay model function
def log_decay_model(x, a, b):
    return a + b * np.log(x)

# Curve fitting
params, covariance = curve_fit(log_decay_model, months, memory_size_gb)

# Predicted memory sizes using the fitted model
predicted_memory_size_gb = log_decay_model(months, *params)

# Plot actual vs predicted memory sizes
plt.figure(figsize=(10, 6))
plt.scatter(months, memory_size_gb, color='red', label='Actual Memory Size (GB)')
plt.plot(months, predicted_memory_size_gb, color='blue', label='Predicted Memory Size (GB) using Log Decay Model')
plt.axhline(y=2.8, color='green', linestyle='--', label='2.8 GB Limit')
plt.title('Memory Size Growth and Prediction')
plt.xlabel('Time (Months)')
plt.ylabel('Memory Size (GB)')
plt.legend()
plt.grid(True)
plt.show()

# Solve the model equation for the time when memory size reaches 2.8 GB
from scipy.optimize import fsolve

# Define a function to find when memory size reaches 2.8 GB
def equation_to_solve(month):
    return log_decay_model(month, *params) - 2.8

# Use fsolve to find the month when memory size reaches 2.8 GB
expected_failure_month = fsolve(equation_to_solve, 12) # Starting guess is 12 months

