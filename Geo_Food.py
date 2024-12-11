import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import pandas as pd
import folium
from folium.plugins import HeatMap
# CHANGES IN LINE 10 TO 27 AND 164 TO 167
# OLD :
# Load the dataset
#food_orders = pd.read_csv("C:/Users/VICTUS/OneDrive/Desktop/Datasets/Food_order_New_Delhi.csv")

# Data cleaning
# Convert date and time columns to datetime
#food_orders['Order Date and Time'] = pd.to_datetime(food_orders['Order Date and Time'])
#food_orders['Delivery Date and Time'] = pd.to_datetime(food_orders['Delivery Date and Time'])

# NEW :

# Load the dataset
food_orders = pd.read_csv("Food_order_New_Delhi.csv")

# Data cleaning
# Convert date and time columns to datetimefood_orders['Order Date and Time'] = pd.to_datetime(
food_orders['Order Date and Time'] = pd.to_datetime(
    food_orders['Order Date and Time'], 
    errors='coerce'
)
food_orders['Delivery Date and Time'] = pd.to_datetime(
    food_orders['Delivery Date and Time'], 
    errors='coerce'
)


# Function to extract numeric values from the 'Discounts and Offers' string
def extract_discount(discount_str):
    if pd.isna(discount_str):
        return 0.0
    if 'off' in discount_str:
        # Fixed amount off
        return float(discount_str.split(' ')[0])
    elif '%' in discount_str:
        # Percentage off
        return float(discount_str.split('%')[0])
    else:
        # No discount
        return 0.0

# Apply the function to create a new 'Discount Percentage' column
food_orders['Discount Percentage'] = food_orders['Discounts and Offers'].apply(extract_discount)

# For percentage discounts, calculate the discount amount based on the order value
food_orders['Discount Amount'] = food_orders.apply(lambda x: (x['Order Value'] * x['Discount Percentage'] / 100)
                                                   if x['Discount Percentage'] > 1
                                                   else x['Discount Percentage'], axis=1)

# Adjust 'Discount Amount' for fixed discounts directly specified in the 'Discounts and Offers' column
food_orders['Discount Amount'] = food_orders.apply(lambda x: x['Discount Amount'] if x['Discount Percentage'] <= 1
                                                   else x['Order Value'] * x['Discount Percentage'] / 100, axis=1)

# Display the relevant columns and data types
print(food_orders[['Order Value', 'Discounts and Offers', 'Discount Percentage', 'Discount Amount']].head())
print(food_orders.dtypes)

# Cost and profit analysis

# Calculate total costs and revenue per order
food_orders['Total Costs'] = food_orders['Delivery Fee'] + food_orders['Payment Processing Fee'] + food_orders['Discount Amount']
food_orders['Revenue'] = food_orders['Commission Fee']
food_orders['Profit'] = food_orders['Revenue'] - food_orders['Total Costs']

# Aggregate data to get overall metrics
total_orders = food_orders.shape[0]
total_revenue = food_orders['Revenue'].sum()
total_costs = food_orders['Total Costs'].sum()
total_profit = food_orders['Profit'].sum()

overall_metrics = {
    "Total Orders": total_orders,
    "Total Revenue": total_revenue,
    "Total Costs": total_costs,
    "Total Profit": total_profit
}

print(overall_metrics)

# Visualization of distribution of costs, revenue, and profit
# Histogram of profits per order
plt.figure(figsize=(10, 6))
plt.hist(food_orders['Profit'], bins=50, color='skyblue', edgecolor='black')
plt.title('Profit Distribution per Order in Food Delivery')
plt.xlabel('Profit')
plt.ylabel('Number of Orders')
plt.axvline(food_orders['Profit'].mean(), color='red', linestyle='dashed', linewidth=1)
plt.show()

# Visualization of Proportion of total costs
# Pie chart for the proportion of total costs
costs_breakdown = food_orders[['Delivery Fee', 'Payment Processing Fee', 'Discount Amount']].sum()
plt.figure(figsize=(7, 7))
plt.pie(costs_breakdown, labels=costs_breakdown.index, autopct='%1.1f%%', startangle=140, colors=['tomato', 'gold', 'lightblue'])
plt.title('Proportion of Total Costs in Food Delivery')
plt.show()

# Comparing total revenue, total costs, and total profit (net loss in our case)
# Bar chart for total revenue, costs, and profit
totals = ['Total Revenue', 'Total Costs', 'Total Profit']
values = [total_revenue, total_costs, total_profit]

plt.figure(figsize=(8, 6))
plt.bar(totals, values, color=['green', 'red', 'blue'])
plt.title('Total Revenue, Costs, and Profit')
plt.ylabel('Amount (INR)')
plt.show()

