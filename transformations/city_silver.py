from pyspark import pipelines as dp
from pyspark.sql.functions import current_timestamp


@dp.materialized_view(
    name="goodcabs.silver.city"
)
def city():

    df = spark.read.table("goodcabs.bronze.city")

    df = (
        df
        .withColumnRenamed(
            "ingest_timestamp",
            "bronze_ingest_timestamp"
        )
        .withColumn(
            "silver_processed_timestamp",
            current_timestamp()
        )
    )

    return df