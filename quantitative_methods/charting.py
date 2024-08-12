import matplotlib.pyplot as plt
import numpy as np

def grouped_bar_chart(labels, men_means, women_means, title, xlabel, ylabel):
    """
    Create a Grouped Bar Chart.

    Parameters:
    labels (list): List of labels for the x-axis.
    men_means (list): List of values for the first group.
    women_means (list): List of values for the second group.
    title (str): Title of the chart.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    """
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label='Men')
    rects2 = ax.bar(x + width/2, women_means, width, label='Women')

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

def stacked_bar_chart(labels, men_means, women_means, title, xlabel, ylabel):
    """
    Create a Stacked Bar Chart.

    Parameters:
    labels (list): List of labels for the x-axis.
    men_means (list): List of values for the first group.
    women_means (list): List of values for the second group.
    title (str): Title of the chart.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    """
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x, men_means, width, label='Men')
    ax.bar(x, women_means, width, bottom=men_means, label='Women')

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

def bubble_line_chart(x, y, z, title, xlabel, ylabel):
    """
    Create a Bubble Line Chart.

    Parameters:
    x (list): List of x-coordinates.
    y (list): List of y-coordinates.
    z (list): List of bubble sizes.
    title (str): Title of the chart.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    """
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=z)

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xlabel(xlabel)

    plt.show()

if __name__ == "__main__":
    # Example usage
    labels = ['A', 'B', 'C', 'D', 'E']
    men_means = [10, 15, 7, 12, 20]
    women_means = [8, 12, 10, 15, 18]

    grouped_bar_chart(labels, men_means, women_means, 'Grouped Bar Chart', 'X-axis', 'Y-axis')
    stacked_bar_chart(labels, men_means, women_means, 'Stacked Bar Chart', 'X-axis', 'Y-axis')

    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 12, 20]
    z = [100, 200, 50, 150, 250]

    bubble_line_chart(x, y, z, 'Bubble Line Chart', 'X-axis', 'Y-axis')
