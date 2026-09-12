from pyspark import pipelines as dp


@dp.materialized_view(
    name="goodcabs.gold.fact_trips_jaipur"
)
def fact_trips_jaipur():

    df = spark.read.table(
        "goodcabs.gold.gold_fact_trips"
    )

    return df.filter("city_id = 'RJ01'")