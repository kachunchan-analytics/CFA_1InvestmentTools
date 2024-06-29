import numpy as np

def calculate_mwrr(cash_flows):
    """
    Calculates the Money-Weighted Rate of Return (MWRR) for a series of cash flows.

    Args:
        cash_flows (list): A list of cash flows, where positive values represent inflows and negative values represent outflows.

    Returns:
        float: The MWRR as a percentage.
    """
    return np.irr(cash_flows) * 100

if __name__ == "__main__":
    # Example usage
    cash_flows = [-50, 2, 2, 65]  # Initial investment, dividends, and sale proceeds
    mwrr = calculate_mwrr(cash_flows)
    print(f"Money-Weighted Rate of Return (MWRR): {mwrr:.2f}%")