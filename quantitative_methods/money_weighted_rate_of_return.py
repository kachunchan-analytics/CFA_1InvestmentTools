import numpy as np

def calculate_pv_outflows(cash_flows, irr):
    """
    Calculate the present value of outflows (PVO)
    """
    pv_outflows = 0
    for i, cf in enumerate(cash_flows):
        pv_outflows += cf * (1 + irr) ** i
    return pv_outflows

def calculate_pv_inflows(cash_flows, irr):
    """
    Calculate the present value of inflows (PVI)
    """
    pv_inflows = 0
    for i, cf in enumerate(cash_flows):
        pv_inflows += cf * (1 + irr) ** i
    return pv_inflows

def calculate_mwrr(cash_flows, initial_investment):
    """
    Calculate the Money-Weighted Rate of Return (MWRR)
    """
    irr = 0.0
    while True:
        pv_outflows = calculate_pv_outflows(cash_flows, irr)
        pv_inflows = calculate_pv_inflows(cash_flows, irr)
        if np.isclose(pv_outflows, pv_inflows, atol=1e-6):
            break
        elif pv_outflows > pv_inflows:
            irr += 0.01
        else:
            irr -= 0.01
    return irr

def main():
    # Example usage:
    cash_flows = [-100, 50, 75, 120]  # initial investment, then 3 cash flows
    initial_investment = -100
    mwrr = calculate_mwrr(cash_flows, initial_investment)
    print(f"The Money-Weighted Rate of Return (MWRR) is: {mwrr:.2f}%")

if __name__ == "__main__":
    main()
