# GeoFood: Food Delivery Data Analysis  

## Overview  
GeoFood is a data analysis project aimed at examining food delivery trends in New Delhi. This project utilizes Python libraries to clean, analyze, and visualize data to extract actionable insights. The analyses focus on profitability, cost distribution, order values, and delivery zones using both traditional data visualization and geospatial techniques.  

## Key Insights from Visualizations  

### 1. Profit Distribution per Order  
- The histogram reveals the spread of profit per order, ranging from significant losses (-1000 INR) to moderate profits (200 INR).  
- Most orders cluster around the breakeven point (0 INR), indicating thin margins.  

![Profit Distribution per Order](https://github.com/Adityasubhaditya/geofood/blob/main/Screenshot%202025-05-23%20192138.png?raw=true)  

### 2. Total Revenue, Costs, and Profit  
- **Total Revenue**: ~150,000 INR  
- **Total Costs**: ~100,000 INR  
- **Total Profit**: ~50,000 INR  
- Costs nearly offset revenue, emphasizing the need for cost optimization.  

![Total Financial Metrics](https://github.com/Adityasubhaditya/geofood/blob/main/Screenshot%202025-05-23%20192240.png?raw=true)  

### 3. Profitability Comparison: Actual vs. Recommended Rates  
- Adjusting discounts and commissions could shift profitability density toward higher profits (0–250 INR range).  
- Current profitability is skewed toward lower margins or losses.  

![Profitability Comparison](https://github.com/Adityasubhaditya/geofood/blob/main/Screenshot%202025-05-23%20192304.png?raw=true)  

### 4. Distribution of Order Values  
- Most orders fall between 250–1000 INR, with frequencies peaking at ~40 orders for lower values.  
- Higher-order values (>1500 INR) are rare but may contribute disproportionately to revenue.  

![Order Value Distribution](https://github.com/Adityasubhaditya/geofood/blob/main/Screenshot%202025-05-23%20192326.png?raw=true)  

### 5. Box Plot of Order Values  
- Median order value lies near 750 INR.  
- Significant outliers above 1500 INR suggest occasional high-value orders.  

![Order Value Box Plot](https://github.com/Adityasubhaditya/geofood/blob/main/Screenshot%202025-05-23%20192405.png?raw=true)  

### 6. Geospatial Order Density
[INSERT SCATTER PLOT IMAGE HERE]
Figure: Order Concentration (Latitude 28.6–28.7, Longitude 77.1–77.2)

### 7. Cost Structure Breakdown
[INSERT PIE CHART IMAGE HERE]
Figure: Cost Distribution (Discounts 74.9%, Delivery Fees 12.8%, Payment Processing 12.3%)

Critical Issue: Discounts consume 3/4 of total costs.

Solution: Implement dynamic discounts (max 30% for high-value orders).





Hotspots: Connaught Place, Saket.

Gaps: Expand marketing in South Extension (Lat <28.6).

## Features  
- **Data Cleaning & Transformation**: Handles missing values, outliers, and geospatial conversions.  
- **Financial Analysis**: Computes revenue, costs (delivery fees, commissions), and profit at order and aggregate levels.  
- **Visualizations**:  
  - Histograms and box plots for order values and profitability.  
  - Comparative density plots for profitability scenarios.  
  - Interactive heatmaps (Folium) for delivery location density.  
- **Geospatial Analysis**: Maps delivery zones and hotspots in New Delhi.  

## Technologies Used  
- **Python 3.x**  
- **Libraries**:  
  - `pandas`, `numpy` for data manipulation.  
  - `matplotlib`, `seaborn` for visualizations.  
  - `folium`, `geopandas` for geospatial mapping.  

## Data Input  
- Order/delivery timestamps, order value (INR).  
- Fees: Delivery, payment processing, commissions.  
- Discounts/offers applied.  
- Latitude/longitude for geospatial analysis.  



---  
*Visualizations and analysis derived from GeoFood project data (New Delhi region).*
