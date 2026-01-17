import os
import csv
from datetime import datetime, time
import pytz

def get_jst_now():
    return datetime.now(pytz.timezone('Asia/Tokyo'))

def get_1530_jst_timestamp():
    """当日の日本時間15:30のUNIXタイムスタンプを返す"""
    jst = pytz.timezone('Asia/Tokyo')
    now = get_jst_now()
    # 今日の15:30を作成
    target_dt = jst.localize(datetime.combine(now.date(), time(15, 30)))
    return int(target_dt.timestamp())

def save_to_csv(filename, data_row):
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", filename)
    file_exists = os.path.isfile(file_path)
    
    with open(file_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['datetime_jst', 'price_usd'])
        writer.writerow(data_row)