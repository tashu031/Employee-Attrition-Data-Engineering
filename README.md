# 📊 Employee Attrition Analysis using Azure Data Factory, Azure Databricks & Power BI

## 📌 Project Overview

Employee attrition is one of the major challenges faced by organizations. This project analyzes employee attrition data using Microsoft Azure Data Engineering services and Power BI to identify trends and factors influencing employee turnover.

The project demonstrates an end-to-end data engineering pipeline starting from raw employee data, processing it in Azure Databricks, orchestrating the workflow using Azure Data Factory, and visualizing business insights through an interactive Power BI dashboard.

---

# 🏗️ Project Architecture

```
Employee Attrition CSV Dataset
            │
            ▼
 Azure Data Lake Storage Gen2 (Raw Layer)
            │
            ▼
 Azure Data Factory Pipeline
            │
            ▼
 Azure Databricks Notebook
(Data Cleaning & Transformation)
            │
            ▼
Processed Data (Gold Layer)
            │
            ▼
Power BI Dashboard
```

---

# 🛠️ Technologies Used

- Microsoft Azure
- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2 (ADLS)
- Azure Databricks
- Apache Spark
- Python
- Power BI Desktop

---

# 📁 Project Structure

```
Employee-Attrition-Data-Engineering
│
├── Dataset
│   └── employee_attrition.csv
│
├── Databricks
│   └── Employee_Attrition_Notebook.ipynb
│
├── PowerBI
│   └── Employee_Attrition.pbix
│
├── Pipeline
│   ├── Pipeline.png
│   └── Pipeline_Run.png
│
├── Dashboard
│   └── Dashboard.png
│
└── README.md
```

---

# 🔄 Project Workflow

### Step 1
Raw Employee Attrition dataset is uploaded to Azure Data Lake Storage Gen2.

### Step 2
Azure Data Factory triggers the data pipeline.

### Step 3
Azure Databricks reads the raw dataset.

### Step 4
Data cleaning and preprocessing are performed using Apache Spark.

Operations include:
- Removing unnecessary columns
- Handling missing values
- Data transformation
- Data validation

### Step 5
Processed data is stored back in Azure Data Lake Storage.

### Step 6
Power BI connects to the processed dataset and generates an interactive dashboard.

---

# 📈 Dashboard Features

The dashboard includes:

### KPI Cards
- Total Employees
- Employees Left
- Overall Attrition Rate
- Total Departments

### Interactive Filters (Slicers)
- Department
- Age Group
- Gender

### Visualizations

- Department-wise Attrition Rate
- Overtime vs Attrition
- Performance Rating vs Attrition
- Job Role-wise Attrition
- Salary-wise Attrition
- Gender-wise Attrition
- Work-Life Balance vs Attrition
- Age Group vs Attrition
- Education-wise Attrition

---

# 📊 Key Insights

- Total Employees: **1470**
- Employees Left: **237**
- Overall Attrition Rate: **16.12%**
- Sales department has the highest attrition rate.
- Employees working overtime show higher attrition.
- Employees in the low salary slab have higher attrition.
- Laboratory Technicians and Sales Executives have the highest employee exits.
- Most employees have a Performance Rating of 3.
- Employees with a Work-Life Balance rating of 3 represent the largest group.

---

# 🚀 How to Run the Project

1. Upload the dataset to Azure Data Lake Storage Gen2.
2. Create and configure Azure Data Factory pipeline.
3. Execute the Databricks notebook.
4. Store transformed data back into ADLS.
5. Refresh the Power BI report.
6. Use slicers to explore insights interactively.

---

# 📷 Screenshots

## Dashboard

(Add Dashboard.png here)

---

## Azure Data Factory Pipeline

(Add Pipeline.png here)

---

## Pipeline Execution

(Add Pipeline_Run.png here)

---

## Architecture Diagram

(Add Architecture.png here)

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Azure Data Factory
- Azure Data Lake Storage
- Azure Databricks
- Apache Spark
- Data Transformation
- ETL Pipeline Development
- Interactive Dashboard Development
- Power BI Data Visualization

---

# 👩‍💻 Author

**Tashu Gupta**

B.Tech (Computer Science Engineering)

Swami Keshvanand Institute of Technology, Management & Gramothan (SKIT), Jaipur

---

# ⭐ Future Enhancements

- Real-time data ingestion
- Predictive attrition analysis using Machine Learning
- Automated email alerts
- Incremental data loading
- Azure Synapse Analytics integration

---

# 📜 License

This project is created for educational and learning purposes.