# New Strategy for Profits

# Filter the dataset for profitable orders
profitable_orders = food_orders[food_orders['Profit'] > 0]

# Calculate the average commission percentage for profitable orders
profitable_orders['Commission Percentage'] = (profitable_orders['Commission Fee'] / profitable_orders['Order Value']) * 100

# Calculate the average discount percentage for profitable orders
profitable_orders['Effective Discount Percentage'] = (profitable_orders['Discount Amount'] / profitable_orders['Order Value']) * 100

# Calculate the new averages
new_avg_commission_percentage = profitable_orders['Commission Percentage'].mean()
new_avg_discount_percentage = profitable_orders['Effective Discount Percentage'].mean()

print(new_avg_commission_percentage, new_avg_discount_percentage)

# Simulate profitability with recommended discounts and commissions
recommended_commission_percentage = 30.0  # 30%
recommended_discount_percentage = 6.0    # 6%

# Calculate the simulated commission fee and discount amount using recommended percentages
food_orders['Simulated Commission Fee'] = food_orders['Order Value'] * (recommended_commission_percentage / 100)
food_orders['Simulated Discount Amount'] = food_orders['Order Value'] * (recommended_discount_percentage / 100)

# Recalculate total costs and profit with simulated values
food_orders['Simulated Total Costs'] = (food_orders['Delivery Fee'] +
                                        food_orders['Payment Processing Fee'] +
                                        food_orders['Simulated Discount Amount'])

food_orders['Simulated Profit'] = (food_orders['Simulated Commission Fee'] -
                                   food_orders['Simulated Total Costs'])

# Visualizing the comparison
plt.figure(figsize=(14, 7))

# Actual profitability
sns.kdeplot(food_orders['Profit'], label='Actual Profitability', fill=True, alpha=0.5, linewidth=2)

# Simulated profitability
sns.kdeplot(food_orders['Simulated Profit'], label='Estimated Profitability with Recommended Rates', fill=True, alpha=0.5, linewidth=2)

plt.title('Comparison of Profitability in Food Delivery: Actual vs. Recommended Discounts and Commissions')
plt.xlabel('Profit')
plt.ylabel('Density')
plt.legend(loc='upper left')
plt.show()

#   Geospatial Ananlysis Using Heatwave

# Load the dataset with geospatial information

# OLD: 
#food_orders_geo = pd.read_csv('C:/Users/VICTUS/OneDrive/Desktop/food_orders_new_delhi.csv')
# NEW:
food_orders_geo = pd.read_csv('Food_order_New_Delhi.csv')

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    food_orders_geo,
    geometry=gpd.points_from_xy(food_orders_geo['Longitude'], food_orders_geo['Latitude'])
)

# Check for missing geospatial data
print(gdf[['Latitude', 'Longitude', 'Order Value']].head())

# Create heatmaps
m = folium.Map(location=[food_orders_geo['Latitude'].mean(), food_orders_geo['Longitude'].mean()], zoom_start=12)
heat_data = [[row['Latitude'], row['Longitude']] for index, row in food_orders_geo.iterrows()]
HeatMap(heat_data).add_to(m)
m.save('heatmap.html')

# Analyze delivery zones
delivery_zones = {
    "Zone 1": [28.6139, 77.2090],
    "Zone 2": [28.7041, 77.1025],
}

m_zones = folium.Map(location=[food_orders_geo['Latitude'].mean(), food_orders_geo['Longitude'].mean()], zoom_start=12)
for zone, coords in delivery_zones.items():
    folium.Marker(
        location=coords,
        popup=zone,
        icon=folium.Icon(color='blue')
    ).add_to(m_zones)
m_zones.save('delivery_zones.html')

# Visualization with Matplotlib

# 1. Histogram of Order Values
plt.figure(figsize=(10, 6))
plt.hist(food_orders_geo['Order Value'], bins=30, edgecolor='black')
plt.title('Distribution of Order Values')
plt.xlabel('Order Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2. Scatter Plot of Orders (Latitude vs Longitude)
plt.figure(figsize=(10, 6))
plt.scatter(food_orders_geo['Longitude'], food_orders_geo['Latitude'], alpha=0.5, c='blue', s=10)
plt.title('Scatter Plot of Orders')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()

# 3. Box Plot of Order Values
plt.figure(figsize=(10, 6))
plt.boxplot(food_orders_geo['Order Value'], vert=False)
plt.title('Box Plot of Order Values')
plt.xlabel('Order Value')
plt.grid(True)
plt.show()