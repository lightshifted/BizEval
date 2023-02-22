<div>
  <h1 align="center">Business Evaluation</h1>
<div/>
<p>A simple Python class containing methods for computing financial equations used by business for assessing financial decisions<p/>

## Return on Investment(ROI)

This equation measures the profitability of an investment by dividing the net profit by the initial investment. It is a useful tool for comparing different investment options and deciding which is the most profitable.

For example, given a net profit of \$10,000 and an initial investment of \$50,000, the return on investment would be:

```python
net_profit = 10000
initial_investment = 50000
return_on_investment(net_profit, initial_investment)
```

## Net Present Value (NPV)

This equation can be used to compare different investments or projects, taking into account the time value of money. A startup might use NPV to decide between investing in a new product line or expanding into a new market.

For example, suppose a startup is considering an investment that requires an initial investment of $100,000 and is expected to generate cash flows of \$50,000 in year 1, \$60,000 in year 2, and \$70,000 in year 3. If the discount rate is 10%, the NPV of the investment can be calculated as follows:

```python
investment = 100000
discount_rate = 0.1
cash_flows = [50000, 60000, 70000]
npv = calc_npv(investment, discount_rate, cash_flows)
print(npv)
```

## Payback Period

This equation can be used to measures the amount of time it will take to recover the initial investment in a project. It is often used to evaluate the risk of an investment and determine whether it is a good financial decision.

For example, if a startup has an initial investment of \$50,000 and expects an annual cash flow of \$10,000, the payback period would be:

```python
payback_period = payback_period(50000, 10000)
print(payback_period)  # Output: 5.0
```

## Break-Even Point

This equation calculates the point at which the revenue from a project equals the costs of the project. It is useful for determining when a project will start to generate a profit.

For example, if a startup has a total fixed cost of \$10,000, where each unit product sells for \$50, and the variable cost per unit time is \$20, the break-even point would be:

```python
fixed_costs = 10000
price = 50
variable_costs =  20

break_even_point(fixed_costs, price, variable_costs)
```

## Debt-to-Equity Ratio

This equation compares a company's total debt to its total equity. It is used to evaluate a company's financial stability and determine the relative proportion of debt and equity financing.

```python
total_debt = 100000
total_equity = 200000
debt_to_equity_ratio(total_debt, total_equity)
```

## Gross Profit Margin

This equation calculates the percentage of each sale that is profit after subtracting the cost of goods sold. It is useful for evaluating the profitability of a business and comparing it to industry benchmarks.

## Operating Profit Margin

This equation calculates the percentage of each sale that is profit after subtracting all operating expenses, including cost of goods sold and general and administrative expenses. It is useful for evaluating the efficiency of a business's operations.

## Earnings Before Interest and Taxes (EBIT)

This equation calculates the profit of a business before deducting interest and taxes. It is useful for evaluating the profitability of a business without considering financing costs or tax implications.

## Earnings Before Interest, Taxes, Depreciations, and Amortization (EBITDA)

This equation calculates the profit of a business before deducting interest, taxes, depreciation, and amortization. It is useful for evaluating the cash flow of a business and comparing it to industry benchmarks.

## Price-to-Earnings Ratio (P/E Ratio)

This equation calculates the market value of a company's stock relative to its earnings per share. It is used to evaluate the relative value of a company's stock and compare it to industry benchmarks.

## Example

Here is a scenario where a new startup specializing in speech-to-text translations might use all five of the financial equations:

1. Return on Investment (ROI): The startup might use ROI to evaluate the profitability of different marketing campaigns or new product launches. For example, the company might compare the ROI of a social media marketing campaign to the ROI of a paid search campaign to decide which is the more profitable option.
2. Net Present Value (NPV): The startup might use NPV to compare the potential returns of different investment opportunities. For example, the company might use NPV to decide whether to invest in a new software development project or a hardware upgrade.
3. Payback Period: The startup might use payback period to evaluate the risk of different investments or projects. For example, the company might use payback period to decide between two different strategies for expanding into a new market, one with a shorter payback period and lower risk, and one with a longer payback period but higher potential returns.
4. Break-Even Point: The startup might use break-even analysis to determine the number of units that need to be sold in order to recoup the costs of producing a new product. For example, the company might use break-even analysis to determine the minimum number of units that need to be sold in order to break even on the development and production costs of a new speech-to-text software.
5. Debt-to-Equity Ratio: The startup might use this equation to evaluate its financial stability and determine the appropriate mix of debt and equity financing. For example, the company might use debt-to-equity ratio to decide whether to take on additional debt or seek additional equity financing in order to fund a new product launch.
