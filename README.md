# GeoFood: Food Delivery Data Analysis

## Overview:-
GeoFood is a data analysis project aimed at examining food delivery trends in New Delhi. This project utilizes various Python libraries to clean, analyze, and visualize data to extract actionable insights. The analyses focus on profitability, cost distribution, and delivery zones using both traditional data visualization and geospatial analysis techniques.

## Features:-
- **Data Cleaning & Transformation**: Handles raw data preparation and conversion for analysis.
- **Financial Analysis**: Computes order-level revenue, total costs, and overall profit.
- **Data Visualizations**: Generates detailed plots and charts to understand financial metrics and distribution.
- **Geospatial Analysis**: Creates heatmaps and delivery zone visualizations to identify delivery hotspots.

## Technologies Used:-
- **Programming Language**: Python 3.x
- **Libraries**: 
  - `pandas` for data manipulation and analysis
  - `matplotlib` and `seaborn` for data visualization
  - `folium` for interactive maps and geospatial analysis
  - `geopandas` for handling geographical data

## Data Input :-
Order Date and Time
Delivery Date and Time
Order Value
Discounts and Offers
Delivery Fee
Payment Processing Fee
Commission Fee
Latitude
Longitude

## Visualizations and Outputs:-
1. Histogram of Order Values
Displays the distribution of order values, providing insights into the range and frequency of orders.

2. Scatter Plot (Latitude vs Longitude)
A visual representation of order locations to understand distribution patterns across New Delhi.

3. Profit Distribution
Histogram showcasing the distribution of profit per order, including a line for the mean profit.

4. Proportion of Costs Pie Chart
Breakdown of total costs such as delivery fees, payment processing fees, and discounts.

5. Heatmap of Delivery Locations
Interactive visualization created using Folium to show high-density order locations in New Delhi.

6. Delivery Zones
Mapping of defined delivery zones to understand area-based delivery performance.

Analysis Summary:-
Total Orders: Displayed as a metric for understanding order volume.
Total Revenue, Costs, and Profit: Calculated to measure the overall financial performance.
Simulation of Profitability: Estimated profitability based on recommended commission and discount percentages.


