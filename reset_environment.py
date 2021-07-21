import pandas as pd
import os

def reset_environment():
    # 1 Reset data source
    pd.read_parquet('data/default_data.parquet').to_parquet('data/cancel_stats.parquet')
    # Reset online sqlite.db, 3 Reset registry
    online_store, registry = 'data/online_store.db', 'data/registry.db'
    if os.path.exists(online_store):
        os.remove(online_store)
        os.remove(registry)
    print("Environment has been reset")

if __name__ =='__main__':
    reset_environment()