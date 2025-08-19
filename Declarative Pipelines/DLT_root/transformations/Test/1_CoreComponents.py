# import dlt

# # Create Streaming Table
# @dlt.table(
#     name = 'first_stream_table'
# )
# def first_stream_table():
#     df = spark.readStream.table('mydb.source.orders')
#     return df


# # Create Materialized View (Batch Table)
# @dlt.table(
#     name='first_mat_view'
# )
# def first_mat_view():
#     df = spark.read.table('mydb.source.orders')
#     return df


# # Create Batch View
# @dlt.view(
#     name='batch_view'
# )
# def batch_view():
#     df = spark.read.table('mydb.source.orders')
#     return df

# # Create Streaming View
# @dlt.view(
#     name='stream_view'
# )
# def stream_view():
#     df = spark.readStream.table('mydb.source.orders')
#     return df

