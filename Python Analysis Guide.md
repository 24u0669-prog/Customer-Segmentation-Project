# Python Customer Segmentation Analysis Guide

## Overview
This guide provides instructions for running the Python-based customer segmentation analysis as an alternative to the Power BI approach.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation

### 1. Install Required Packages
Navigate to the `python` directory and install the required packages:

```bash
cd python
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 2. Verify Installation
Run the following command to verify installations:
```bash
python -c "import pandas, numpy, matplotlib, seaborn, sklearn; print('All packages installed successfully')"
```

## Running the Analysis

### Basic Execution
From the project root directory:
```bash
cd python
python customer_segmentation.py
```

### From Project Root
```bash
python python/customer_segmentation.py
```

## Analysis Components

The Python script performs the following analyses:

### 1. Demographic Analysis
- Age distribution and grouping
- Income level segmentation
- Education level analysis
- Gender distribution
- Geographic distribution

**Output:** `demographic_analysis.png`

### 2. RFM Analysis
- Recency, Frequency, Monetary scoring
- Customer segment assignment (Champions, Loyal, At Risk, etc.)
- Segment performance comparison
- RFM score distribution

**Output:** `rfm_analysis.png`

### 3. K-Means Clustering
- Elbow method for optimal cluster determination
- K-means clustering on customer features
- Cluster characterization and naming
- PCA visualization of clusters

**Output:** `elbow_curve.png`, `kmeans_clustering.png`

### 4. Behavioral Analysis
- Product category preferences
- Payment method analysis
- Monthly sales patterns
- Transaction amount distribution

**Output:** `behavioral_analysis.png`

### 5. Comprehensive Report
- Processed customer data with all calculated metrics
- Summary statistics
- Segment performance rankings

**Output:** `customer_segmentation_results.csv`

## Understanding the Output Files

### Visualizations (.png files)
- **demographic_analysis.png**: Customer demographic distributions
- **rfm_analysis.png**: RFM segment analysis and characteristics
- **elbow_curve.png**: Elbow method for determining optimal clusters
- **kmeans_clustering.png**: K-means clustering results and visualizations
- **behavioral_analysis.png**: Purchase behavior and patterns

### Data File (.csv)
- **customer_segmentation_results.csv**: Complete customer dataset with:
  - Original demographic data
  - Calculated RFM scores and segments
  - Cluster assignments
  - Behavioral metrics
  - Derived features

## Customization Options

### Modify Number of Clusters
Edit the main function or call the clustering method with a different k:
```python
segmentation.kmeans_clustering(n_clusters=5)  # Change from 4 to 5
```

### Change Features for Clustering
Modify the features list in the `kmeans_clustering` method:
```python
features = ['Age', 'Income', 'TotalSpend', 'TransactionCount', 
           'AvgOrderValue', 'CategoryDiversity', 'YearsAsCustomer']
```

### Adjust RFM Scoring
Modify the scoring bins in the `rfm_analysis` method to change segment definitions.

### Customize Visualizations
The script uses matplotlib and seaborn. You can modify:
- Color schemes
- Chart types
- Figure sizes
- Labels and titles

## Integration with Power BI

### Export Results for Power BI
The generated CSV file can be imported into Power BI for additional visualization:

1. Open Power BI Desktop
2. Get Data → Text/CSV
3. Select `python/customer_segmentation_results.csv`
4. Use the pre-calculated segments and scores in Power BI visualizations

### Use Python Visuals in Power BI
Power BI supports Python visuals for advanced analytics:

1. Enable Python scripting in Power BI options
2. Add a Python visual to your report
3. Use the clustering and analysis code directly in Power BI

## Troubleshooting

### Common Issues

**Issue:** ModuleNotFoundError
```bash
Solution: Install missing packages using pip install <package_name>
```

**Issue:** File not found errors
```bash
Solution: Ensure you're running the script from the correct directory
or update the file paths in the script.
```

**Issue:** Display issues with plots
```bash
Solution: The script saves plots automatically. If you want to display
them interactively, remove plt.close() calls.
```

**Issue:** Memory errors with large datasets
```bash
Solution: Process data in chunks or use sampling for initial analysis.
```

## Advanced Usage

### Custom Segmentation Logic
Add your own segmentation methods by extending the class:

```python
def custom_segmentation(self):
    # Your custom segmentation logic
    pass
```

### Time Series Analysis
Add time-based analysis for seasonal patterns and trends:

```python
def time_series_analysis(self):
    # Add time series analysis
    pass
```

### Predictive Modeling
Extend the script to include predictive capabilities:

```python
from sklearn.ensemble import RandomForestClassifier

def predict_churn(self):
    # Add churn prediction
    pass
```

## Performance Considerations

### Large Datasets
For datasets with more than 10,000 customers:
- Use sampling for initial exploration
- Consider incremental clustering
- Optimize memory usage with data types

### Computation Time
- K-means clustering: O(n * k * i * d) where n=samples, k=clusters, i=iterations, d=dimensions
- RFM analysis: O(n) - very fast
- Demographic analysis: O(n) - very fast

## Next Steps

1. **Explore Results**: Review generated visualizations and data files
2. **Refine Segments**: Adjust clustering parameters based on business needs
3. **Validate Segments**: Compare with business knowledge and requirements
4. **Deploy Insights**: Integrate findings into marketing strategies
5. **Monitor Performance**: Track segment changes over time

## Comparison with Power BI Approach

| Aspect | Python | Power BI |
|--------|--------|----------|
| Learning Curve | Steeper (requires programming) | Easier (GUI-based) |
| Flexibility | High (custom algorithms) | Medium (built-in features) |
| Visualization | Good (matplotlib/seaborn) | Excellent (interactive) |
| Deployment | Requires environment setup | Easy (web publishing) |
| Advanced Analytics | Excellent (ML libraries) | Limited (Python integration) |
| Real-time Updates | Manual refresh | Automatic refresh |
| Collaboration | Code sharing | Report sharing |

## Support and Resources

- Python Documentation: https://docs.python.org/3/
- Scikit-learn Documentation: https://scikit-learn.org/
- Pandas Documentation: https://pandas.pydata.org/
- Matplotlib Documentation: https://matplotlib.org/

## Best Practices

1. **Data Quality**: Always validate your data before analysis
2. **Reproducibility**: Set random seeds for clustering
3. **Documentation**: Comment your code and analysis decisions
4. **Version Control**: Use git for tracking changes
5. **Testing**: Validate results with business stakeholders
6. **Performance**: Profile code for large datasets
7. **Security**: Handle customer data responsibly and compliantly