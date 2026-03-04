import sqlite3
import pandas as pd
import json
from datetime import datetime

# 讀 SQLite → 轉 JSON/CSV
conn = sqlite3.connect('admissions.db')
df = pd.read_sql("SELECT * FROM jbcrc_notices", conn)

# 統計儀表板資料
stats = {
    'total': len(df),
    'y115': len(df[df.year == '115']),
    'schools': df['title'].str.split().str[0].nunique(),
    'last_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'recent': df.tail(10).to_dict('records')
}

# 儲存檔案
df.to_csv('admissions.csv', index=False, encoding='utf-8-sig')
with open('dashboard.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

print(f"✅ 產生檔案：")
print(f"   admissions.csv ({len(df)} 筆)")
print(f"   dashboard.json (統計：{stats['total']} 總筆/{stats['y115']} 115學年)")
