# Databricks notebook source
# MAGIC %md
# MAGIC ## 
# MAGIC ## Employee Attrition & HR Analytics
# MAGIC
# MAGIC Notebook 3 : 03_silver_to_gold
# MAGIC
# MAGIC ### Objective
# MAGIC - Read cleaned HR data from Silver layer
# MAGIC
# MAGIC - Create business-ready analytical datasets
# MAGIC - Store curated datasets in Gold layer
# MAGIC
# MAGIC Author: Tashu Gupta

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.hranalyticsadls031.dfs.core.windows.net",
    "<YOUR_STORAGE_KEY>"
)

# COMMAND ----------

silver_path = "abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/silver/employee_cleaned"

df = spark.read.format("delta").load(silver_path)

# COMMAND ----------

df.show(5)

# COMMAND ----------

#First Transformation: Salary Band Analysis

from pyspark.sql.functions import when, col

df = df.withColumn(
    "SalaryBand",
    when(col("MonthlyIncome") < 5000, "Low")
    .when((col("MonthlyIncome") >= 5000) & (col("MonthlyIncome") < 10000), "Medium")
    .otherwise("High")
)

# COMMAND ----------

df.select("MonthlyIncome", "SalaryBand").show(10)

# COMMAND ----------

# Transformation 2: Department-wise Attrition Analysis
from pyspark.sql.functions import count, sum, when, round

department_attrition = (
    df.groupBy("Department")
      .agg(
          count("*").alias("TotalEmployees"),
          sum(when(col("Attrition") == "Yes", 1).otherwise(0)).alias("EmployeesLeft")
      )
      .withColumn(
          "AttritionRatePercent",
          round((col("EmployeesLeft") / col("TotalEmployees")) * 100, 2)
      )
)

department_attrition.show()

# COMMAND ----------

# Transformation 3: Overtime vs Attrition

overtime_analysis = (
    df.groupBy("OverTime", "Attrition")
      .count()
)

overtime_analysis.show()

# COMMAND ----------

# Transformation 4: Job Role Analysis
jobrole_analysis = (
    df.groupBy("JobRole", "Attrition")
      .count()
)

jobrole_analysis.show()

# COMMAND ----------

# Transformation 5: Work-Life Balance Analysis
worklife_analysis = (
    df.groupBy("WorkLifeBalance", "Attrition")
      .count()
)

worklife_analysis.show()

# COMMAND ----------

# Transformation: Age Group Analysis
from pyspark.sql.functions import when

df = df.withColumn(
    "AgeGroup",
    when(col("Age") < 30, "Young")
    .when((col("Age") >= 30) & (col("Age") < 45), "Mid-Career")
    .otherwise("Senior")
)

df.select("Age", "AgeGroup").show(10)

# COMMAND ----------

# Age Group vs Attrition
agegroup_analysis = (
    df.groupBy("AgeGroup", "Attrition")
      .count()
)

agegroup_analysis.show()

# COMMAND ----------

# Next Transformation: Gender Analysis
gender_analysis = (
    df.groupBy("Gender", "Attrition")
      .count()
)

gender_analysis.show()

# COMMAND ----------

# Transformation: Education Field Analysis
education_analysis = (
    df.groupBy("EducationField", "Attrition")
      .count()
)

education_analysis.show()

# COMMAND ----------

# Transformation: Performance Rating Analysis
performance_analysis = (
    df.groupBy("PerformanceRating", "Attrition")
      .count()
)

performance_analysis.show()

# COMMAND ----------

department_attrition.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/department_attrition")

# COMMAND ----------

salary_analysis = (
    df.groupBy("SalaryBand", "Attrition")
      .count()
)

salary_analysis.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/salary_analysis")

# COMMAND ----------

overtime_analysis.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/overtime_analysis")

# COMMAND ----------

jobrole_analysis.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/jobrole_analysis")

# COMMAND ----------

worklife_analysis.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/worklife_analysis")

# COMMAND ----------

agegroup_analysis.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/agegroup_analysis")

# COMMAND ----------

gender_analysis.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/gender_analysis")

# COMMAND ----------

education_analysis.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/education_analysis")

# COMMAND ----------

performance_analysis.write \
    .format("delta") \
    .mode("overwrite") \
    .save("abfss://hr-data@hranalyticsadls031.dfs.core.windows.net/gold/performance_analysis")

# COMMAND ----------

print("======================================")
print("HR Gold Layer Created Successfully!")
print("Business datasets saved to Gold Layer.")
print("======================================")