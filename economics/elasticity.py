import matplotlib.pyplot as plt
import numpy as np

def calculate_own_price_elasticity(initial_quantity, final_quantity, initial_price, final_price):
    """
    Calculates the own-price elasticity of demand.

    Args:
        initial_quantity (float): The initial quantity demanded.
        final_quantity (float): The final quantity demanded.
        initial_price (float): The initial price.
        final_price (float): The final price.

    Returns:
        float: The own-price elasticity of demand.
    """

    percentage_change_quantity = ((final_quantity - initial_quantity) / initial_quantity) * 100
    percentage_change_price = ((final_price - initial_price) / initial_price) * 100
    elasticity = percentage_change_quantity / percentage_change_price
    return elasticity

def plot_demand_curve(prices, quantities, elasticity):
    """
    Plots a demand curve and highlights the elasticity point.

    Args:
        prices (list): A list of prices.
        quantities (list): A list of corresponding quantities demanded.
        elasticity (float): The own-price elasticity of demand.
    """

    plt.figure(figsize=(8, 6))
    plt.plot(prices, quantities, label="Demand Curve")
    plt.xlabel("Price")
    plt.ylabel("Quantity Demanded")
    plt.title("Demand Curve with Elasticity Point")

    # Find the point on the curve with the given elasticity
    elasticity_point = np.interp(elasticity, quantities, prices)
    elasticity_quantity = np.interp(elasticity_point, prices, quantities)

    # Highlight the elasticity point
    plt.scatter(elasticity_point, elasticity_quantity, color="red", label="Elasticity Point")

    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example usage:
    initial_quantity = 100
    final_quantity = 80
    initial_price = 10
    final_price = 12

    elasticity = calculate_own_price_elasticity(initial_quantity, final_quantity, initial_price, final_price)
    print(f"Own-price elasticity of demand: {elasticity:.2f}")

    # Example demand curve data
    prices = [5, 6, 7, 8, 9, 10, 11, 12]
    quantities = [120, 110, 100, 90, 80, 70, 60, 50]

    plot_demand_curve(prices, quantities, elasticity)