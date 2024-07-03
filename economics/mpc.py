import numpy as np
import pandas as pd

def calculate_keyesian_multiplier(mpc):
  """Calculates the Keynesian multiplier based on the marginal propensity to consume (MPC).

  Args:
    mpc: The marginal propensity to consume (MPC), a value between 0 and 1.

  Returns:
    The Keynesian multiplier, a value greater than 1.
  """
  return 1 / (1 - mpc)

def simulate_multiplier_effect(initial_spending, mpc, rounds=5):
  """Simulates the multiplier effect of government spending.

  Args:
    initial_spending: The initial amount of government spending.
    mpc: The marginal propensity to consume (MPC).
    rounds: The number of rounds to simulate.

  Returns:
    A list of total spending for each round, including the initial spending.
  """
  total_spending = [initial_spending]
  for _ in range(rounds):
    new_spending = total_spending[-1] * mpc
    total_spending.append(total_spending[-1] + new_spending)
  return total_spending

def calculate_mpc(income_change, consumption_change):
  """
  Calculates the marginal propensity to consume (MPC).

  Args:
    income_change: The change in income.
    consumption_change: The change in consumption.

  Returns:
    The MPC as a float.
  """
  return consumption_change / income_change

def analyze_mpc_data(data):
  """
  Analyzes MPC data and provides insights.

  Args:
    data: A pandas DataFrame containing income change and consumption change data.

  Returns:
    A summary of the analysis, including average MPC, MPC by income level, and potential economic implications.
  """
  # Calculate average MPC
  average_mpc = data['Consumption Change'].sum() / data['Income Change'].sum()

  # Group data by income level and calculate MPC for each group
  mpc_by_income = data.groupby('Income Level')['Consumption Change'].sum() / data.groupby('Income Level')['Income Change'].sum()

  # Provide insights based on the analysis
  print(f"Average MPC: {average_mpc:.2f}")
  print("\nMPC by Income Level:")
  print(mpc_by_income)

  # Additional insights could be added here, such as:
  # - Identifying potential trends in MPC based on income level
  # - Relating MPC to economic indicators like GDP growth
  # - Suggesting potential policy implications based on the MPC analysis

if __name__ == "__main__":
  # Example usage:
  data = pd.DataFrame({
    'Income Change': [500, 1000, 2000, 3000],
    'Consumption Change': [400, 100, 1500, 2500],
    'Income Level': ['Low', 'Low', 'Medium', 'High']
  })

  analyze_mpc_data(data)

  # Example usage of Keynesian multiplier functions
  mpc = 0.75  # Marginal propensity to consume
  initial_spending = 100  # Initial government spending

  multiplier = calculate_keyesian_multiplier(mpc)
  print(f"\nKeynesian Multiplier: {multiplier}")

  spending_rounds = simulate_multiplier_effect(initial_spending, mpc, rounds=5)
  print("Total Spending per Round:")
  for i, spending in enumerate(spending_rounds):
    print(f"Round {i+1}: ${spending:,.2f}")