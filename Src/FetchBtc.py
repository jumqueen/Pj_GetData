import os
import requests
from datetime import datetime
import pytz
from utils.helpers import get_1530_jst_timestamp, get_jst_now, save_to_csv

def fetch_btc():
    # 環境変数からモードを取得（デフォルトは manual）
    mode = os.environ.get('FETCH_MODE', 'manual')
    jst = pytz.timezone('Asia/Tokyo')

    if mode == 'scheduled':
        # 15:30のタイムスタンプを取得
        target_ts = get_1530_jst_timestamp()
        label = "Scheduled (15:30 JST)"
    else:
        # 現在時刻のタイムスタンプを取得
        target_ts = int(get_jst_now().timestamp())
        label = "Manual (Current Time)"

    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
    params = {
        'vs_currency': 'usd',
        'from': target_ts - 600,
        'to': target_ts + 600
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'prices' in data and data['prices']:
        closest_data = min(data['prices'], key=lambda x: abs(x[0] - target_ts * 1000))
        price = closest_data[1]
        dt_str = datetime.fromtimestamp(closest_data[0] / 1000, jst).strftime('%Y-%m-%d %H:%M:%S')
        
        save_to_csv("bitcoin_prices.csv", [dt_str, price])
        print(f"[{label}] Recorded BTC price at {dt_str}: ${price}")
    else:
        print(f"[{label}] Failed to fetch data.")

if __name__ == "__main__":
    fetch_btc()