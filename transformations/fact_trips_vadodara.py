from pyspark import pipelines as dp


@dp.materialized_view(
    name="goodcabs.gold.fact_trips_vadodara"
)
def fact_trips_vadodara():

    df = spark.read.table("goodcabs.gold.gold_fact_trips")

    df = df.filter("city_id = 'GJ02'")

    return df