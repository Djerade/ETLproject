# 🛒 Projet ETL E-commerce vers un Data Lakehouse

Ce projet implémente un pipeline **ETL** pour une plateforme e-commerce, en utilisant **Apache Spark**, **Delta Lake**, **Apache Airflow** et **Hive Metastore**. L’objectif est de consolider des données issues de plusieurs sources (CSV, JSON, MySQL) vers un **data lakehouse** structuré pour des analyses avancées.

---

## 📦 Objectifs du projet

- Extraire des données clients, produits et ventes.
- Nettoyer et transformer les données en un schéma en étoile (star schema).
- Stocker les données en format **Delta** partitionné pour des performances optimales.
- Orchestrer les traitements avec **Airflow**.
- Mettre en place une base solide pour la BI ou le machine learning.

---

## 📁 Structure du projet

/ecommerce-etl-pipeline/
├── dags/ # DAGs Airflow
│ └── etl_pipeline.py
├── config/
│ └── mysql_config.json # Config de connexion MySQL
├── data/ # Données brutes
│ ├── clients.csv
│ ├── produits.json
│ └── ventes.csv
├── spark_jobs/ # Scripts Spark
│ ├── extract_transform.py
│ └── load_to_delta.py
├── lakehouse/ # Data Lakehouse Delta
│ └── delta_tables/
├── notebooks/
│ └── analyse_delta_lake.ipynb
├── docker-compose.yml
├── requirements.txt
└── README.md

---

## ⚙️ Technologies utilisées

- [Apache Spark](https://spark.apache.org/)
- [Apache Airflow](https://airflow.apache.org/)
- [Delta Lake](https://delta.io/)
- [Hive Metastore](https://cwiki.apache.org/confluence/display/Hive/AdminManual+MetastoreAdmin)
- Python 3.10
- Docker / Docker Compose

---
