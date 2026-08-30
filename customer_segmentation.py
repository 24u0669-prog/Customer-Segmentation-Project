"""
Customer Segmentation Analysis using Python
This script provides an alternative approach to customer segmentation using Python and scikit-learn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class CustomerSegmentation:
    def __init__(self, customer_path, transaction_path, product_path):
        """
        Initialize the Customer Segmentation Analysis
        
        Parameters:
        -----------
        customer_path : str
            Path to customer data CSV file
        transaction_path : str
            Path to transaction data CSV file
        product_path : str
            Path to product data CSV file
        """
        self.customer_path = customer_path
        self.transaction_path = transaction_path
        self.product_path = product_path
        
        # Load data
        self.customers = pd.read_csv(customer_path)
        self.transactions = pd.read_csv(transaction_path)
        self.products = pd.read_csv(product_path)
        
        # Process data
        self.process_data()
        
    def process_data(self):
        """Process and merge the datasets"""
        # Convert date columns
        self.customers['CustomerSince'] = pd.to_datetime(self.customers['CustomerSince'])
        self.transactions['TransactionDate'] = pd.to_datetime(self.transactions['TransactionDate'])
        
        # Merge transactions with product data
        self.transactions = self.transactions.merge(
            self.products[['ProductID', 'ProductCategory', 'UnitPrice']], 
            on='ProductID', 
            how='left'
        )
        
        # Calculate customer metrics
        self.calculate_customer_metrics()
        
    def calculate_customer_metrics(self):
        """Calculate RFM and other customer metrics"""
        # Calculate metrics per customer
        customer_metrics = self.transactions.groupby('CustomerID').agg({
            'TransactionDate': ['max', 'count'],
            'Amount': ['sum', 'mean'],
            'Quantity': 'sum',
            'ProductCategory': lambda x: x.nunique()
        }).reset_index()
        
        # Flatten column names
        customer_metrics.columns = ['CustomerID', 'LastPurchaseDate', 'TransactionCount', 
                                   'TotalSpend', 'AvgOrderValue', 'TotalQuantity', 'CategoryDiversity']
        
        # Calculate recency (days since last purchase)
        reference_date = self.transactions['TransactionDate'].max()
        customer_metrics['RecencyDays'] = (reference_date - customer_metrics['LastPurchaseDate']).dt.days
        
        # Merge with customer demographics
        self.customer_analysis = self.customers.merge(customer_metrics, on='CustomerID', how='left')
        
        # Fill missing values for customers with no transactions
        self.customer_analysis['TransactionCount'] = self.customer_analysis['TransactionCount'].fillna(0)
        self.customer_analysis['TotalSpend'] = self.customer_analysis['TotalSpend'].fillna(0)
        self.customer_analysis['AvgOrderValue'] = self.customer_analysis['AvgOrderValue'].fillna(0)
        self.customer_analysis['TotalQuantity'] = self.customer_analysis['TotalQuantity'].fillna(0)
        self.customer_analysis['CategoryDiversity'] = self.customer_analysis['CategoryDiversity'].fillna(0)
        self.customer_analysis['RecencyDays'] = self.customer_analysis['RecencyDays'].fillna(365)  # Assume 1 year if no purchases
        
        # Create additional features
        self.customer_analysis['SpendPerYear'] = self.customer_analysis['TotalSpend'] / (self.customer_analysis['YearsAsCustomer'] + 1)
        
    def demographic_analysis(self):
        """Perform demographic segmentation analysis"""
        print("=" * 50)
        print("DEMOGRAPHIC SEGMENTATION ANALYSIS")
        print("=" * 50)
        
        # Age distribution
        print("\nAge Distribution:")
        print(self.customer_analysis['Age'].describe())
        
        # Create age groups
        self.customer_analysis['AgeGroup'] = pd.cut(
            self.customer_analysis['Age'], 
            bins=[0, 25, 35, 45, 55, 100], 
            labels=['18-24', '25-34', '35-44', '45-54', '55+']
        )
        
        # Income groups
        self.customer_analysis['IncomeGroup'] = pd.cut(
            self.customer_analysis['Income'], 
            bins=[0, 50000, 75000, 100000], 
            labels=['Low', 'Medium', 'High']
        )
        
        # Segment analysis
        print("\nCustomer Count by Age Group:")
        print(self.customer_analysis['AgeGroup'].value_counts().sort_index())
        
        print("\nCustomer Count by Income Group:")
        print(self.customer_analysis['IncomeGroup'].value_counts().sort_index())
        
        print("\nCustomer Count by Education:")
        print(self.customer_analysis['Education'].value_counts())
        
        # Plot demographic distributions
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Age distribution
        self.customer_analysis['AgeGroup'].value_counts().sort_index().plot(
            kind='bar', ax=axes[0, 0], color='skyblue'
        )
        axes[0, 0].set_title('Customer Distribution by Age Group')
        axes[0, 0].set_xlabel('Age Group')
        axes[0, 0].set_ylabel('Count')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Income distribution
        self.customer_analysis['IncomeGroup'].value_counts().sort_index().plot(
            kind='bar', ax=axes[0, 1], color='lightcoral'
        )
        axes[0, 1].set_title('Customer Distribution by Income Group')
        axes[0, 1].set_xlabel('Income Group')
        axes[0, 1].set_ylabel('Count')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Education distribution
        self.customer_analysis['Education'].value_counts().plot(
            kind='pie', ax=axes[1, 0], autopct='%1.1f%%'
        )
        axes[1, 0].set_title('Customer Distribution by Education')
        
        # Gender distribution
        self.customer_analysis['Gender'].value_counts().plot(
            kind='pie', ax=axes[1, 1], autopct='%1.1f%%'
        )
        axes[1, 1].set_title('Customer Distribution by Gender')
        
        plt.tight_layout()
        plt.savefig('python/demographic_analysis.png', dpi=300, bbox_inches='tight')
        print("\nDemographic analysis plot saved as 'demographic_analysis.png'")
        plt.close()
        
    def rfm_analysis(self):
        """Perform RFM (Recency, Frequency, Monetary) analysis"""
        print("\n" + "=" * 50)
        print("RFM ANALYSIS")
        print("=" * 50)
        
        # Calculate RFM scores
        self.customer_analysis['R_Score'] = pd.qcut(
            self.customer_analysis['RecencyDays'], 
            5, 
            labels=[5, 4, 3, 2, 1]
        )
        self.customer_analysis['F_Score'] = pd.qcut(
            self.customer_analysis['TransactionCount'].rank(method='first'), 
            5, 
            labels=[1, 2, 3, 4, 5]
        )
        self.customer_analysis['M_Score'] = pd.qcut(
            self.customer_analysis['TotalSpend'].rank(method='first'), 
            5, 
            labels=[1, 2, 3, 4, 5]
        )
        
        # Convert to numeric
        self.customer_analysis['R_Score'] = self.customer_analysis['R_Score'].astype(int)
        self.customer_analysis['F_Score'] = self.customer_analysis['F_Score'].astype(int)
        self.customer_analysis['M_Score'] = self.customer_analysis['M_Score'].astype(int)
        
        # Calculate RFM segment
        self.customer_analysis['RFM_Segment'] = (
            self.customer_analysis['R_Score'].astype(str) + 
            self.customer_analysis['F_Score'].astype(str) + 
            self.customer_analysis['M_Score'].astype(str)
        )
        
        # Calculate RFM score
        self.customer_analysis['RFM_Score'] = (
            self.customer_analysis['R_Score'] + 
            self.customer_analysis['F_Score'] + 
            self.customer_analysis['M_Score']
        )
        
        # Create segment names
        def get_segment_name(row):
            if row['R_Score'] >= 4 and row['F_Score'] >= 4:
                return 'Champions'
            elif row['R_Score'] >= 3 and row['F_Score'] >= 3:
                return 'Loyal Customers'
            elif row['R_Score'] >= 3 and row['F_Score'] <= 2:
                return 'Potential Loyalists'
            elif row['R_Score'] <= 2 and row['F_Score'] >= 3:
                return 'At Risk'
            elif row['R_Score'] <= 2 and row['F_Score'] <= 2:
                return 'Lost'
            else:
                return 'Others'
        
        self.customer_analysis['Segment'] = self.customer_analysis.apply(get_segment_name, axis=1)
        
        # Display RFM segment distribution
        print("\nRFM Segment Distribution:")
        print(self.customer_analysis['Segment'].value_counts())
        
        # Segment characteristics
        print("\nSegment Characteristics:")
        segment_stats = self.customer_analysis.groupby('Segment').agg({
            'CustomerID': 'count',
            'TotalSpend': 'mean',
            'TransactionCount': 'mean',
            'RecencyDays': 'mean'
        }).round(2)
        segment_stats.columns = ['Count', 'AvgSpend', 'AvgTransactions', 'AvgRecency']
        print(segment_stats)
        
        # Plot RFM segments
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Segment distribution
        self.customer_analysis['Segment'].value_counts().plot(
            kind='bar', ax=axes[0, 0], color='lightgreen'
        )
        axes[0, 0].set_title('Customer Distribution by RFM Segment')
        axes[0, 0].set_xlabel('Segment')
        axes[0, 0].set_ylabel('Count')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Average spend by segment
        segment_spend = self.customer_analysis.groupby('Segment')['TotalSpend'].mean().sort_values(ascending=False)
        segment_spend.plot(kind='bar', ax=axes[0, 1], color='orange')
        axes[0, 1].set_title('Average Spend by RFM Segment')
        axes[0, 1].set_xlabel('Segment')
        axes[0, 1].set_ylabel('Average Spend ($)')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # RFM score distribution
        self.customer_analysis['RFM_Score'].hist(bins=15, ax=axes[1, 0], color='purple', alpha=0.7)
        axes[1, 0].set_title('RFM Score Distribution')
        axes[1, 0].set_xlabel('RFM Score')
        axes[1, 0].set_ylabel('Frequency')
        
        # Recency vs Frequency scatter
        scatter = axes[1, 1].scatter(
            self.customer_analysis['RecencyDays'], 
            self.customer_analysis['TransactionCount'],
            c=self.customer_analysis['TotalSpend'], 
            cmap='viridis', 
            alpha=0.6,
            s=100
        )
        axes[1, 1].set_title('Recency vs Frequency (Color = Spend)')
        axes[1, 1].set_xlabel('Recency (Days)')
        axes[1, 1].set_ylabel('Frequency (Transactions)')
        plt.colorbar(scatter, ax=axes[1, 1], label='Total Spend ($)')
        
        plt.tight_layout()
        plt.savefig('python/rfm_analysis.png', dpi=300, bbox_inches='tight')
        print("\nRFM analysis plot saved as 'rfm_analysis.png'")
        plt.close()
        
    def kmeans_clustering(self, n_clusters=4):
        """Perform K-means clustering on customer data"""
        print("\n" + "=" * 50)
        print("K-MEANS CLUSTERING ANALYSIS")
        print("=" * 50)
        
        # Select features for clustering
        features = ['Age', 'Income', 'TotalSpend', 'TransactionCount', 
                   'AvgOrderValue', 'CategoryDiversity', 'YearsAsCustomer']
        
        # Prepare data
        cluster_data = self.customer_analysis[features].copy()
        
        # Handle missing values
        cluster_data = cluster_data.fillna(cluster_data.mean())
        
        # Standardize features
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(cluster_data)
        
        # Determine optimal number of clusters using elbow method
        inertias = []
        K_range = range(1, 10)
        
        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans.fit(scaled_data)
            inertias.append(kmeans.inertia_)
        
        # Plot elbow curve
        plt.figure(figsize=(10, 6))
        plt.plot(K_range, inertias, 'bo-')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Inertia')
        plt.title('Elbow Method for Optimal K')
        plt.grid(True)
        plt.savefig('python/elbow_curve.png', dpi=300, bbox_inches='tight')
        print("Elbow curve saved as 'elbow_curve.png'")
        plt.close()
        
        # Perform K-means with specified number of clusters
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.customer_analysis['Cluster'] = kmeans.fit_predict(scaled_data)
        
        # Display cluster characteristics
        print(f"\nCluster Analysis (K={n_clusters}):")
        print("\nCluster Sizes:")
        print(self.customer_analysis['Cluster'].value_counts().sort_index())
        
        print("\nCluster Characteristics:")
        cluster_features = ['Age', 'Income', 'TotalSpend', 'TransactionCount', 
                           'AvgOrderValue', 'YearsAsCustomer']
        cluster_stats = self.customer_analysis.groupby('Cluster')[cluster_features].mean().round(2)
        print(cluster_stats)
        
        # Name clusters based on characteristics
        cluster_names = {}
        for cluster in range(n_clusters):
            cluster_data = self.customer_analysis[self.customer_analysis['Cluster'] == cluster]
            avg_spend = cluster_data['TotalSpend'].mean()
            avg_income = cluster_data['Income'].mean()
            avg_age = cluster_data['Age'].mean()
            
            if avg_spend > 400 and avg_income > 70000:
                cluster_names[cluster] = 'High Value Affluent'
            elif avg_spend > 300 and avg_income > 50000:
                cluster_names[cluster] = 'Mid Value Professional'
            elif avg_age < 30:
                cluster_names[cluster] = 'Young Budget Conscious'
            elif avg_spend < 200:
                cluster_names[cluster] = 'Low Value Occasional'
            else:
                cluster_names[cluster] = f'Cluster {cluster}'
        
        self.customer_analysis['Cluster_Name'] = self.customer_analysis['Cluster'].map(cluster_names)
        
        print("\nCluster Names:")
        for cluster, name in cluster_names.items():
            print(f"Cluster {cluster}: {name}")
        
        # Visualize clusters
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # PCA visualization
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(scaled_data)
        
        scatter = axes[0, 0].scatter(
            pca_result[:, 0], 
            pca_result[:, 1],
            c=self.customer_analysis['Cluster'], 
            cmap='viridis', 
            alpha=0.6,
            s=100
        )
        axes[0, 0].set_title('PCA Visualization of Clusters')
        axes[0, 0].set_xlabel('Principal Component 1')
        axes[0, 0].set_ylabel('Principal Component 2')
        plt.colorbar(scatter, ax=axes[0, 0], label='Cluster')
        
        # Age vs Income by cluster
        for cluster in range(n_clusters):
            cluster_data = self.customer_analysis[self.customer_analysis['Cluster'] == cluster]
            axes[0, 1].scatter(cluster_data['Age'], cluster_data['Income'], 
                             label=f'Cluster {cluster}', alpha=0.6, s=100)
        axes[0, 1].set_title('Age vs Income by Cluster')
        axes[0, 1].set_xlabel('Age')
        axes[0, 1].set_ylabel('Income')
        axes[0, 1].legend()
        
        # Spend vs Frequency by cluster
        for cluster in range(n_clusters):
            cluster_data = self.customer_analysis[self.customer_analysis['Cluster'] == cluster]
            axes[1, 0].scatter(cluster_data['TransactionCount'], cluster_data['TotalSpend'], 
                             label=f'Cluster {cluster}', alpha=0.6, s=100)
        axes[1, 0].set_title('Transaction Count vs Total Spend by Cluster')
        axes[1, 0].set_xlabel('Transaction Count')
        axes[1, 0].set_ylabel('Total Spend ($)')
        axes[1, 0].legend()
        
        # Cluster distribution
        self.customer_analysis['Cluster_Name'].value_counts().plot(
            kind='bar', ax=axes[1, 1], color='lightblue'
        )
        axes[1, 1].set_title('Customer Distribution by Cluster')
        axes[1, 1].set_xlabel('Cluster Name')
        axes[1, 1].set_ylabel('Count')
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('python/kmeans_clustering.png', dpi=300, bbox_inches='tight')
        print("K-means clustering plot saved as 'kmeans_clustering.png'")
        plt.close()
        
    def behavioral_analysis(self):
        """Analyze customer behavioral patterns"""
        print("\n" + "=" * 50)
        print("BEHAVIORAL ANALYSIS")
        print("=" * 50)
        
        # Product category preferences
        print("\nProduct Category Preferences:")
        category_sales = self.transactions.groupby('ProductCategory').agg({
            'Amount': ['sum', 'count'],
            'Quantity': 'sum'
        }).round(2)
        category_sales.columns = ['TotalRevenue', 'TransactionCount', 'TotalQuantity']
        print(category_sales)
        
        # Payment method analysis
        print("\nPayment Method Distribution:")
        payment_stats = self.transactions.groupby('PaymentMethod').agg({
            'Amount': ['sum', 'count', 'mean']
        }).round(2)
        payment_stats.columns = ['TotalRevenue', 'TransactionCount', 'AvgTransaction']
        print(payment_stats)
        
        # Time-based analysis
        self.transactions['Month'] = self.transactions['TransactionDate'].dt.month
        self.transactions['DayOfWeek'] = self.transactions['TransactionDate'].dt.dayofweek
        
        print("\nMonthly Sales Pattern:")
        monthly_sales = self.transactions.groupby('Month')['Amount'].sum().sort_index()
        print(monthly_sales)
        
        # Plot behavioral patterns
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Revenue by category
        category_revenue = self.transactions.groupby('ProductCategory')['Amount'].sum()
        category_revenue.plot(kind='bar', ax=axes[0, 0], color='lightcoral')
        axes[0, 0].set_title('Total Revenue by Product Category')
        axes[0, 0].set_xlabel('Category')
        axes[0, 0].set_ylabel('Revenue ($)')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Payment method distribution
        payment_counts = self.transactions['PaymentMethod'].value_counts()
        payment_counts.plot(kind='pie', ax=axes[0, 1], autopct='%1.1f%%')
        axes[0, 1].set_title('Payment Method Distribution')
        
        # Monthly sales trend
        monthly_sales.plot(kind='line', ax=axes[1, 0], marker='o', color='green')
        axes[1, 0].set_title('Monthly Sales Trend')
        axes[1, 0].set_xlabel('Month')
        axes[1, 0].set_ylabel('Revenue ($)')
        axes[1, 0].grid(True)
        
        # Transaction amount distribution
        self.transactions['Amount'].hist(bins=20, ax=axes[1, 1], color='purple', alpha=0.7)
        axes[1, 1].set_title('Transaction Amount Distribution')
        axes[1, 1].set_xlabel('Transaction Amount ($)')
        axes[1, 1].set_ylabel('Frequency')
        
        plt.tight_layout()
        plt.savefig('python/behavioral_analysis.png', dpi=300, bbox_inches='tight')
        print("\nBehavioral analysis plot saved as 'behavioral_analysis.png'")
        plt.close()
        
    def generate_report(self):
        """Generate a comprehensive segmentation report"""
        print("\n" + "=" * 50)
        print("COMPREHENSIVE SEGMENTATION REPORT")
        print("=" * 50)
        
        # Save processed data
        self.customer_analysis.to_csv('python/customer_segmentation_results.csv', index=False)
        print("\nProcessed customer data saved as 'customer_segmentation_results.csv'")
        
        # Summary statistics
        print("\nSUMMARY STATISTICS:")
        print(f"Total Customers: {len(self.customers)}")
        print(f"Total Transactions: {len(self.transactions)}")
        print(f"Total Revenue: ${self.transactions['Amount'].sum():,.2f}")
        print(f"Average Order Value: ${self.transactions['Amount'].mean():,.2f}")
        print(f"Average Customer Spend: ${self.customer_analysis['TotalSpend'].mean():,.2f}")
        
        # Top segments
        print("\nTOP PERFORMING SEGMENTS:")
        if 'Segment' in self.customer_analysis.columns:
            segment_performance = self.customer_analysis.groupby('Segment').agg({
                'CustomerID': 'count',
                'TotalSpend': 'sum'
            }).sort_values('TotalSpend', ascending=False)
            segment_performance.columns = ['CustomerCount', 'TotalRevenue']
            print(segment_performance)
        
        print("\nAnalysis complete! Check the 'python' folder for generated visualizations and data files.")

def main():
    """Main function to run the customer segmentation analysis"""
    # File paths
    customer_path = '../data/customer_data.csv'
    transaction_path = '../data/transaction_data.csv'
    product_path = '../data/product_data.csv'
    
    # Initialize analysis
    print("Starting Customer Segmentation Analysis...")
    print("Loading data files...")
    
    try:
        segmentation = CustomerSegmentation(customer_path, transaction_path, product_path)
        
        # Run analyses
        segmentation.demographic_analysis()
        segmentation.rfm_analysis()
        segmentation.kmeans_clustering(n_clusters=4)
        segmentation.behavioral_analysis()
        
        # Generate final report
        segmentation.generate_report()
        
        print("\n" + "=" * 50)
        print("ANALYSIS COMPLETE!")
        print("=" * 50)
        print("Generated files:")
        print("- demographic_analysis.png")
        print("- rfm_analysis.png")
        print("- elbow_curve.png")
        print("- kmeans_clustering.png")
        print("- behavioral_analysis.png")
        print("- customer_segmentation_results.csv")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure the data files are in the correct location.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()