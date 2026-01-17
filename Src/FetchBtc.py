import requests
from datetime import datetime
import pytz
from utils.helpers import get_1500_jst_timestamp, save_to_csv

def fetch_btc_at_1500():
    target_ts = get_1500_jst_timestamp()
    
    # 15:00の前後10分間のデータを取得
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
    params = {
        'vs_currency': 'usd',
        'from': target_ts - 600,
        'to': target_ts + 600
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'prices' in data and len(data['prices']) > 0:
        # 最も15:00に近いデータを抽出
        closest_data = min(data['prices'], key=lambda x: abs(x[0] - target_ts * 1000))
        price = closest_data[1]
        
        # JST形式の文字列に変換
        jst = pytz.timezone('Asia/Tokyo')
        dt_str = datetime.fromtimestamp(closest_data[0] / 1000, jst).strftime('%Y-%m-%d %H:%M:%S')
        
        save_to_csv("bitcoin_prices.csv", [dt_str, price])
        print(f"Recorded BTC price at {dt_str}: ${price}")
    else:
        print("Failed to fetch data or no data available for the range.")

if __name__ == "__main__":
    fetch_btc_at_1500()