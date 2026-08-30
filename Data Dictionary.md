# Data Dictionary

## Customer Data (customer_data.csv)

| Field Name | Data Type | Description | Values/Notes |
|------------|-----------|-------------|--------------|
| CustomerID | String | Unique identifier for each customer | Format: C001, C002, etc. |
| Age | Integer | Customer age in years | Range: 24-52 |
| Gender | String | Customer gender | Male, Female |
| Income | Integer | Annual income in USD | Range: 43,000-96,000 |
| Education | String | Highest education level | Bachelor, Master, PhD |
| MaritalStatus | String | Marital status | Single, Married, Divorced |
| Children | Integer | Number of children | Range: 0-3 |
| City | String | City of residence | Major US cities |
| CustomerSince | Date | Date when customer first registered | Format: YYYY-MM-DD |
| YearsAsCustomer | Decimal | Number of years as customer | Calculated field, range: 3.9-8.6 |

## Transaction Data (transaction_data.csv)

| Field Name | Data Type | Description | Values/Notes |
|------------|-----------|-------------|--------------|
| TransactionID | String | Unique identifier for each transaction | Format: T001, T002, etc. |
| CustomerID | String | Foreign key to customer data | Links to customer_data.CustomerID |
| TransactionDate | Date | Date of transaction | Format: YYYY-MM-DD |
| ProductID | String | Foreign key to product data | Links to product_data.ProductID |
| Quantity | Integer | Number of units purchased | Range: 1-4 |
| Amount | Decimal | Total transaction amount in USD | Range: 35.00-400.00 |
| ProductCategory | String | Category of product | Electronics, Clothing, Home, Books |
| PaymentMethod | String | Payment method used | Credit Card, Debit Card, PayPal |

## Product Data (product_data.csv)

| Field Name | Data Type | Description | Values/Notes |
|------------|-----------|-------------|--------------|
| ProductID | String | Unique identifier for each product | Format: P001, P002, etc. |
| ProductName | String | Name of the product | Various product names |
| ProductCategory | String | Category of product | Electronics, Clothing, Home, Books |
| UnitPrice | Decimal | Price per unit in USD | Range: 35.00-120.00 |
| Brand | String | Product brand name | TechBrand, FashionCo, HomeStyle, ReadWell, SportMax |

## Data Relationships

```
customer_data (1) ----< (many) transaction_data >---- (1) product_data
     CustomerID                            ProductID
```

## Data Quality Notes

### Completeness
- All fields are populated in the sample data
- No missing values in the dataset
- Consistent formatting across all records

### Consistency
- Customer IDs are unique across the customer table
- Transaction IDs are unique across the transaction table
- Product IDs are unique across the product table
- Foreign key relationships are maintained

### Accuracy
- Age ranges are realistic for the customer base
- Income values are reasonable for the demographics
- Transaction amounts correspond to quantity × unit price
- Dates are within a realistic timeframe (2016-2024)

## Data Limitations

1. **Sample Size:** The dataset contains 50 customers and 137 transactions for demonstration purposes
2. **Time Period:** Customer data spans from 2016-2024, transactions from 2024 only
3. **Geographic Scope:** Limited to major US cities
4. **Product Range:** Limited to 11 products across 4 categories
5. **Demographic Variables:** Limited demographic variables available

## Data Privacy Considerations

- This is sample data created for educational purposes
- No real personally identifiable information (PII) is included
- Customer IDs are anonymized
- Income values are representative, not actual customer data
- Geographic data is at city level only, not specific addresses

## Calculated Fields Recommendations

### Customer-Level Calculations
- **Total Spend:** Sum of all transaction amounts per customer
- **Transaction Count:** Number of transactions per customer
- **Average Order Value:** Total Spend / Transaction Count
- **Purchase Frequency:** Transactions per time period
- **Favorite Category:** Most frequently purchased category
- **Preferred Payment Method:** Most used payment method

### Product-Level Calculations
- **Total Revenue:** Sum of transaction amounts per product
- **Units Sold:** Sum of quantities per product
- **Average Order Quantity:** Average quantity per transaction
- **Customer Count:** Number of unique customers per product

### Time-Based Calculations
- **Monthly Revenue:** Sum of amounts by month
- **Quarterly Trends:** Revenue and transaction patterns by quarter
- **Seasonal Patterns:** Identify peak purchasing periods
- **Growth Rates:** Period-over-period changes

## Data Refresh Considerations

When implementing with real data:
1. **Update Frequency:** Determine how often new transactions are added
2. **Historical Data:** Decide how much historical data to maintain
3. **Customer Updates:** Plan for customer profile changes over time
4. **Product Catalog:** Handle product additions, removals, and price changes
5. **Data Validation:** Implement checks for data quality and consistency