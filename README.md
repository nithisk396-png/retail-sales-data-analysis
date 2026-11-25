# Retail Sales Data Analysis

A Python data-analysis project that explores a sample retail sales dataset and produces summary metrics and charts.

## Project goals

- Calculate revenue after discounts
- Compare revenue across product categories and regions
- Identify products contributing the most revenue
- Examine monthly revenue trends
- Practise data cleaning, aggregation and visualization

## Tools used

- Python 3
- Pandas
- Matplotlib
- CSV

## Project structure

```text
retail-sales-data-analysis/
├── main.py
├── sales_data.csv
├── requirements.txt
└── README.md
```

## Run locally

1. Install Python 3.
2. Open a terminal in this project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the analysis:

```bash
python main.py
```

The script prints summary metrics and creates three chart images in an `output/` folder.

## Dataset

`sales_data.csv` contains 60 fictional sample orders. It is synthetic data created for learning and demonstration; it is not real company or customer data.

Columns:
- `order_id`: unique order identifier
- `order_date`: order date
- `product`: product name
- `category`: product category
- `region`: sales region
- `quantity`: units sold
- `unit_price`: price per unit in Indian rupees
- `discount_rate`: discount as a decimal fraction

## Analysis performed

1. Data loading and basic validation
2. Revenue calculation after discounts
3. Revenue aggregation by category, product, region and month
4. Summary metrics including total revenue and average order value
5. Charts for monthly, category and regional revenue

## Limitations

This is a learning project using a small synthetic dataset. The results should not be interpreted as actual business performance.

## Possible improvements

- Add exploratory data analysis in a Jupyter notebook
- Compare units sold as well as revenue
- Add filters for date ranges and regions
- Build an interactive dashboard
- Add automated tests for data validation and calculations
