from pyspark.sql import SparkSession

# Initialiser la session Spark avec les extensions Delta
spark = SparkSession.builder \
    .appName("EcommerceETLLoadDelta") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# === 1. Charger les données transformées (Parquet) ===

df = spark.read.parquet("lakehouse/clean_data/ventes_enrichies")

# === 2. Écrire dans un dossier Delta Lake partitionné par catégorie et année ===

df.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("categorie", "annee") \
    .save("lakehouse/delta_tables/ventes")

print("✅ Données chargées dans Delta Lake partitionnées par catégorie et année.")

spark.stop()
