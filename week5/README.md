Token Economics Budget Calculator

This project estimates the cost and capacity of an AI feature before you build it. You give your expected usage and limits, and it tells you if the plan fits your budget.

What It Calculates
Input, output and total tokens per day
Estimated cost per day and per month
Peak requests per minute (RPM) and peak tokens per minute (TPM), with a safety margin added
Whether your plan passes four checks: RPM limit, TPM limit, daily budget and monthly budget
Files
budget.py: the main program
test_budget.py: simple tests
requirements_6ee100.txt: list of packages to install
Setup

Step 1: Install the package

pip install -r requirements_6ee100.txt

Step 2: Create a file named .env and add your numbers. Here is an example:

REQUESTS_PER_DAY=1000
AVG_INPUT_TOKENS=1000
AVG_OUTPUT_TOKENS=500
PEAK_REQUESTS_PER_MINUTE=10
INPUT_PRICE_PER_MILLION=1.0
OUTPUT_PRICE_PER_MILLION=2.0
RPM_LIMIT=100
TPM_LIMIT=50000
MONTHLY_BUDGET_USD=100
DAILY_BUDGET_USD=5
SAFETY_MARGIN_PERCENT=20

What Each Setting Means
REQUESTS_PER_DAY: how many requests you expect each day
AVG_INPUT_TOKENS: average tokens you send in one request
AVG_OUTPUT_TOKENS: average tokens the AI returns in one request
PEAK_REQUESTS_PER_MINUTE: the most requests you expect in one minute
INPUT_PRICE_PER_MILLION: price in USD for one million input tokens
OUTPUT_PRICE_PER_MILLION: price in USD for one million output tokens
RPM_LIMIT: the requests per minute your provider allows
TPM_LIMIT: the tokens per minute your provider allows
MONTHLY_BUDGET_USD: the most you want to spend in a month
DAILY_BUDGET_USD: the most you want to spend in a day
SAFETY_MARGIN_PERCENT: extra space added for safety (default is 20)

If you leave a setting out, it is treated as 0, except the safety margin, which is 20.

Run

python budget.py

What You Will See

The program prints a report with the token counts, the daily and monthly cost, and the peak RPM and TPM. Then it shows four checks:

RPM capacity
TPM capacity
Daily budget
Monthly budget

Each check shows PASS or REVIEW. If all four pass, you will see "WITHIN configured planning limits." If not, you will see "REVISE assumptions, limits, or design before build."

How It Works
Daily cost = (input tokens per day x input price + output tokens per day x output price) / 1,000,000
Monthly cost = daily cost x 30
The safety margin makes the numbers a little higher, so you have some extra room.
Negative numbers are not allowed and will show an error.
Run the Tests

python -m unittest test_budget.py
