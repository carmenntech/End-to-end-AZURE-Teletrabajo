# Databricks notebook source
# MAGIC %fs ls /FileStore/tables

# COMMAND ----------

# MAGIC %md
# MAGIC Creacion del RDD y del DF

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, trim
import pandas as pd
import numpy as np
from pyspark.sql.types import *

spark = SparkSession.builder.appName("EjemploPySpark").getOrCreate()

df = spark.read.option("sep",";").option("header", "true").option("inferSchema", "true").csv("dbfs:/FileStore/tables/71035.csv")





# COMMAND ----------

# MAGIC %md
# MAGIC Castear y renombrar las columnas 

# COMMAND ----------



df = df.withColumnRenamed('Comunidades y ciudades autónomas','ccaa')\
        .withColumnRenamed('Principales variables','variables')\
        .withColumnRenamed('Agrupación de actividad','sectores')\
        .withColumnRenamed('Total','porcentaje')\

# Limpiar la columna `Total`: eliminar espacios y reemplazar comas con puntos
df = df.withColumn("porcentaje", regexp_replace(trim(col("porcentaje")), ",", "."))

# Convertir `Total` a `float` después de la limpieza
df = df.withColumn("porcentaje", col("porcentaje").cast(FloatType()))

# Mostrar el esquema y el contenido del DataFrame para verificar
df.printSchema()
df.show(10)


# COMMAND ----------

# MAGIC %md
# MAGIC Observamos la columna Sectores y CCAA (comunidad autonoma)

# COMMAND ----------

df.groupBy('sectores').count().display()
df.groupBy('ccaa').count().display()

# COMMAND ----------

pivot_df = df.groupBy("ccaa").pivot("sectores").agg({"porcentaje": "first"}).show()

# COMMAND ----------

Creamos la delta table

# COMMAND ----------

spark.sql("CREATE DATABASE IF NOT EXISTS teletrabajodb")
spark.sql("USE teletrabajodb")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS teletrabajo_sectores_ccaa(
    ccaa string,
    variables string,
    sectores string,
    porcentaje float
)
USING DELTA
LOCATION '{teletrabajo_sectores_ccaa}'
""")

teletrabajodb.write.format("delta").mode("overwrite").save(teletrabajo_sectores_ccaa)

