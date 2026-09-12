from pyspark import pipelines as dp
from pyspark.sql.functions import col


@dp.materialized_view(
    name="goodcabs.gold.gold_fact_trips"
)
def gold_fact_trips():

    trips = spark.read.table("goodcabs.silver.trips_cdc")
    city = spark.read.table("goodcabs.silver.city")
    calendar = spark.read.table("goodcabs.silver.calendar")

    df = (
        trips.alias("t")
        .join(
            city.alias("c"),
            col("t.city_id") == col("c.city_id"),
            "left"
        )
        .join(
            calendar.alias("cal"),
            col("t.date") == col("cal.date"),
            "left"
        )
        .select(
            col("t.*"),
            col("c.city_name"),
            col("cal.date_key"),
            col("cal.year"),
            col("cal.month"),
            col("cal.day"),
            col("cal.weekday"),
            col("cal.month_name"),
            col("cal.quarter"),
            col("cal.week"),
            col("cal.is_weekend")
        )
    )

    return df