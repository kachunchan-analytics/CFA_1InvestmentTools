import numpy as np

def calculate_future_value(principal, dividend, interest_rate, periods, payment_frequency):
    """
    Calculate the future value of an investment with regular dividends.

    Parameters:
    principal (float): The initial investment amount.
    dividend (float): The regular dividend payment.
    interest_rate (float): The interest rate per period.
    periods (int): The number of periods.
    payment_frequency (str): The frequency of dividend payments, either 'begin' or 'end'.

    Returns:
    float: The future value of the investment.
    """
    if payment_frequency == 'begin':
        # Calculate future value with dividend payments at the beginning of each period
        future_value = principal * (1 + interest_rate) ** periods + dividend * (((1 + interest_rate) ** periods - 1) / interest_rate) * (1 + interest_rate)
    elif payment_frequency == 'end':
        # Calculate future value with dividend payments at the end of each period
        future_value = principal * (1 + interest_rate) ** periods + dividend * (((1 + interest_rate) ** periods - 1) / interest_rate)
    else:
        raise ValueError("Invalid payment frequency. Please use 'begin' or 'end'.")

    return future_value

def main():
    # Example usage:
    principal = 1000
    dividend = 30
    interest_rate = 0.06
    periods = 5

    # Calculate future value with dividend payments at the beginning of each period
    future_value_begin = calculate_future_value(principal, dividend, interest_rate, periods, 'begin')

    # Calculate future value with dividend payments at the end of each period
    future_value_end = calculate_future_value(principal, dividend, interest_rate, periods, 'end')

    print("Future Value (Dividend at Beginning):", future_value_begin)
    print("Future Value (Dividend at End):", future_value_end)

if __name__ == "__main__":
    main()
