# Databricks notebook source
# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Employee Attrition & HR Analytics
# MAGIC ### 
# MAGIC ### Notebook 1 : 01_raw_to_bronze
# MAGIC
# MAGIC ### Objective :
# MAGIC - Read HR dataset (CSV) from Azure Data Lake Storage Gen2 Raw Layer
# MAGIC - Verify dataset structure and schema
# MAGIC - Convert CSV data into Delta format
# MAGIC - Store raw data in Bronze Layer
# MAGIC
# MAGIC
# MAGIC Author: Tashu Gupta

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.hranalyticsadls031.dfs.core.windows.net",
    "<YOUR_STORAGE_KEY>"
)

# COMMAND ----------

raw_path = "abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(raw_path)

# COMMAND ----------

df.show(10)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

print("Total Records :", df.count())
print("Total Columns :", len(df.columns))

# COMMAND ----------

bronze_path = "abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/bronze/employee_raw"

df.write \
    .format("delta") \
    .mode("overwrite") \
    .save(bronze_path)

print("Bronze Layer Created Successfully!")