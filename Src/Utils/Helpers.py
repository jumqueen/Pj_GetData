import os
import csv
from datetime import datetime
import pytz

def get_1500_jst_timestamp():
    """当日の日本時間15:00のUNIXタイムスタンプを返す"""
    jst = pytz.timezone('Asia/Tokyo')
    now = datetime.now(jst)
    target_dt = jst.localize(datetime.combine(now.date(), datetime.min.time().replace(hour=15)))
    return int(target_dt.timestamp())

def save_to_csv(filename, data_row):
    """data/ディレクトリにCSVを保存する"""
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", filename)
    file_exists = os.path.isfile(file_path)
    
    with open(file_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['datetime_jst', 'price_usd'])
        writer.writerow(data_row)