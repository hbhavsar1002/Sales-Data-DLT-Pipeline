import dlt
from pyspark.sql.functions import col

# Transforming Sales data
@dlt.view(
    name='sales_view'
)
def sales_view():
    df = spark.readStream.table('sales_stream')
    df = df.withColumn("total_amount",col('quantity') * col('amount'))
    return df

# Creating Destination Silver Table
dlt.create_streaming_table(
    name='sales_transform'
)

dlt.create_auto_cdc_flow(
    target='sales_transform',
    source='sales_view',
    keys=['sales_id'],
    sequence_by='sale_timestamp',
    ignore_null_updates = False,
    apply_as_deletes = None,
    apply_as_truncates = None,
    column_list = None,
    except_column_list = None,
    stored_as_scd_type = 1,
    track_history_column_list = None,
    track_history_except_column_list = None,
    name = None,
    once = False
)