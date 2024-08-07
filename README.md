# stock_fetcher
uvicorn main:app --reload


# 使用方法
resolution = D  => 每日
start_date, end_date => 使用 UNIX 時間戳

http://127.0.0.1:8000?resolution=D&start_date=1714579200&end_date=1725033600