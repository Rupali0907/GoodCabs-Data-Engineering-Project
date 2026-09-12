from pyspark import pipelines as dp
from pyspark.sql.functions import current_timestamp, col


@dp.table(
    name="goodcabs.bronze.trips"
)
def trips():

    df = (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .option("cloudFiles.inferColumnTypes", "true")
        .option("cloudFiles.schemaEvolutionMode", "rescue")
        .load(
            "/Workspace/Users/rupali93358@gmail.com/GoodCabs_Project/data/trips"
        )
    )

    # Clean invalid column name
    df = df.withColumnRenamed(
        "distance_travelled(km)",
        "distance_travelled_km"
    )

    df = (
        df
        .withColumn(
            "source_file",
            col("_metadata.file_path")
        )
        .withColumn(
            "ingest_timestamp",
            current_timestamp()
        )
    )

    return df