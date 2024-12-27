from twitterTrends.models import trends_collection
from datetime import datetime

def store_trends_in_DB(trends):
    try:
        trend_data = {
            'unique_id': str(datetime.now().timestamp()),
            'nameOfTrend1': trends[0],
            'nameOfTrend2': trends[1],
            'nameOfTrend3': trends[2],
            'nameOfTrend4': trends[3],
            'nameOfTrend5': trends[4],
        }

        trends_collection.insert_one(trend_data)
        print(f"Uploaded to DB: {trend_data}")
        return True
    
    except Exception as e:
        print(f"An error occured uploading to DB: {e}")
        return False