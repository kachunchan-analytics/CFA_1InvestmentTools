from decimal import Decimal, getcontext

getcontext().prec = 6  # Set precision for decimal calculations

def calculate_cost(interest, commitment_fee=0, loan_amount=0, dealer_commission=0, backup_costs=0):
    """
    Calculates the cost of short-term funding based on different scenarios.

    Args:
        interest (Decimal): Interest amount.
        commitment_fee (Decimal, optional): Commitment fee for lines of credit. Defaults to 0.
        loan_amount (Decimal, optional): Total loan amount. Defaults to 0.
        dealer_commission (Decimal, optional): Dealer commission for commercial paper. Defaults to 0.
        backup_costs (Decimal, optional): Backup costs for commercial paper. Defaults to 0.

    Returns:
        Decimal: Calculated cost of borrowing.
    """

    if commitment_fee > 0:
        # Line of credit with commitment fee
        cost = (interest + commitment_fee) / loan_amount
    elif loan_amount > 0:
        # All-inclusive interest rate (e.g., Banker's Acceptances)
        net_proceeds = loan_amount - interest
        cost = interest / net_proceeds
    else:
        # All-inclusive interest rate with additional costs (e.g., Commercial Paper)
        net_proceeds = loan_amount - interest
        cost = (interest + dealer_commission + backup_costs) / net_proceeds

    return cost

# Example usage (for testing within the module)
if __name__ == "__main__":
    interest = Decimal('1000')
    commitment_fee = Decimal('50')
    loan_amount = Decimal('10000')

    cost_line_of_credit = calculate_cost(interest, commitment_fee, loan_amount)
    print(f"Cost of line of credit: {cost_line_of_credit:.2%}")

    interest = Decimal('500')
    loan_amount = Decimal('10000')

    cost_bankers_acceptance = calculate_cost(interest, loan_amount=loan_amount)
    print(f"Cost of Banker's Acceptance: {cost_bankers_acceptance:.2%}")

    interest = Decimal('750')
    dealer_commission = Decimal('25')
    backup_costs = Decimal('10')
    loan_amount = Decimal('15000')

    cost_commercial_paper = calculate_cost(interest, dealer_commission=dealer_commission, backup_costs=backup_costs, loan_amount=loan_amount)
    print(f"Cost of Commercial Paper: {cost_commercial_paper:.2%}")