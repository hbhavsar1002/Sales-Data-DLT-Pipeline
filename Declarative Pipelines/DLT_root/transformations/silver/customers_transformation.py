import dlt
from pyspark.sql.functions import col, upper


#create customer view
@dlt.view(
    name='customers_view'
)
def customers_view():
    df = dlt.read_stream('customer_stream')
    df = df.withColumn('customer_name',upper(col('customer_name')))
    return df



#create customer stream table
dlt.create_streaming_table(
    name='customers_transform'
)

dlt.create_auto_cdc_flow(
    target='customers_transform',
    source='customers_view',
    keys=['customer_id'],
    sequence_by='last_updated',
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