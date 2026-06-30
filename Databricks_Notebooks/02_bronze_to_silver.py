# Databricks notebook source
# MAGIC %md
# MAGIC # Employee Attrition & HR Analytics
# MAGIC
# MAGIC ## Notebook 2: 02_bronze_to_silver
# MAGIC
# MAGIC
# MAGIC ### Objective
# MAGIC - Read HR dataset from Azure Data Lake Storage Gen2
# MAGIC - Verify schema
# MAGIC - Perform initial data quality checks
# MAGIC - Validate and clean the dataset
# MAGIC - Store cleaned data in Silver Delta Layer
# MAGIC
# MAGIC Author: Tashu Gupta

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.hranalyticsadls031.dfs.core.windows.net",
    "<YOUR_STORAGE_KEY>"
)

# COMMAND ----------

bronze_path = "abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/bronze/employee_raw"

df = spark.read \
    .format("delta") \
    .load(bronze_path)

# COMMAND ----------

df.show(10)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

print(f"Total Records: {df.count()}")
print(f"Total Columns: {len(df.columns)}")

# COMMAND ----------

df.describe().show()

# COMMAND ----------

from pyspark.sql.functions import col, count, when

missing_values = df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in df.columns
])

missing_values.show(vertical=True, truncate=False)

# COMMAND ----------

print("Total Records :", df.count())

print("Unique Records :", df.dropDuplicates().count())

# COMMAND ----------

df.groupBy("Attrition").count().show()

# COMMAND ----------

df.groupBy("Department").count().show()

# COMMAND ----------

silver_path = "abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/silver/employee_cleaned"

df.write \
    .format("delta") \
    .mode("overwrite") \
    .save(silver_path)

print("Data successfully written to Silver Layer (Delta)")