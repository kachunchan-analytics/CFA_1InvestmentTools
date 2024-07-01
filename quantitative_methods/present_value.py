import numpy as np

def calculate_present_value(fv, r, n):
  """
  Calculates the present value of a single cash flow.

  Args:
    fv: Future value of the cash flow.
    r: Discount rate per period.
    n: Number of periods.

  Returns:
    The present value of the cash flow.
  """
  pv = fv / (1 + r)**n
  return pv

if __name__ == "__main__":
  fv = float(input("Enter the future value: "))
  r = float(input("Enter the discount rate (as a decimal): "))
  n = int(input("Enter the number of periods: "))

  pv = calculate_present_value(fv, r, n)
  print(f"The present value is: {pv:.2f}")