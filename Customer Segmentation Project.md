# Customer Segmentation Power BI Report Guide

## Overview
This guide will help you create a comprehensive customer segmentation report using Power BI with the provided sample data.

## Data Files
- `customer_data.csv` - Customer demographic and profile information
- `transaction_data.csv` - Customer purchase transactions
- `product_data.csv` - Product information and pricing

## Step-by-Step Power BI Implementation

### 1. Load Data into Power BI
1. Open Power BI Desktop
2. Click "Get Data" → "Text/CSV"
3. Load the three CSV files from the `data` folder:
   - customer_data.csv
   - transaction_data.csv
   - product_data.csv

### 2. Create Data Relationships
1. Go to "Model View" (left sidebar)
2. Create relationships:
   - `customer_data[CustomerID]` → `transaction_data[CustomerID]` (One-to-Many)
   - `product_data[ProductID]` → `transaction_data[ProductID]` (One-to-Many)

### 3. Create Calculated Columns and Measures

#### Calculated Columns (in Customer Data)
```
# Age Group
Age Group = SWITCH(
    TRUE(),
    customer_data[Age] < 25, "18-24",
    customer_data[Age] < 35, "25-34",
    customer_data[Age] < 45, "35-44",
    customer_data[Age] < 55, "45-54",
    customer_data[Age] >= 55, "55+"
)

# Income Level
Income Level = SWITCH(
    TRUE(),
    customer_data[Income] < 50000, "Low",
    customer_data[Income] < 75000, "Medium",
    customer_data[Income] >= 75000, "High"
)

# Customer Tenure Group
Tenure Group = SWITCH(
    TRUE(),
    customer_data[YearsAsCustomer] < 3, "New (0-3 years)",
    customer_data[YearsAsCustomer] < 6, "Regular (3-6 years)",
    customer_data[YearsAsCustomer] >= 6, "Loyal (6+ years)"
)
```

#### Key Measures
```
# Total Revenue
Total Revenue = SUM(transaction_data[Amount])

# Total Transactions
Total Transactions = COUNTROWS(transaction_data)

# Average Order Value
Average Order Value = DIVIDE([Total Revenue], [Total Transactions])

# Customer Count
Customer Count = DISTINCTCOUNT(customer_data[CustomerID])

# Revenue per Customer
Revenue per Customer = DIVIDE([Total Revenue], [Customer Count])

# Total Quantity Sold
Total Quantity = SUM(transaction_data[Quantity])

# Average Purchase Frequency
Purchase Frequency = DIVIDE([Total Transactions], [Customer Count])

# Customer Lifetime Value (CLV)
CLV = [Revenue per Customer] * AVERAGE(customer_data[YearsAsCustomer])

# High Value Customers (Revenue > $500)
High Value Customers = CALCULATE(
    [Customer Count],
    FILTER(
        VALUES(customer_data[CustomerID]),
        CALCULATE([Total Revenue], ALLEXCEPT(customer_data, customer_data[CustomerID])) > 500
    )
)

# Product Category Revenue
Category Revenue = SUM(transaction_data[Amount])
```

### 4. Create the Report Pages

#### Page 1: Customer Overview Dashboard
**Visualizations:**
1. **Customer Count Card** - Display total number of customers
2. **Total Revenue Card** - Display total revenue
3. **Average Order Value Card** - Display average order value
4. **Customers by Age Group** - Donut chart
5. **Customers by Income Level** - Column chart
6. **Customers by Education Level** - Pie chart
7. **Customer Tenure Distribution** - Funnel chart
8. **Customers by City** - Map visualization (if coordinates available) or Bar chart

#### Page 2: Purchase Behavior Analysis
**Visualizations:**
1. **Revenue by Product Category** - Stacked column chart
2. **Payment Method Distribution** - Donut chart
3. **Monthly Sales Trend** - Line chart with TransactionDate on axis
4. **Top 10 Products by Revenue** - Bar chart
5. **Average Order Value by Product Category** - Card or small chart
6. **Quantity Sold by Category** - Treemap

