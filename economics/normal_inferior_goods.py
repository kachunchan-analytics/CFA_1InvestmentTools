import matplotlib.pyplot as plt

def plot_demand_curves(normal_demand, inferior_demand, income_levels):
    """
    Plots the demand curves for normal and inferior goods.

    Args:
        normal_demand (list): Demand values for the normal good at each income level.
        inferior_demand (list): Demand values for the inferior good at each income level.
        income_levels (list): List of income levels.

    Returns:
        None
    """

    plt.plot(income_levels, normal_demand, label="Normal Good")
    plt.plot(income_levels, inferior_demand, label="Inferior Good")

    plt.xlabel("Income")
    plt.ylabel("Demand")
    plt.title("Demand for Normal and Inferior Goods")
    plt.legend()
    plt.show()

# Example usage:
if __name__ == "__main__":
    income_levels = [10, 20, 30, 40, 50]
    normal_demand = [15, 20, 25, 30, 35]
    inferior_demand = [25, 20, 15, 10, 5]
    plot_demand_curves(normal_demand, inferior_demand, income_levels)