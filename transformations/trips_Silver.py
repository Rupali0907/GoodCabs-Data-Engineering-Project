from pyspark import pipelines as dp
from pyspark.sql.functions import current_timestamp


@dp.table(
    name="goodcabs.silver.trips"
)

@dp.expect(
    "valid_business_date",
    "date > '2020-01-01'"
)

@dp.expect(
    "valid_driver_rating",
    "driver_rating BETWEEN 1 AND 10"
)

@dp.expect(
    "valid_passenger_rating",
    "passenger_rating BETWEEN 1 AND 10"
)

def trips():

    df = spark.readStream.table("goodcabs.bronze.trips")

    df = (
        df
        .withColumnRenamed(
            "fare_amount",
            "sales_amount"
        )
        .withColumn(
            "silver_processed_timestamp",
            current_timestamp()
        )
    )

    return df