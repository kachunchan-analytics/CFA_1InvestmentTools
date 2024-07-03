import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve

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

def calculate_elasticity_coefficient(price, quantity, initial_quantity, initial_price):
    """
    Calculates the elasticity coefficient at a given price and quantity.

    Args:
        price (float): The price at which to calculate the elasticity.
        quantity (float): The quantity demanded at the given price.
        initial_quantity (float): The initial quantity demanded.
        initial_price (float): The initial price.

    Returns:
        float: The elasticity coefficient.
    """

    percentage_change_quantity = ((quantity - initial_quantity) / initial_quantity) * 100
    percentage_change_price = ((price - initial_price) / initial_price) * 100
    elasticity = percentage_change_quantity / percentage_change_price
    return elasticity

def calculate_unitary_elasticity_point(prices, quantities):
    """
    Calculates the price and quantity at which demand is unitary elastic.

    Args:
        prices (list): A list of prices.
        quantities (list): A list of corresponding quantities demanded.

    Returns:
        tuple: A tuple containing the price and quantity at unitary elasticity.
    """

    for i in range(1, len(prices)):  # Start from the second price point
        # Calculate the elasticity between the current and previous point
        elasticity = calculate_elasticity_coefficient(prices[i], quantities[i], quantities[i - 1], prices[i - 1])

        # Check if the elasticity is close to 1 (unitary elasticity)
        if abs(elasticity - 1) < 0.01:  # Allow for small rounding errors
            return prices[i], quantities[i]

    return None, None  # Return None if no unitary elasticity point is found

def plot_demand_curve(prices, quantities, elasticity, unitary_elasticity_point):
    """
    Plots a demand curve and highlights the elasticity point and unitary elasticity point.

    Args:
        prices (list): A list of prices.
        quantities (list): A list of corresponding quantities demanded.
        elasticity (float): The own-price elasticity of demand.
        unitary_elasticity_point (tuple): A tuple containing the price and quantity at unitary elasticity.
    """

    plt.figure(figsize=(8, 6))
    plt.plot(prices, quantities, label="Demand Curve")
    plt.xlabel("Price")
    plt.ylabel("Quantity Demanded")
    plt.title("Demand Curve with Elasticity and Unitary Elasticity Points")

    # Find the point on the curve with the given elasticity
    elasticity_point = np.interp(elasticity, quantities, prices)
    elasticity_quantity = np.interp(elasticity_point, prices, quantities)

    # Highlight the elasticity point
    plt.scatter(elasticity_point, elasticity_quantity, color="red", label="Elasticity Point")

    # Highlight the unitary elasticity point
    if unitary_elasticity_point:
        unitary_price, unitary_quantity = unitary_elasticity_point
        plt.scatter(unitary_price, unitary_quantity, color="green", label="Unitary Elasticity Point")

    plt.legend()
    plt.grid(True)
    plt.show()

def find_demand_function(prices, quantities):
    """
    Finds a linear demand function using SymPy.

    Args:
        prices (list): A list of prices.
        quantities (list): A list of corresponding quantities demanded.

    Returns:
        sympy.core.expr.Expr: The demand function.
    """

    p = symbols('p')
    q = symbols('q')
    equation = Eq(q, prices[0] - (prices[0] - prices[1]) / (quantities[0] - quantities[1]) * (p - quantities[0]))
    return solve(equation, q)[0]

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

    # Calculate the elasticity coefficient at each point
    for i in range(len(prices)):
        coefficient = calculate_elasticity_coefficient(prices[i], quantities[i], quantities[0], prices[0])
        print(f"Elasticity coefficient at price {prices[i]}: {coefficient:.2f}")

    # Calculate the unitary elasticity point
    unitary_price, unitary_quantity = calculate_unitary_elasticity_point(prices, quantities)
    print(f"Unitary elasticity point: Price = {unitary_price}, Quantity = {unitary_quantity}")

    # Find the demand function
    demand_function = find_demand_function(prices, quantities)
    print(f"Demand function: {demand_function}")

    # Plot the demand curve
    plot_demand_curve(prices, quantities, elasticity, (unitary_price, unitary_quantity))