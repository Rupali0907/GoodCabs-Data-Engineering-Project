from pyspark import pipelines as dp
from pyspark.sql.functions import (
    col,
    year,
    month,
    dayofmonth,
    dayofweek,
    date_format,
    quarter,
    weekofyear,
    when,
    lit,
    sequence,
    explode,
    to_date
)


@dp.materialized_view(
    name="goodcabs.silver.calendar"
)
def calendar():

    start_date = "2024-01-01"
    end_date = "2025-12-31"

    df = spark.sql(f"""
        SELECT explode(
            sequence(
                to_date('{start_date}'),
                to_date('{end_date}'),
                interval 1 day
            )
        ) AS date
    """)

    df = (
        df
        .withColumn("date_key", date_format(col("date"), "yyyyMMdd").cast("int"))
        .withColumn("year", year(col("date")))
        .withColumn("month", month(col("date")))
        .withColumn("day", dayofmonth(col("date")))
        .withColumn("weekday", dayofweek(col("date")))
        .withColumn("month_name", date_format(col("date"), "MMMM"))
        .withColumn("quarter", quarter(col("date")))
        .withColumn("week", weekofyear(col("date")))
        .withColumn(
            "is_weekend",
            when(col("weekday").isin(1, 7), lit(True))
            .otherwise(lit(False))
        )
    )

    return df