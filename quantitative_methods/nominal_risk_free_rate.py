def calculate_total_interest_rate(risk_free_rate, inflation_premium, default_risk_premium, liquidity_premium, maturity_premium):
  """
  Calculates the total interest rate based on various premiums.

  Args:
    risk_free_rate: The risk-free rate of return.
    inflation_premium: The premium charged to compensate for inflation.
    default_risk_premium: The premium charged to compensate for default risk.
    liquidity_premium: The premium charged to compensate for liquidity risk.
    maturity_premium: The premium charged to compensate for maturity risk.

  Returns:
    The total interest rate.
  """
  total_interest_rate = risk_free_rate + inflation_premium + default_risk_premium + liquidity_premium + maturity_premium
  return total_interest_rate

def calculate_nominal_risk_free_rate(real_risk_free_rate, inflation_premium):
  """
  Calculates the nominal risk-free rate based on the real risk-free rate and inflation premium.

  Args:
    real_risk_free_rate: The real risk-free rate of return.
    inflation_premium: The premium charged to compensate for inflation.

  Returns:
    The nominal risk-free rate.
  """
  nominal_risk_free_rate = (1 + real_risk_free_rate) * (1 + inflation_premium) - 1
  return nominal_risk_free_rate

if __name__ == "__main__":
  # Example usage:
  risk_free_rate = 0.02
  inflation_premium = 0.03
  default_risk_premium = 0.01
  liquidity_premium = 0.005
  maturity_premium = 0.008

  total_interest_rate = calculate_total_interest_rate(risk_free_rate, inflation_premium, default_risk_premium, liquidity_premium, maturity_premium)
  print(f"Total Interest Rate: {total_interest_rate:.2f}")

  real_risk_free_rate = 0.01
  nominal_risk_free_rate = calculate_nominal_risk_free_rate(real_risk_free_rate, inflation_premium)
  print(f"Nominal Risk-Free Rate: {nominal_risk_free_rate:.2f}")