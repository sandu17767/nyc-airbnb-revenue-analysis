# 📊 Revenue Concentration & Distribution Analysis

## 🎯 Objective

To evaluate structural revenue dependency across NYC Airbnb hosts and assess marketplace concentration risk.

---

## 🧠 Methodology

### 1️⃣ Host-Level Revenue Aggregation  

Revenue was aggregated at the host level by summing listing-level earnings:

Revenue per host = Sum(price × booked nights)

Each host is treated as a single economic unit.

---

### 2️⃣ Lorenz Curve

The Lorenz Curve plots:

- X-axis → Cumulative % of Hosts (sorted from lowest to highest revenue)  
- Y-axis → Cumulative % of Total Revenue  

Under perfect equality, the curve would follow the 45° equality line.

![Lorenz Curve](lorenz_curve.png)

The deviation from the equality line indicates revenue concentration across hosts.

---

### 3️⃣ Gini Coefficient

The Gini coefficient was computed using numerical integration:

Gini = 1 − 2 × (Area under Lorenz curve)

Result:

**Gini ≈ 0.45**

This indicates **moderate revenue concentration**, meaning higher-performing hosts contribute disproportionately more revenue, though the marketplace is not dominated by a single extreme group.

---

### 4️⃣ Revenue Distribution Structure

To better understand structural behavior, revenue was log-transformed.

![Log Revenue Distribution](log_revenue_distribution.png)

The distribution reveals a right-skewed (heavy-tailed) structure:

- The majority of hosts generate relatively modest revenue  
- A smaller subset generates significantly higher revenue  

The log transformation suggests the revenue distribution approximates a **log-normal pattern**, commonly observed in platform marketplaces.

---

## 🔍 Key Findings

- Top ~20% of hosts generate ~50% of total revenue  
- Revenue concentration exists but is not extreme  
- Marketplace dependency on high-performing hosts is moderate  
- Structural revenue pattern follows heavy-tail behavior  

---

## 💼 Business Implications

- The platform carries moderate exposure to top-host attrition risk  
- Strategic opportunity exists to uplift mid-tier hosts  
- Revenue structure reflects typical marketplace ecosystem dynamics  
