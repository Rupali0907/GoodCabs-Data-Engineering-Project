from pyspark import pipelines as dp
from pyspark.sql.functions import col


dp.create_streaming_table(
    name="goodcabs.silver.trips_cdc"
)


dp.create_auto_cdc_flow(
    target="goodcabs.silver.trips_cdc",
    source="goodcabs.silver.trips",
    keys=["trip_id"],
    sequence_by=col("silver_processed_timestamp"),
    stored_as_scd_type=1
)