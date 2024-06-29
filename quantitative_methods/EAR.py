def calculate_effective_annual_rate(nominal_rate, compounding_periods):
  """
  Calculates the effective annual rate (EAR) given a nominal interest rate and 
  the number of compounding periods per year.

  Args:
    nominal_rate: The nominal annual interest rate as a decimal (e.g., 0.05 for 5%).
    compounding_periods: The number of times interest is compounded per year.

  Returns:
    The effective annual rate as a decimal.
  """
  return (1 + (nominal_rate / compounding_periods)) ** compounding_periods - 1

if __name__ == "__main__":
  # Example usage:
  piggy_bank_nominal_rate = 0.0495
  piggy_bank_compounding_periods = 12  # Monthly compounding
  piggy_bank_ear = calculate_effective_annual_rate(piggy_bank_nominal_rate, piggy_bank_compounding_periods)

  porky_bank_nominal_rate = 0.05
  porky_bank_compounding_periods = 2  # Semi-annual compounding
  porky_bank_ear = calculate_effective_annual_rate(porky_bank_nominal_rate, porky_bank_compounding_periods)

  print("Piggy Bank EAR:", piggy_bank_ear * 100, "%")
  print("Porky Bank EAR:", porky_bank_ear * 100, "%")