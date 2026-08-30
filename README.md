# 🎯 Customer Segmentation Project

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-009639?style=for-the-badge)
![Business Intelligence](https://img.shields.io/badge/Business%20Intelligence-0078D4?style=for-the-badge)

A comprehensive customer segmentation analysis project using **Power BI** to analyze customer behavior, demographics, and purchase patterns for targeted marketing and business intelligence.

## 📊 Project Overview

This project demonstrates customer segmentation techniques using real-world data analysis approaches with **Power BI** for interactive dashboards and business intelligence.

### 🎯 Key Achievements
- ✅ **50 Customers** analyzed with demographic and behavioral data
- ✅ **137 Transactions** processed for purchase pattern analysis
- ✅ **4 Product Categories** across 11 products for preference analysis
- ✅ **Interactive Power BI Dashboard** with real-time visualizations
- ✅ **Demographic Segmentation** by age, income, education, and location
- ✅ **Customer Analytics** with key business metrics

## 🚀 Key Features

- **👥 Demographic Segmentation**: Age, income, education, and geographic analysis
- **🛒 Behavioral Segmentation**: Purchase patterns, frequency, and preferences
- **💰 RFM Analysis**: Recency, Frequency, Monetary value-based segmentation
- **📈 Interactive Dashboards**: Power BI visualizations and reports
- **🎯 Customer Analytics**: Key business metrics and KPIs
- **📊 Data Visualization**: Comprehensive charts and graphs

## 📸 Dashboard Preview

### Power BI Dashboard
![Power BI Dashboard](https://via.placeholder.com/800x400?text=Power+BI+Dashboard+Screenshot)

*Customer segmentation dashboard showing age distribution, revenue metrics, and demographic analysis*

## Project Structure

```
Customer Segmentation Project/
├── data/
│   ├── customer_data.csv          # Customer demographic information
│   ├── transaction_data.csv      # Purchase transaction records
│   └── product_data.csv           # Product catalog and pricing
├── powerbi/
│   └── Power BI Report Guide.md   # Step-by-step Power BI implementation
├── documentation/
│   ├── Data Dictionary.md         # Complete data documentation
│   └── Segmentation Methodology.md # Detailed segmentation approaches
└── README.md                      # This file
```

## 🚀 Getting Started

### 📊 Power BI Implementation

**Prerequisites:**
- Power BI Desktop (free download from Microsoft)

**Quick Start:**
1. **Download Power BI Desktop**: https://www.microsoft.com/en-us/power-platform/products/power-bi-desktop
2. **Open Power BI Desktop** and load the CSV files from the `data/` folder:
   - `customer_data.csv`
   - `transaction_data.csv`
   - `product_data.csv`
3. **Create data relationships** in Model View:
   - `customer_data[CustomerID]` → `transaction_data[CustomerID]`
   - `product_data[ProductID]` → `transaction_data[ProductID]`
4. **Build your dashboard** using the guide in `powerbi/Power BI Report Guide.md`

**Sample Dashboard Created:**
- Total Customers: 50
- Total Revenue: $19,000+
- Age distribution analysis
- Demographic segmentation charts

## Data Description

### Customer Data (50 customers)
- **Demographics**: Age (24-52), Gender, Income ($43K-$96K), Education, Marital Status
- **Geographic**: 10 major US cities
- **Customer Tenure**: 3.9-8.6 years as customer
- **Fields**: CustomerID, Age, Gender, Income, Education, MaritalStatus, Children, City, CustomerSince, YearsAsCustomer

### Transaction Data (137 transactions)
- **Purchase History**: Q1 2024 transactions with dates and amounts
- **Product Categories**: Electronics, Clothing, Home, Books
- **Payment Methods**: Credit Card, Debit Card, PayPal
- **Fields**: TransactionID, CustomerID, TransactionDate, ProductID, Quantity, Amount, ProductCategory, PaymentMethod

### Product Data (11 products)
- **4 Categories**: Electronics, Clothing, Home, Books
- **Pricing**: $35-$120 per unit
- **Brands**: TechBrand, FashionCo, HomeStyle, ReadWell, SportMax
- **Fields**: ProductID, ProductName, ProductCategory, UnitPrice, Brand

## 🎯 Segmentation Approaches

### 1. 👥 Demographic Segmentation
- **Age Groups**: 18-24, 25-34, 35-44, 45-54, 55+
- **Income Levels**: Low (<$50K), Medium ($50K-$75K), High (>$75K)
- **Education Levels**: Bachelor, Master, PhD
- **Geographic Distribution**: Analysis by city and region

### 2. 🛒 Behavioral Segmentation
- **Purchase Frequency**: How often customers buy
- **Average Order Value**: How much customers spend per transaction
- **Product Category Preferences**: Electronics, Clothing, Home, Books
- **Payment Method Usage**: Credit Card, Debit Card, PayPal patterns

### 3. 💰 RFM Analysis (Recency, Frequency, Monetary)
- **Recency**: Days since last purchase (1-5 score)
- **Frequency**: Number of transactions (1-5 score)
- **Monetary**: Total amount spent (1-5 score)
- **Customer Segments**: Champions, Loyal Customers, Potential Loyalists, At Risk, Lost

## 🎓 Expected Outcomes

By completing this project, you will gain experience in:

- **📊 Customer Analytics**: Understanding customer behavior and value
- **📈 Data Visualization**: Creating compelling dashboards and reports
- **💼 Business Intelligence**: Transforming data into actionable insights
- **📝 Data Storytelling**: Communicating insights effectively
- **🎯 Marketing Analytics**: Segmentation for targeted campaigns

## 💼 Business Applications

The segmentation results can be used for:

- **🎯 Targeted Marketing**: Personalized campaigns for different segments
- **📦 Product Development**: Understanding segment-specific needs
- **🔄 Customer Retention**: Identifying at-risk customers
- **💵 Pricing Strategy**: Segment-based pricing optimization
- **📦 Inventory Planning**: Demand forecasting by segment
- **🛎️ Customer Service**: Priority handling for high-value segments

## 📚 Documentation

- **📖 Data Dictionary.md**: Complete data documentation and field descriptions
- **🎯 Segmentation Methodology.md**: Detailed explanation of segmentation approaches
- **📊 Power BI Report Guide.md**: Step-by-step Power BI implementation

## 📋 Requirements

### Power BI Requirements
- **Power BI Desktop** (free download from Microsoft)
- **Windows operating system** (Windows 10/11 recommended)
- **4GB RAM minimum** (8GB recommended for optimal performance)
- **1GB free disk space** for Power BI Desktop

### Technical Specifications Used
- **Power BI Desktop**: Latest version (as of 2024)
- **Data Sources**: CSV files (customer_data.csv, transaction_data.csv, product_data.csv)
- **Data Model**: Relational model with customer and product lookups
- **Visualizations**: Cards, bar charts, column charts, pie charts, matrices
- **DAX Measures**: Calculated columns and measures for RFM analysis

## 🛠️ Installation

### Power BI Setup
```bash
# Download from Microsoft
https://www.microsoft.com/en-us/power-platform/products/power-bi-desktop

# Install and run the application
# Follow the setup wizard
```

## 📊 Results & Insights

### Key Findings from Sample Data:
- **Customer Base**: 50 customers with diverse demographics
- **Total Revenue**: $19,000+ across 137 transactions
- **Average Order Value**: ~$139 per transaction
- **Top Age Groups**: 25-34 and 35-44 segments most active
- **Popular Categories**: Electronics and Home products lead in revenue
- **Customer Tenure**: Average 5.8 years, indicating loyal customer base

### Segmentation Results:
- **Champions**: High-value, frequent purchasers
- **Loyal Customers**: Consistent spenders with good retention
- **Potential Loyalists**: New customers showing promise
- **At Risk**: Customers who haven't purchased recently
- **Lost**: Inactive customers needing re-engagement

## 🛠️ Customization

### Adding Your Own Data
1. Replace the CSV files in the `data/` directory
2. Ensure the structure matches the existing format
3. Update field mappings in Power BI
4. Refresh the data model

### Modifying Segmentation Logic
- **Power BI**: Update DAX formulas and calculated columns
- Use the "New Measure" feature for custom calculations
- Modify data relationships in Model View

### Adding New Visualizations
- **Power BI**: Use the visualization gallery and custom visuals
- Drag and drop fields from the Data pane
- Use the Format pane to customize appearance

## 🔧 Troubleshooting

### Power BI Issues
- **Data loading errors**: Check file paths and formats
- **Relationship errors**: Verify key fields match between tables
- **Calculation errors**: Review DAX syntax and data types
- **Visual not updating**: Try refreshing the page or data
- **Performance issues**: Consider data optimization or filtering

## ✅ Best Practices

1. **🔍 Data Quality**: Always validate and clean your data
2. **📝 Documentation**: Document your analysis decisions
3. **✅ Validation**: Verify segments with business stakeholders
4. **🔄 Iteration**: Continuously refine segmentation based on results
5. **🔒 Privacy**: Handle customer data responsibly and compliantly
6. **💾 Backup**: Keep copies of original data files

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Future Enhancements

- **🔮 Predictive Analytics**: Add churn prediction models
- **📅 Time Series Analysis**: Seasonal pattern detection
- **🧪 A/B Testing**: Test marketing strategies by segment
- **⚡ Real-time Segmentation**: Implement streaming data processing
- **🎯 Advanced ML**: Try different clustering algorithms (DBSCAN, Hierarchical)
- **🔗 Integration**: Connect to live data sources and APIs

## Author 
Soundarya Umesh Barigidad , Information Science Engineering Student
