def calculate_perpetuity_pv(pmt, r):
  """Calculates the present value of a perpetuity.

  Args:
    pmt: The payment amount.
    r: The interest rate per period.

  Returns:
    The present value of the perpetuity.
  """
  return pmt / r

def calculate_growing_perpetuity_pv(pmt, r, g):
  """Calculates the present value of a growing perpetuity.

  Args:
    pmt: The payment amount.
    r: The interest rate per period.
    g: The growth rate of the payments.

  Returns:
    The present value of the growing perpetuity.
  """
  return pmt / (r - g)

if __name__ == "__main__":
  # Example usage for testing
  pmt = 100
  r = 0.05
  g = 0.02
  pv = calculate_perpetuity_pv(pmt, r)
  pv_growing = calculate_growing_perpetuity_pv(pmt, r, g)
  print(f"Present Value of Perpetuity: {pv}")
  print(f"Present Value of Growing Perpetuity: {pv_growing}")