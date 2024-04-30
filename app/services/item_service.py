from fastapi import HTTPException
from typing import Dict, Any
import plotly.graph_objects as go
import pandas as pd
import requests


def get_stock_service(query_string: str) -> Dict[str, Any]:
    base_url: str = 'https://ws.api.cnyes.com/ws/api/v1/charting/history'
    url: str = f"{base_url}?{query_string}"
    headers = {'Accept': 'application/json'}

    try:
        # 使用 GET 请求调用 API
        response = requests.get(url, headers=headers)

        # 检查请求是否成功
        if response.status_code == 200:
            # 将响应的 JSON 内容解析为字典
            data: Dict[str, Any] = response.json()
            return data["data"]
        else:
            # 如果 API 响应的 HTTP 状态码不是 200，则抛出 HTTPException
            raise HTTPException(status_code=response.status_code,
                                detail="Failed to fetch data from external API")

    except requests.exceptions.RequestException as e:
        # 捕捉 requests 库可能抛出的所有异常
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # 捕捉其他所有未预料的异常
        raise HTTPException(
            status_code=500, detail=f"{e}")


def data_process(data: Dict[str, Any]) -> None:
    df = pd.DataFrame({
        # 假设 data["t"] 是 UNIX 时间戳，需要转换为 datetime
        "time": pd.to_datetime(data["t"], unit='s'),
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "close": data["c"],
        "volume": data["v"],
        "vwap": data["vwap"]
    })
    print(df)
    fig = go.Figure(data=[go.Candlestick(
        x=df["time"],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])

    fig.update_layout(title='2330',
                      xaxis_title='日期',
                      yaxis_title='價格',
                      autosize=False,
                      width=1920,
                      height=1080)

    fig.write_image(r"D:\life_ease\stock_fetcher\app\2330.png")

    # print(df)
