import numpy as np

def holding_period_return(dividends, selling_price, purchase_price):
    """
    Calculate the holding period return (HPR)
    
    Parameters:
    dividends (float): Total dividends received
    selling_price (float): Selling price of the asset
    purchase_price (float): Purchase price of the asset
    
    Returns:
    float: Holding period return
    """
    return (dividends + selling_price) / purchase_price - 1

def annualized_return(hpr, years):
    """
    Calculate the annualized return
    
    Parameters:
    hpr (float): Holding period return
    years (int): Number of years
    
    Returns:
    float: Annualized return
    """
    return (1 + hpr) ** (1 / years) - 1

def arithmetic_mean_return(returns):
    """
    Calculate the arithmetic mean return
    
    Parameters:
    returns (list): List of periodic returns
    
    Returns:
    float: Arithmetic mean return
    """
    return np.mean(returns)

def geometric_mean_return(returns):
    """
    Calculate the geometric mean return
    
    Parameters:
    returns (list): List of periodic returns
    
    Returns:
    float: Geometric mean return
    """
    product = 1
    for ret in returns:
        product *= (1 + ret)
    return product ** (1 / len(returns)) - 1

def money_weighted_rate_of_return(cash_flows):
    """
    Calculate the money-weighted rate of return (MWRR)
    
    Parameters:
    cash_flows (list): List of cash inflows and outflows
    
    Returns:
    float: Money-weighted rate of return
    """
    # Note: This function assumes that the cash flows are in the correct order
    # (i.e., inflows are positive and outflows are negative)
    # and that the cash flows are equally spaced in time.
    # In practice, you would need to use a more sophisticated method
    # to calculate the MWRR, such as the Newton-Raphson method.
    return np.irr(cash_flows)

def real_return(nominal_return, inflation_rate):
    """
    Calculate the real return
    
    Parameters:
    nominal_return (float): Nominal return
    inflation_rate (float): Inflation rate
    
    Returns:
    float: Real return
    """
    return (1 + nominal_return) / (1 + inflation_rate) - 1

def leveraged_return(nominal_return, debt_ratio, interest_rate):
    """
    Calculate the leveraged return
    
    Parameters:
    nominal_return (float): Nominal return
    debt_ratio (float): Debt ratio (i.e., debt / equity)
    interest_rate (float): Interest rate on debt
    
    Returns:
    float: Leveraged return
    """
    return nominal_return * (1 + debt_ratio) - interest_rate * debt_ratio

if __name__ == "__main__":
    # Example usage:
    dividends = 15
    selling_price = 140
    purchase_price = 100
    years = 3
    
    hpr = holding_period_return(dividends, selling_price, purchase_price)
    annualized_ret = annualized_return(hpr, years)
    print(f"Holding period return: {hpr:.2%}")
    print(f"Annualized return: {annualized_ret:.2%}")
    
    returns = [0.25, -0.0416, 0.318]
    arithmetic_mean = arithmetic_mean_return(returns)
    geometric_mean = geometric_mean_return(returns)
    print(f"Arithmetic mean return: {arithmetic_mean:.2%}")
    print(f"Geometric mean return: {