#### Page 3: Customer Segmentation
**Visualizations:**
1. **Customer Segments Matrix** - Matrix showing segments by Age Group, Income Level, and Education
2. **Revenue by Customer Segment** - Clustered bar chart
3. **High Value Customers by Segment** - Bar chart
4. **Customer Tenure vs Revenue** - Scatter plot
5. **Purchase Frequency by Segment** - Column chart
6. **Segment Performance Summary** - Table with key metrics per segment

#### Page 4: Geographic Analysis
**Visualizations:**
1. **Revenue by City** - Bar chart
2. **Customer Count by City** - Column chart
3. **Average Order Value by City** - Card or small chart
4. **Popular Products by City** - Matrix visualization
5. **Customer Distribution Map** - Filled map (if using location data)

#### Page 5: RFM Analysis (Recency, Frequency, Monetary)
**Create RFM Scores:**
```
# Recency Score (days since last purchase)
Recency = DATEDIFF(
    MAX(transaction_data[TransactionDate]),
    TODAY(),
    DAY
)

# Frequency Score (number of transactions)
Frequency = COUNTROWS(transaction_data)

# Monetary Score (total spent)
Monetary = SUM(transaction_data[Amount])

# RFM Segment
RFM Segment = SWITCH(
    TRUE(),
    [Recency] <= 30 && [Frequency] >= 5 && [Monetary] >= 500, "Champions",
    [Recency] <= 60 && [Frequency] >= 3 && [Monetary] >= 300, "Loyal Customers",
    [Recency] <= 90 && [Frequency] >= 2 && [Monetary] >= 200, "Potential Loyalists",
    [Recency] <= 120 && [Frequency] >= 1, "New Customers",
    [Recency] > 120 && [Frequency] >= 2, "At Risk",
    [Recency] > 180, "Lost"
)
```

**Visualizations:**
1. **RFM Segment Distribution** - Donut chart
2. **Customer Count by RFM Segment** - Column chart
3. **Revenue by RFM Segment** - Bar chart
4. **RFM Matrix** - Scatter plot (Frequency vs Monetary with Recency as color)
5. **Segment Transition Flow** - Sankey diagram (if using custom visuals)

### 5. Apply Formatting and Styling
1. Choose a professional color scheme (e.g., corporate blues and grays)
2. Add consistent titles and subtitles
3. Apply data labels where appropriate
4. Add tooltips for additional context
5. Use consistent fonts and sizes
6. Add filters to each page:
   - Age Group slicer
   - Income Level slicer
   - Education Level slicer
   - Product Category slicer
   - Date range slicer

### 6. Create Interactive Features
1. Add drill-down capabilities on charts
2. Create bookmarks for different views
3. Add buttons for navigation between pages
4. Implement cross-filtering between visualizations
5. Add tooltips with customer details

### 7. Advanced Analytics (Optional)
1. **Customer Clustering using Python in Power BI:**
   - Enable Python scripting in Power BI options
   - Use scikit-learn for K-means clustering
   - Create clusters based on Age, Income, and Purchase behavior

2. **Predictive Analytics:**
   - Create forecast for future revenue
   - Predict customer churn probability
   - Forecast next purchase date

### 8. Final Review and Export
1. Review all visualizations for accuracy
2. Test all filters and interactions
3. Ensure data refresh is configured
4. Add documentation in the report
5. Export as PBIX file
6. Publish to Power BI Service (optional)

## Key Insights to Highlight
1. **High-Value Segments:** Identify which customer segments generate the most revenue
2. **Growth Opportunities:** Find underperforming segments with potential
3. **Product Preferences:** Understand which products appeal to different segments
4. **Geographic Patterns:** Identify regional differences in customer behavior
5. **Purchase Patterns:** Analyze seasonal trends and purchase frequency
6. **Retention Analysis:** Evaluate customer loyalty and tenure impact

## Data Refresh Schedule
- Set up automatic data refresh if using Power BI Service
- Schedule daily/weekly refresh based on data update frequency
- Configure data source credentials for refresh

## Tips for Effective Segmentation
1. Start with basic demographic segmentation
2. Add behavioral data for more sophisticated segments
3. Use RFM analysis for value-based segmentation
4. Validate segments with business stakeholders
5. Create targeted marketing strategies for each segment
6. Monitor segment performance over time