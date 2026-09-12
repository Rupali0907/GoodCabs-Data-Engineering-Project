# GoodCabs – Transportation Data Processing & Analytics System

## Project Overview

GoodCabs is an end-to-end data engineering project built to process transportation data and generate business insights.

The project uses Databricks and PySpark to ingest, clean, transform and analyze transportation trip data.

The project follows the Medallion Architecture:

**Bronze → Silver → Gold**

The processed data is used for SQL analysis, interactive dashboards and natural-language analytics using Databricks Genie.

---

## Business Objectives

The project analyzes transportation performance across different cities and helps answer questions such as:

- Which city generates the highest revenue?
- Which city has the highest number of rides?
- What are the average passenger and driver ratings?
- How does revenue change over time?
- How does the number of rides change over time?

---

## Architecture

```text
Raw Transportation Data
          |
          v
      Bronze Layer
          |
          v
   Cleaning & Quality Checks
          |
          v
      Silver Layer
          |
          v
   Business Transformations
          |
          v
       Gold Layer
          |
     +----+----+
     |         |
     v         v
 Dashboard   Genie
     |
     v
Business Analytics

## Technologies Used

- Databricks
- PySpark
- SQL
- Delta Lake
- Lakeflow Pipelines
- Unity Catalog
- Databricks AI/BI Dashboards
- Databricks Genie
- GitHub

## Data Processing

### Bronze Layer
Stores raw city and trip data.

- `goodcabs.bronze.city`
- `goodcabs.bronze.trips`

### Silver Layer
Cleans and validates the data.

- `goodcabs.silver.city`
- `goodcabs.silver.trips`
- `goodcabs.silver.calendar`

### Gold Layer
Contains business-ready data for analytics.

- `goodcabs.gold.gold_fact_trips`
- `goodcabs.gold.city_metrics`

Key metrics include total rides, total revenue, average passenger rating and average driver rating.

## Data Quality

The Silver layer includes checks for:

- Valid dates
- Driver ratings
- Passenger ratings

## SQL Analysis

SQL is used for city-wise revenue, rides, ratings and trend analysis.

## Dashboard

The Databricks AI/BI Dashboard includes:

- Total Revenue
- Total Rides
- Average Ratings
- Revenue by City
- Rides by City
- Revenue Trend
- Rides Trend
- City Filter

## Databricks Genie

Genie enables natural-language analysis of the Gold data.

Example:

- Which city has the highest revenue?
- Which city has the highest number of rides?

## Unity Catalog

Data is organized using:

- `goodcabs.bronze`
- `goodcabs.silver`
- `goodcabs.gold`

Basic access permissions are configured for the Gold layer.

## Project Structure

```text
GoodCabs-Data-Engineering/
│
├── README.md
└── transformations/
    ├── city_silver.py
    ├── calendar.py
    ├── trips_bronze.py
    ├── trips_silver.py
    ├── gold_fact_trips.py
    ├── gold_city_metrics.py
    ├── fact_trips_vadodara.py
    └── city_access.py

          
