# 🏨 Hotel Booking Analytics Dashboard | Snowflake + Streamlit

## 📌 Project Overview

This project demonstrates an end-to-end Hotel Booking Analytics solution built using Snowflake, SQL, Python, and Streamlit. Raw hotel booking data is ingested into Snowflake, transformed through a Medallion Architecture (Bronze, Silver, and Gold Layers), and visualized through an interactive Streamlit dashboard.

The solution enables hotel management teams to analyze booking trends, revenue performance, room utilization, customer behavior, booking status distribution, and operational KPIs through real-time dashboards powered directly from Snowflake.

---

## 🚀 Architecture

<img width="1536" height="1024" alt="ChatGPT Image Jun 11, 2026, 06_26_35 PM" src="https://github.com/user-attachments/assets/266752c1-9dc8-4ac8-bd93-e0b889eeeffb" />


### Data Flow

```text
Hotel Booking CSV
        │
        ▼
Bronze Layer (Raw Data)
RAW_HOTEL_BOOKING
        │
        ▼
Silver Layer (Cleaned Data)
SILVER_HOTEL_BOOKING
        │
        ▼
Gold Layer (Aggregated Analytics)
GOLD_HOTEL_AGGREGATES
        │
        ▼
Streamlit Dashboard
        │
        ▼
Business Insights & KPI Reporting
```

---

## 🏗️ Medallion Architecture

### 🥉 Bronze Layer – Raw Data

Stores source booking data exactly as received from the source system.

**Table:**

```sql
HOTEL_DB.PUBLIC.RAW_HOTEL_BOOKING
```

Responsibilities:

* Raw CSV ingestion
* Historical data preservation
* No transformations applied
* Source-of-truth storage

---

### 🥈 Silver Layer – Cleaned Data

Performs data quality checks and standardization.

**Table:**

```sql
HOTEL_DB.PUBLIC.SILVER_HOTEL_BOOKING
```

Transformations:

* Null value handling
* Date standardization
* Data type corrections
* Duplicate validation
* Data cleansing
* Business rule validation

---

### 🥇 Gold Layer – Aggregated Analytics

Creates business-ready datasets optimized for reporting and dashboard consumption.

**Table:**

```sql
HOTEL_DB.PUBLIC.GOLD_HOTEL_AGGREGATES
```

Aggregations:

* Total Revenue
* Total Bookings
* Revenue by Room Type
* Bookings by City
* Booking Status Metrics
* Occupancy KPIs
* Dashboard Summary Metrics

---

## 🛠️ Technology Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Snowflake  | Cloud Data Warehouse            |
| SQL        | Data Transformation & Analytics |
| Python     | Dashboard Development           |
| Streamlit  | Interactive Dashboard           |
| GitHub     | Version Control                 |
| CSV        | Source Data                     |

---

## 📂 Repository Structure

```text
hotel-booking-dashboard/

├── data/
│   └── hotel_bookings_raw.csv
│
├── sql/
│   ├── Processing.sql
│   ├── Dashboard.sql
│
├── streamlit/
│   └── app.py
│
├── screenshots/
│   ├── dashboard-overview.png
│   ├── booking-status.png
│   ├── booking-details.png
│   └── hotel_analytics_architecture.png
│
└── README.md
```

---

## 🔄 Data Pipeline

### Step 1: Data Ingestion

* Load hotel booking CSV data into Snowflake.
* Store records in Bronze Layer.

### Step 2: Data Cleaning

Apply SQL transformations to:

* Standardize dates
* Remove duplicates
* Handle missing values
* Validate business rules

### Step 3: Data Aggregation

Generate Gold Layer tables containing:

* Revenue metrics
* Booking KPIs
* Room type analytics
* City-level summaries

### Step 4: Dashboard Reporting

Streamlit consumes Snowflake data directly and generates interactive dashboards.

---

## 📊 Dashboard Features

### Executive KPI Cards

* Total Bookings
* Total Revenue
* Average Guests per Booking
* Confirmed Booking Percentage

### Interactive Filters

* Hotel City
* Booking Status
* Room Type

### Visualizations

#### 📍 Bookings by City

Displays booking volume across hotel locations.

#### 💰 Revenue by Room Type

Analyzes revenue contribution from:

* Standard Rooms
* Deluxe Rooms
* Suites

#### 📈 Booking Status Distribution

Shows distribution of:

* Confirmed Bookings
* Cancelled Bookings
* No-Shows

#### 📅 Bookings Over Time

Tracks booking trends using check-in dates.

#### 📋 Booking Details Table

Provides detailed booking-level information with filtering capabilities.

---

## 📷 Dashboard Screenshots

### Dashboard Overview

![Dashboard Overview](screenshots/dashboard-overview.png)

### Booking Analytics

![Booking Analytics](screenshots/booking-status.png)

### Detailed Booking Report

![Booking Details](screenshots/booking-details.png)

---

## ▶️ Running the Project

### 1. Load Dataset into Snowflake

Upload:

```text
hotel_bookings_raw.csv
```

---

### 2. Execute Data Processing Script

Run:

```sql
Processing.sql
```

This creates and populates:

* Bronze Layer
* Silver Layer
* Gold Layer

---

### 3. Configure Snowflake Connection

Create:

```text
.streamlit/secrets.toml
```

```toml
[connections.snowflake]
account = "your_account"
user = "your_username"
password = "your_password"
warehouse = "your_warehouse"
database = "HOTEL_DB"
schema = "PUBLIC"
```

---

### 4. Install Dependencies

```bash
pip install streamlit snowflake-snowpark-python pandas
```

---

### 5. Run Dashboard

```bash
streamlit run app.py
```

---

## 📈 Key Business Insights

The dashboard enables stakeholders to:

* Monitor booking performance
* Track revenue trends
* Analyze room type profitability
* Evaluate booking confirmation rates
* Detect no-show patterns
* Analyze city-wise hotel performance
* Improve occupancy planning
* Support operational decision-making

---

## 🎯 Business KPIs

| KPI                         | Description                           |
| --------------------------- | ------------------------------------- |
| Total Bookings              | Total reservations processed          |
| Total Revenue               | Revenue generated from bookings       |
| Avg Guests                  | Average guests per booking            |
| Confirmation Rate           | Percentage of confirmed bookings      |
| Revenue by Room Type        | Revenue contribution by room category |
| Bookings by City            | Geographic booking analysis           |
| Booking Status Distribution | Operational booking health            |

---

## 💡 Skills Demonstrated

### Data Engineering

* Data Ingestion
* ETL Development
* Snowflake SQL
* Medallion Architecture
* Data Quality Validation
* Data Transformation

### Analytics Engineering

* KPI Development
* Business Reporting
* Data Modeling
* Aggregation Design

### Dashboard Development

* Streamlit
* Interactive Filtering
* Data Visualization
* Real-Time Analytics

### Cloud Data Warehousing

* Snowflake Tables
* SQL Processing
* Analytical Data Layers
* Reporting Optimization

---

## 🎯 Project Outcome

Successfully developed an end-to-end analytics solution that transforms raw hotel booking data into actionable business insights using Snowflake's Medallion Architecture and an interactive Streamlit dashboard.

The solution provides scalable reporting, improved data quality, and real-time KPI monitoring for hotel business stakeholders.

---

## 👨‍💻 Author

**Krishnakanth Reddy Sattineni**

Data Analyst | Data Engineer

**Technical Skills:**
Snowflake • SQL • Python • Streamlit • Power BI • AWS



