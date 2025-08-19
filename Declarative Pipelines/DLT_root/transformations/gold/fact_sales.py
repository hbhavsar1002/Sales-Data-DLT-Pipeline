import dlt

# Create Products stream table
dlt.create_streaming_table(
    name='fact_sales'
)

# auto cdc flow
dlt.create_auto_cdc_flow(
    target='fact_sales',
    source='sales_view',
    keys=['sales_id'],
    sequence_by='sale_timestamp',
    ignore_null_updates = False,
    apply_as_deletes = None,
    apply_as_truncates = None,
    column_list = None,
    except_column_list = None,
    stored_as_scd_type = 2,
    track_history_column_list = None,
    track_history_except_column_list = None,
    name = None,
    once = False

)