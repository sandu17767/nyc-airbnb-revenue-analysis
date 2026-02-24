# ================================
# NYC Airbnb Revenue Analysis
# ================================

# 1. Import Libraries
import pandas as pd
import numpy as np

# 2. Load Dataset
df = pd.read_csv("AB_NYC_2019.csv")

# =====================================
# 3. Data Cleaning
# =====================================

# Remove invalid zero prices
df = df[df["price"] > 0]

# Remove extreme luxury outliers (price > 1000)
df = df[df["price"] <= 1000]

# Replace structural missing values
df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

# =====================================
# 4. Feature Engineering
# =====================================

# Demand proxy: booked nights
df["booked_nights"] = 365 - df["availability_365"]

# Revenue modelling
df["estimated_revenue"] = df["price"] * df["booked_nights"]

# =====================================
# 5. Revenue Distribution Summary
# =====================================

revenue_summary = df["estimated_revenue"].describe()

# =====================================
# 6. Borough-Level Analysis
# =====================================

# Median revenue by borough
median_revenue = (
    df.groupby("neighbourhood_group")["estimated_revenue"]
    .median()
    .sort_values(ascending=False)
)

# Mean revenue by borough
mean_revenue = (
    df.groupby("neighbourhood_group")["estimated_revenue"]
    .mean()
    .sort_values(ascending=False)
)

# Median price by borough
median_price = (
    df.groupby("neighbourhood_group")["price"]
    .median()
    .sort_values(ascending=False)
)

# Median booked nights by borough
median_booked_nights = (
    df.groupby("neighbourhood_group")["booked_nights"]
    .median()
    .sort_values(ascending=False)
)

# =====================================
# 7. Market Concentration Analysis
# =====================================

# Listings per host
host_counts = df["host_id"].value_counts()

# Map listing count back to dataframe
df["host_listing_count"] = df["host_id"].map(host_counts)

# Percentage of single-listing hosts
single_listing_hosts = (host_counts == 1).sum()
total_hosts = host_counts.shape[0]
single_listing_percentage = (single_listing_hosts / total_hosts) * 100

# Manhattan concentration
manhattan_df = df[df["neighbourhood_group"] == "Manhattan"]

manhattan_multi = manhattan_df[
    manhattan_df["host_listing_count"] > 1
].shape[0]

manhattan_total = manhattan_df.shape[0]

manhattan_multi_percentage = (
    manhattan_multi / manhattan_total
) * 100

# =====================================
# 8. Output Key Metrics
# =====================================

print("Revenue Summary:")
print(revenue_summary)

print("\nMedian Revenue by Borough:")
print(median_revenue)

print("\nMedian Price by Borough:")
print(median_price)

print("\nMedian Booked Nights by Borough:")
print(median_booked_nights)

print("\nSingle Listing Host Percentage:")
print(single_listing_percentage)

print("\nManhattan Multi-Listing Percentage:")
print(manhattan_multi_percentage)
