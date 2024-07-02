import pandas as pd

def calculate_annuity_pv(pmt, r, n):
  """Calculates the present value of an ordinary annuity.

  Args:
    pmt: The payment amount.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The present value of the annuity.
  """
  return pmt * (1 - (1 + r)**-n) / r

def calculate_annuity_fv(pmt, r, n):
  """Calculates the future value of an ordinary annuity.

  Args:
    pmt: The payment amount.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The future value of the annuity.
  """
  return pmt * ((1 + r)**n - 1) / r

def calculate_annuity_due_pv(pmt, r, n):
  """Calculates the present value of an annuity due.

  Args:
    pmt: The payment amount.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The present value of the annuity due.
  """
  return calculate_annuity_pv(pmt, r, n) * (1 + r)

def calculate_annuity_due_fv(pmt, r, n):
  """Calculates the future value of an annuity due.

  Args:
    pmt: The payment amount.
    r: The interest rate per period.
    n: The number of periods.

  Returns:
    The future value of the annuity due.
  """
  return calculate_annuity_fv(pmt, r, n) * (1 + r)

if __name__ == "__main__":
  # Example usage for testing
  pmt = 100
  r = 0.05
  n = 10
  pv = calculate_annuity_pv(pmt, r, n)
  fv = calculate_annuity_fv(pmt, r, n)
  pv_due = calculate_annuity_due_pv(pmt, r, n)
  fv_due = calculate_annuity_due_fv(pmt, r, n)
  print(f"Present Value of Ordinary Annuity: {pv}")
  print(f"Future Value of Ordinary Annuity: {fv}")
  print(f"Present Value of Annuity Due: {pv_due}")
  print(f"Future Value of Annuity Due: {fv_due}")