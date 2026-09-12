from pyspark import pipelines as dp
from pyspark.sql.functions import (
    count,
    sum,
    avg,
    round
)


@dp.materialized_view(
    name="goodcabs.gold.city_metrics"
)
def city_metrics():

    df = spark.read.table(
        "goodcabs.gold.gold_fact_trips"
    )

    result = (
        df.groupBy(
            "city_id",
            "city_name"
        )
        .agg(
            count("trip_id").alias("total_rides"),

            round(
                sum("sales_amount"),
                2
            ).alias("total_revenue"),

            round(
                avg("passenger_rating"),
                2
            ).alias("avg_passenger_rating"),

            round(
                avg("driver_rating"),
                2
            ).alias("avg_driver_rating")
        )
    )

    return result