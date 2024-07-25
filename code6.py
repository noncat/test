from pyspark.sql import SparkSession
from pyspark.sql.functions import length, substring

spark = SparkSession.builder \
    .appName("ContractsByRegion") \
    .getOrCreate()

orders_csv_path = "/home/noncat/Документы/DO/int_cert/orders.csv"
contracts_csv_path = "/home/noncat/Документы/DO/int_cert/contracts.csv"
output_csv_path = "/home/noncat/Документы/DO/int_cert/contracts_by_region_export_pyspark"

orders_df = spark.read.csv(orders_csv_path, header=True, inferSchema=True)
contracts_df = spark.read.csv(contracts_csv_path, header=True, inferSchema=True)

orders_df.createOrReplaceTempView("orders")
contracts_df.createOrReplaceTempView("contracts")

query = """
    WITH regions AS (
        SELECT
            SUBSTR(org_inn, 1, 2) AS region_code,
            id AS order_id
        FROM orders
    ),
    contracts_with_regions AS (
        SELECT
            r.region_code,
            c.id AS contract_id,
            c.suppl_inn
        FROM contracts c
        JOIN regions r ON c.ord_id = r.order_id
    )
    SELECT
        region_code,
        COUNT(*) AS contract_count
    FROM contracts_with_regions
    WHERE LENGTH(CAST(suppl_inn AS STRING)) = 12
    GROUP BY region_code
    ORDER BY contract_count DESC
"""

result_df = spark.sql(query)

result_df.show()

result_df.coalesce(1).write.csv(output_csv_path, header=True, mode='overwrite')

spark.stop()

#Ура работает! Выводит столько же строк, как и в postgresql. Вывод информации в консоль и экспорт в CSV файл в папку contracts_by_region_export_pyspark.