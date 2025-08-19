import dlt

# Expectations
product_rules = {
    "rule_1": "product_id IS NOT NULL",
    "rule_2": "product_name IS NOT NULL",
    "rule_3": "price > 0"
}

# Creating Products Stream Table
@dlt.table(
    name='products_stream'
)
@dlt.expect_all_or_drop(product_rules)
def products_stream():
    df = spark.readStream.table("mydb.source.products")
    return df