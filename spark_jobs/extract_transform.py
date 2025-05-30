from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, dayofweek, expr

# Crée une session Spark avec support Delta Lake
spark = SparkSession.builder \
    .appName("EcommerceETLExtractTransform") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# === 1. Lecture des données brutes ===

clients = spark.read.option("header", True).csv("data/clients.csv")
produits = spark.read.option("multiline", "true").json("data/produits.json")
ventes = spark.read.option("header", True).csv("data/ventes.csv")

# Cast des colonnes
ventes = ventes.withColumn("quantite", col("quantite").cast("int")) \
               .withColumn("produit_id", col("produit_id").cast("int")) \
               .withColumn("client_id", col("client_id").cast("int")) \
               .withColumn("date", col("date").cast("date"))

produits = produits.withColumn("produit_id", col("produit_id").cast("int")) \
                   .withColumn("prix", col("prix").cast("double"))

clients = clients.withColumn("client_id", col("client_id").cast("int"))

# === 2. Jointures ===

jointure = ventes \
    .join(produits, on="produit_id", how="left") \
    .join(clients, on="client_id", how="left")

# === 3. Ajout des colonnes enrichies ===

jointure = jointure.withColumn("revenu", col("prix") * col("quantite")) \
                   .withColumn("annee", year(col("date"))) \
                   .withColumn("mois", month(col("date"))) \
                   .withColumn("jour_semaine", dayofweek(col("date")))

# === 4. Sauvegarde au format Parquet temporaire ===

jointure.write.mode("overwrite").parquet("lakehouse/clean_data/ventes_enrichies")

print("✅ Transformation terminée et sauvegardée dans lakehouse/clean_data/")

spark.stop()
