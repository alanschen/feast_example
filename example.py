# This is an example feature definition file

from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, ValueType
from feast.data_source import FileSource

# 1 Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.
cancel_stats = FileSource(
    path="/Users/alanschen/Arize/tutorials/feast-tutorial/feature_repo/data/cancel_stats.parquet",
    event_timestamp_column="datetime",
    created_timestamp_column="created",
)

basic_stats = FileSource(
    path="/Users/alanschen/Arize/tutorials/feast-tutorial/feature_repo/data/user_stats.parquet",
    event_timestamp_column="datetime",
    created_timestamp_column="created",
)

# 2 Define an entity for the driver. You can think of entity as a primary key used to
# fetch features.
user = Entity(name="user_id", value_type=ValueType.INT64, description="user id",)

# 3 Our parquet files contain sample data that includes a driver_id column, timestamps and
# three feature column. Here we define a Feature View that will allow us to serve this
# data to our model online.

user_cancel_stats_view = FeatureView(
    name="user_cancel_stats",
    entities=["user_id"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="current_24_hr_cancels", dtype=ValueType.INT32),
        Feature(name="avg_cancels", dtype=ValueType.FLOAT),
    ],
    online=True,
    input=cancel_stats, # the feast.data_source defined in step 1
    tags={},
)

user_basic_stats_view = FeatureView(
    name="user_basic_stats",
    entities=["user_id"],
    ttl=Duration(seconds=86400 * 1),
    features=[
        Feature(name="transaction_price", dtype=ValueType.FLOAT),
        Feature(name="interest_rate", dtype=ValueType.FLOAT),
        Feature(name="annual_income", dtype=ValueType.INT32),
    ],
    online=True,
    input=basic_stats, # the feast.data_source defined in step 1
    tags={},
)