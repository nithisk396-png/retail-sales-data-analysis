from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = Path(__file__).with_name("sales_data.csv")
OUTPUT_DIR = Path(__file__).with_name("output")


def load_and_prepare_data():
    """Load sales records and calculate revenue after discounts."""
    df = pd.read_csv(DATA_FILE)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    required_columns = {
        "order_id", "order_date", "product", "category",
        "region", "quantity", "unit_price", "discount_rate"
    }
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df = df.dropna(subset=["order_id", "order_date", "product"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0)]
    df["revenue"] = (
        df["quantity"] * df["unit_price"] * (1 - df["discount_rate"])
    )
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    return df


def print_summary(df):
    total_revenue = df["revenue"].sum()
    total_orders = df["order_id"].nunique()
    average_order_value = total_revenue / total_orders if total_orders else 0

    print("\nRETAIL SALES SUMMARY")
    print("=" * 42)
    print(f"Orders analysed:       {total_orders}")
    print(f"Total revenue:         Rs. {total_revenue:,.2f}")
    print(f"Average order value:   Rs. {average_order_value:,.2f}")

    print("\nRevenue by category:")
    print(df.groupby("category")["revenue"].sum().sort_values(ascending=False).round(2))

    print("\nTop products by revenue:")
    print(df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(5).round(2))

    print("\nRevenue by region:")
    print(df.groupby("region")["revenue"].sum().sort_values(ascending=False).round(2))


def create_charts(df):
    OUTPUT_DIR.mkdir(exist_ok=True)

    monthly = df.groupby("month")["revenue"].sum().sort_index()
    plt.figure(figsize=(10, 5))
    monthly.plot(marker="o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue (Rs.)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
    plt.close()

    category = df.groupby("category")["revenue"].sum().sort_values()
    plt.figure(figsize=(8, 5))
    category.plot(kind="barh")
    plt.title("Revenue by Product Category")
    plt.xlabel("Revenue (Rs.)")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "category_revenue.png", dpi=150)
    plt.close()

    region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    region.plot(kind="bar")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue (Rs.)")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "regional_revenue.png", dpi=150)
    plt.close()


def main():
    try:
        sales = load_and_prepare_data()
    except (OSError, ValueError, KeyError) as error:
        print(f"Unable to analyse the dataset: {error}")
        return

    if sales.empty:
        print("No valid sales records found.")
        return

    print_summary(sales)
    create_charts(sales)
    print(f"\nCharts saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
