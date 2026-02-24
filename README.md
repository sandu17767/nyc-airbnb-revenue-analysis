# 🏙 NYC Airbnb Revenue & Market Analysis (2019)

## 🧾 Executive Summary

- Manhattan generates the highest median revenue ($33,682), primarily driven by premium pricing.
- Brooklyn achieves slightly higher occupancy (337 median booked nights) but relies on lower pricing ($90 median).
- Queens offers lower competition (5,656 listings) with moderate revenue potential.
- 86% of hosts own only one listing, but 32% of Manhattan listings are controlled by multi-listing hosts.
- Revenue distribution is right-skewed, making median values more reliable than mean.
- Investment decisions depend on pricing strategy, occupancy model, and competitive intensity.

---

## 🎯 Business Problem

This project analyses the New York City Airbnb market from an investment and revenue perspective.

The objective was to determine:

- Which borough generates the strongest revenue performance?
- Is revenue driven by pricing or occupancy?
- How competitive is each borough?
- Is the market dominated by professional operators?

The goal is to provide data-driven insight for potential investors entering the NYC short-term rental market.

---

## 📂 Dataset Overview

- Source: NYC Airbnb Open Data (2019)
- Total Listings After Cleaning: **48,645**
- Boroughs Included:
  - Manhattan
  - Brooklyn
  - Queens
  - Bronx
  - Staten Island

---

## 🧹 Data Cleaning

To ensure accurate revenue modelling:

- Removed 11 listings with `price = 0`
- Removed 239 extreme outliers (`price > $1000`)
- Replaced `reviews_per_month` NaN with 0 (structural zeros)
- Retained `last_review` NaN as true missing values

This prevented revenue distortion and ensured realistic market representation.

---

## 🧠 Feature Engineering

### 1️⃣ Demand Proxy (Booked Nights)

```python
booked_nights = 365 - availability_365
```

Unavailable days were assumed to approximate booked days.

---

### 2️⃣ Estimated Annual Revenue

```python
estimated_revenue = price * booked_nights
```

Revenue statistics:

- Mean Revenue: $33,880
- Median Revenue: $25,550
- Max Revenue: $365,000

Since mean > median, revenue distribution is right-skewed.
Median values were used for borough comparison.

---

## 🗺 Borough-Level Revenue Analysis

### 💰 Median Revenue by Borough

| Borough         | Median Revenue |
|----------------|---------------|
| Manhattan      | $33,682 |
| Brooklyn       | $23,500 |
| Queens         | $16,160 |
| Bronx          | $11,780 |
| Staten Island  | $10,212 |

Manhattan leads in revenue performance.

---

## 💵 Pricing Strategy Comparison

### Median Price per Night

| Borough        | Median Price |
|---------------|--------------|
| Manhattan     | $149 |
| Brooklyn      | $90 |
| Queens        | $75 |
| Bronx         | $65 |

Manhattan’s revenue advantage is driven primarily by premium pricing.

---

## 📈 Occupancy Comparison

### Median Booked Nights

| Borough        | Median Booked Nights |
|---------------|---------------------|
| Brooklyn      | 337 |
| Manhattan     | 329 |
| Queens        | 268 |
| Bronx         | 217 |
| Staten Island | 146 |

Brooklyn slightly exceeds Manhattan in occupancy, indicating a volume-driven model.

---

## 🏗 Market Concentration Analysis

Host ownership structure:

- 37,283 unique hosts
- 86% own only one listing
- Manhattan mean listings per host: **12.85**
- 32% of Manhattan listings controlled by multi-listing hosts

This indicates stronger professional presence in Manhattan compared to other boroughs.

---

## 📊 Key Strategic Insights

### 🏙 Manhattan
- Premium pricing model
- Highest revenue performance
- Higher professional concentration
- Highly competitive market

### 🌉 Brooklyn
- Occupancy-driven revenue
- Moderate pricing
- More evenly distributed host ownership

### 🌆 Queens
- Lower competition
- Lower pricing
- Entry opportunity for smaller investors

---

## 🛠 Tools & Skills Demonstrated

- Python (Pandas)
- Data Cleaning & Outlier Handling
- Feature Engineering
- Revenue Modelling
- Distribution Analysis (Mean vs Median)
- Geographic Segmentation
- Market Concentration Analysis
- Business Interpretation & Insight Generation

---

## 📌 Conclusion

Revenue performance varies significantly across NYC boroughs.

- Manhattan monetises through pricing power.
- Brooklyn monetises through occupancy volume.
- Queens offers lower competitive pressure.

Optimal investment decisions depend on investor capital, risk tolerance, and strategic positioning.

