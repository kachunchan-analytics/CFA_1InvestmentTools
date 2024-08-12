import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def calculate_mode(data):
    """
    Calculate the mode of a dataset.

    Parameters:
        data (array-like): Input data.

    Returns:
        mode (float): The mode of the data.
        mode_type (str): The type of mode (unimodal, bimodal, trimodal, or no mode).
    """
    mode = stats.mode(data)[0][0]
    mode_count = np.sum(data == mode)
    unique_values = np.unique(data)
    if len(unique_values) == len(data):
        mode_type = "No Mode"
    elif mode_count == 1:
        mode_type = "Unimodal"
    elif mode_count == 2:
        mode_type = "Bimodal"
    elif mode_count == 3:
        mode_type = "Trimodal"
    else:
        mode_type = "Multimodal"
    return mode, mode_type

def calculate_bin_width(data, num_bins):
    """
    Calculate the bin width for a histogram.

    Parameters:
        data (array-like): Input data.
        num_bins (int): Number of bins.

    Returns:
        bin_width (float): The bin width.
    """
    data_range = np.ptp(data)
    bin_width = data_range / num_bins
    return bin_width

def identify_modal_interval(data, num_bins):
    """
    Identify the modal interval in a histogram.

    Parameters:
        data (array-like): Input data.
        num_bins (int): Number of bins.

    Returns:
        modal_interval (tuple): The modal interval (lower, upper).
    """
    hist, bins = np.histogram(data, bins=num_bins)
    max_freq_idx = np.argmax(hist)
    modal_interval = (bins[max_freq_idx], bins[max_freq_idx + 1])
    return modal_interval

def plot_histogram(data, num_bins):
    """
    Plot a histogram of the data.

    Parameters:
        data (array-like): Input data.
        num_bins (int): Number of bins.
    """
    plt.hist(data, bins=num_bins)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

if __name__ == "__main__":
    # Example usage
    data = np.random.normal(0, 1, 1000)
    mode, mode_type = calculate_mode(data)
    print(f"Mode: {mode}, Mode Type: {mode_type}")

    num_bins = 10
    bin_width = calculate_bin_width(data, num_bins)
    print(f"Bin Width: {bin_width}")

    modal_interval = identify_modal_interval(data, num_bins)
    print(f"Modal Interval: {modal_interval}")

    plot_histogram(data, num_bins)
