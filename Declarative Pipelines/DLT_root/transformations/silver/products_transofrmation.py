import dlt
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

# Create Transform products view
@dlt.view(
    name='products_view'
)
def products_view():
  df = dlt.read_stream('products_stream')
  df = df.withColumn('price',col('price').cast(IntegerType()))
  return df


# Create Silver Products Stream Table
dlt.create_streaming_table(
    name='products_transform'
)

dlt.create_auto_cdc_flow(
    target='products_transform',
    source='products_view',
    keys=['product_id'],
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

