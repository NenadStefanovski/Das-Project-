# utils/storage.py
import os
import csv

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

MASTER_FILE = os.path.join(DATA_DIR, "cryptocurrency_binance_all.csv")

def append_records_to_csv(symbol, records):
    
    # Appends OHLCV records for ALL coins into ONE CSV file.
    
    file_exists = os.path.exists(MASTER_FILE)

    with open(MASTER_FILE, "a", newline="") as f:
        w = csv.writer(f)

        # Add header once
        if not file_exists:
            w.writerow([
                "date", "symbol", 
                "open", "high", "low", "close", "volume"
            ])

        for r in records:
            w.writerow([
                r.get("date"),
                symbol,
                r.get("open"),
                r.get("high"),
                r.get("low"),
                r.get("close"),
                r.get("volume")
            ])
