import pandas as pd
import matplotlib.pyplot as plt

def calculate_productivity_measures(labor_input, total_product):
  """
  Calculates total product, average product, and marginal product.

  Args:
    labor_input: A list of labor inputs.
    total_product: A list of total product values corresponding to the labor inputs.

  Returns:
    A pandas DataFrame containing the calculated productivity measures.
  """

  # Calculate average product
  average_product = [total_product[i] / labor_input[i] for i in range(len(labor_input))]

  # Calculate marginal product
  marginal_product = [total_product[i] - total_product[i-1] for i in range(1, len(total_product))]
  marginal_product.insert(0, 0)  # Add a 0 for the first labor input

  # Create a pandas DataFrame
  df = pd.DataFrame({
      'Labor Input': labor_input,
      'Total Product': total_product,
      'Average Product': average_product,
      'Marginal Product': marginal_product
  })

  return df

def plot_productivity_curves(df):
  """
  Plots the total product, average product, and marginal product curves.

  Args:
    df: A pandas DataFrame containing the productivity measures.
  """

  plt.figure(figsize=(10, 6))
  plt.plot(df['Labor Input'], df['Total Product'], label='Total Product')
  plt.plot(df['Labor Input'], df['Average Product'], label='Average Product')
  plt.plot(df['Labor Input'], df['Marginal Product'], label='Marginal Product')

  plt.xlabel('Labor Input')
  plt.ylabel('Output')
  plt.title('Productivity Curves')
  plt.legend()
  plt.grid(True)
  plt.show()

def show_diminishing_marginal_returns(df):
  """
  Prints a message indicating whether diminishing marginal returns are present.

  Args:
    df: A pandas DataFrame containing the productivity measures.
  """

  if all(df['Marginal Product'][i] >= df['Marginal Product'][i+1] for i in range(len(df['Marginal Product']) - 1)):
    print("Diminishing marginal returns are present.")
  else:
    print("Diminishing marginal returns are not present.")

if __name__ == "__main__":
  # Example usage
  labor_input = [0, 1, 2, 3, 4, 5, 6, 7]
  total_product = [0, 20, 50, 90, 120, 140, 150, 150]

  productivity_df = calculate_productivity_measures(labor_input, total_product)
  print(productivity_df)

  plot_productivity_curves(productivity_df)
  show_diminishing_marginal_returns(productivity_df)