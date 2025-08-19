import dlt

# Expectations
order_rules ={
    "rule_1": "sales_id IS NOT NULL",
    "rule_2": "product_id IS NOT NULL",
    "rule_3": "customer_id IS NOT NULL",
    "rule_4": "quantity > 0",
    "rule_5": "amount > 0"
}

# Empty Streaming Table
dlt.create_streaming_table(
    name='sales_stream',
    expect_all_or_drop=order_rules
)

# Creating East Sales Flow
@dlt.append_flow(target='sales_stream')
def east_sales():
    df = spark.readStream.table('mydb.source.sales_east')
    return df

# Creating West Sales Flow
@dlt.append_flow(target='sales_stream')
def west_sales():
    df = spark.readStream.table('mydb.source.sales_west')
    return df

