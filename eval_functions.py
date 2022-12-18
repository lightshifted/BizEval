def return_on_investment(net_profit, initial_investment):
    """Calculates the return on investment of a business.

    Args:
    net_profit: The net profit of the business.
    initial_investment: The initial investment in the business.

    Returns:
    The return on investment of the business.
    """
    # Calculate the return on investment by dividing the net profit by the initial investment
    return_on_investment = net_profit / initial_investment

    return return_on_investment


def calc_npv(investment, discount_rate, cash_flows):
    """
    Calculates the net present value of an investment.

    Parameters:
    investment (float): The initial investment amount.
    discount_rate (float): The discount rate used to calculate the present value of the cash flows.
    cash_flows (list of floats): A list of the cash flows expected from the investment.

    Returns:
    float: The net present value of the investment.
    """
    npv = 0
    for i, cash_flow in enumerate(cash_flows):
        npv += cash_flow / (1 + discount_rate)**i
    npv -= investment
    return npv


def payback_period(initial_investment, annual_cash_flow):
    """Calculates the payback period in years for a given initial investment and annual cash flow.

    Args:
    initial_investment (float): The initial amount invested in the project or investment.
    annual_cash_flow (float): The expected annual cash flow from the project or investment.

    Returns:
    float: The payback period in years.
    """
    # Calculate the payback period by dividing the initial investment by the annual cash flow
    payback_period = initial_investment / annual_cash_flow

    # Return the payback period
    return payback_period


def break_even_point(fixed_costs, price, variable_costs):
    """Calculates the break-even point for a business.

    Args:
    fixed_costs: The total fixed costs of the business.
    price: The price of each unit sold.
    variable_costs: The variable costs per unit.

    Returns:
    The number of units that need to be sold to break even.
    """
    # Calculate the total costs per unit by adding the fixed and variable costs
    total_costs = fixed_costs + variable_costs

    # Calculate the break-even point by dividing the total fixed costs by the difference between the price and the total costs per unit
    break_even_point = fixed_costs / (price - total_costs)

    return break_even_point

def debt_to_equity_ratio(total_debt, total_equity):
    """Calculates the debt-to-equity ratio of a business.

    Args:
    total_debt: The total debt of the business.
    total_equity: The total equity of the business.

    Returns:
    The debt-to-equity ratio of the business.
    """
    # Calculate the debt-to-equity ratio by dividing the total debt by the total equity
    debt_to_equity_ratio = total_debt / total_equity

    return debt_to_equity_ratio


def operating_profit_margin(revenue, operating_expenses):
    """Calculates the operating profit margin of a business.

    Args:
    revenue: The total revenue of the business.
    operating_expenses: The total operating expenses of the business.

    Returns:
    The operating profit margin of the business.
    """
    # Calculate the operating profit by subtracting the operating expenses from the revenue
    operating_profit = revenue - operating_expenses

    # Calculate the operating profit margin by dividing the operating profit by the revenue
    operating_profit_margin = operating_profit / revenue

    return operating_profit_margin


def operating_profit_margin(revenue, operating_expenses):
    """Calculates the operating profit margin of a business.

    Args:
    revenue: The total revenue of the business.
    operating_expenses: The total operating expenses of the business.

    Returns:
    The operating profit margin of the business.
    """
    # Calculate the operating profit by subtracting the operating expenses from the revenue
    operating_profit = revenue - operating_expenses

    # Calculate the operating profit margin by dividing the operating profit by the revenue
    operating_profit_margin = operating_profit / revenue

    return operating_profit_margin


def ebitda(revenue, costs, interest, taxes, depreciation, amortization):
    """Calculates the EBITDA of a business.

    Args:
    revenue: The total revenue of the business.
    costs: The total costs of the business.
    interest: The total interest expense of the business.
    taxes: The total taxes paid by the business.
    depreciation: The total depreciation expense of the business.
    amortization: The total amortization expense of the business.

    Returns:
    The EBITDA of the business.
    """
    # Calculate the EBITDA by subtracting costs, interest, taxes, depreciation, and amortization from revenue
    ebitda = revenue - costs - interest - taxes - depreciation - amortization

    return ebitda


def operating_pe_ratio(market_value, operating_income):
    """Calculates the operating P/E ratio of a business.

    Args:
    market_value: The market value of the business.
    operating_income: The operating income of the business.

    Returns:
    The operating P/E ratio of the business.
    """
    # Calculate the operating P/E ratio by dividing the market value by the operating income
    operating_pe_ratio = market_value / operating_income

    return operating_pe_ratio
