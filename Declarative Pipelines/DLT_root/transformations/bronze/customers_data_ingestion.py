import dlt

# Expectations
customer_rules = {
    "rule_1": "customer_id IS NOT NULL",
    "rule_2": "customer_name IS NOT NULL"
}

# Creating Customers Stream Table
@dlt.table(
    name='customer_stream'
)
@dlt.expect_all_or_drop(customer_rules)
def customers_stream():
    df = spark.readStream.table("mydb.source.customers")
    return df