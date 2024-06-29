def future_value(pv, r, n):
  """
  Calculates the future value (FV) of a present value (PV) investment.

  Args:
    pv: The present value of the investment.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The future value of the investment.
  """
  return pv * (1 + r) ** n

def present_value(fv, r, n):
  """
  Calculates the present value (PV) of a future value (FV) investment.

  Args:
    fv: The future value of the investment.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The present value of the investment.
  """
  return fv / (1 + r) ** n

def payment(pv, r, n):
  """
  Calculates the payment (PMT) required to reach a future value (FV) over a specified period.

  Args:
    pv: The present value of the investment.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The required payment per period.
  """
  return (pv * r * (1 + r) ** n) / ((1 + r) ** n - 1)

def future_value_with_payment(pmt, r, n):
  """
  Calculates the future value (FV) of an investment with regular payments.

  Args:
    pmt: The payment amount per period.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The future value of the investment with payments.
  """
  return pmt * (((1 + r) ** n - 1) / r)

def present_value_with_payment(pmt, r, n):
  """
  Calculates the present value (PV) of an investment with regular payments.

  Args:
    pmt: The payment amount per period.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The present value of the investment with payments.
  """
  return pmt * ((1 - (1 + r) ** -n) / r)

def calculate_future_value_of_uneven_cash_flows(cash_flows, interest_rate):
    """
    Calculates the future value of a series of uneven cash flows.

    Args:
        cash_flows (list): A list of cash flow amounts.
        interest_rate (float): The annual interest rate.

    Returns:
        float: The future value of the uneven cash flows.
    """

    # Calculate the future value of each cash flow individually
    future_values = [cash_flow * (1 + interest_rate)**(len(cash_flows) - i - 1) for i, cash_flow in enumerate(cash_flows)]

    # Sum up the results to get the total future value
    total_future_value = sum(future_values)

    return total_future_value

# Example usage:
if __name__ == "__main__":
  # Calculate the future value of a $1000 investment at 5% interest for 10 years
  fv = future_value(pv=1000, r=0.05, n=10)
  print(f"Future value: ${fv:.2f}")

  # Calculate the present value of $5000 in 5 years at a 3% discount rate
  pv = present_value(fv=5000, r=0.03, n=5)
  print(f"Present value: ${pv:.2f}")

  # Calculate the payment required to reach $100,000 in 20 years at 6% interest
  pmt = payment(pv=0, r=0.06, n=20)
  print(f"Required payment: ${pmt:.2f}")

  # Calculate the future value of an investment with $100 payments for 15 years at 4% interest
  fv_pmt = future_value_with_payment(pmt=100, r=0.04, n=15)
  print(f"Future value with payments: ${fv_pmt:.2f}")

  # Calculate the present value of an investment with $50 payments for 10 years at 2% interest
  pv_pmt = present_value_with_payment(pmt=50, r=0.02, n=10)
  print(f"Present value with payments: ${pv_pmt:.2f}")