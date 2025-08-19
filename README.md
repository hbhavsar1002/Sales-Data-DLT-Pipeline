# Sales Data DLT Pipeline

This repository contains a **Delta Live Tables (DLT) pipeline** designed to process and analyze sales data. The pipeline leverages a **Medallion Architecture** to organize and transform raw data into meaningful business insights.  

The pipeline includes data from multiple sources such as **Sales East, Sales West, Products, and Customers**, and follows a three-layer architecture: **Bronze, Silver, and Gold**.  


## Architecture Overview

The pipeline is built using the **Medallion Architecture**, with the following layers:

### Bronze Layer (Raw Data)
**Tables:**
- **Sales East**: Contains sales data for the East region.  
- **Sales West**: Contains sales data for the West region.  
- **Products**: Information about products, including product ID and category.  
- **Customer**: Information about customers, including customer ID and region.  

**Transformation:**  
The **Sales East** and **Sales West** data streams are merged into a single Delta Live Table (DLT) in the Bronze layer. This provides a unified view of the sales data from both regions.  

---

### Silver Layer (Cleansed Data)
**Tables:**
- **AutocDC Type 1 Flow**: Ensures the latest records for each sale are captured (overwriting historical data).  

**Transformation:**  
The data from the Bronze layer is **cleaned, filtered, and transformed**, ensuring only relevant data is included in the final dataset.  

---

### Gold Layer (Aggregated Business Data)
**Tables:**
- **AutocDC Type 2 Flow**: Captures **historical changes** to data over time. Both the latest and historical records are stored.  

**Business View:**  
- A summarized view is created to analyze **total sales by region and category**, providing insights for decision-makers.  

---

## Key Features
- **Medallion Architecture**: Ensures that raw data is transformed into clean, structured, and aggregated business data.  
- **AutocDC**:  
  - **Type 1 (Silver Layer)** → Keeps only the most recent data.  
  - **Type 2 (Gold Layer)** → Maintains both current and historical records.  
- **Sales Aggregation**: Provides insights into total sales performance across regions and product categories.  

---

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/hbhavsar1002/Sales-Data-DLT-Pipeline
```
### 2. Setup DLT Pipeline
- Install Delta Live Tables if not already set up.  
- Follow the [Databricks documentation](https://docs.databricks.com/workflows/delta-live-tables/index.html) to configure the DLT pipeline.  

---

### 3. Run the Pipeline
- Trigger the DLT pipeline to start processing sales data.  
- Monitor pipeline progress in the Databricks UI.  

---

## Example Queries

**1. Total Sales by Region**
```sql
SELECT region, SUM(total_sales) AS total_sales
FROM gold_sales_data
GROUP BY region;
```

**2. Total Sales by Category
```sql
SELECT category, SUM(total_sales) AS total_sales
FROM gold_sales_data
GROUP BY category;
```
## Pipeline Run Screenshot

Below is a screenshot of the Delta Live Tables pipeline run:

<img width="1932" height="1224" alt="image" src="https://github.com/user-attachments/assets/f4162249-2574-43a6-95c4-1501c4fb34f0" />


## Future Enhancements
- Add additional **business metrics and aggregations** to the Gold layer.  
- Implement **advanced data quality checks** in the Silver layer.  
- Incorporate **Sales Forecasting** using historical data and ML models.  

---

## Conclusion
This DLT pipeline provides a **flexible, efficient way** to process, clean, and aggregate sales data across regions.  
