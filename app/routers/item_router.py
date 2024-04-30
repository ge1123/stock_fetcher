from typing import Optional

from pydantic import BaseModel
from fastapi import APIRouter, Query
from services.item_service import get_stock_service
from services.item_service import data_process
from typing import Dict, Any

router = APIRouter()


class GetStockRequest(BaseModel):
    resolution: Optional[str] = Query(None, alias='resolution')
    symbol: Optional[str] = Query(None, alias='symbol')
    start_date: Optional[str] = Query(None, alias='start_date')
    end_date: Optional[str] = Query(None, alias='end_date')


@router.get("/")
def get_stock(resolution: Optional[str] = None, symbol: Optional[str] = None,
              start_date: Optional[str] = None, end_date: Optional[str] = None) -> dict:

    query_params = {}
    if resolution:
        query_params['resolution'] = resolution
    if symbol:
        query_params['symbol'] = symbol
    if end_date:
        query_params['from'] = end_date
    if start_date:
        query_params['to'] = start_date

    query_string = '&'.join(f"{key}={value}" for key,
                            value in query_params.items())

    result: Dict[str, Any] = get_stock_service(query_string)

    data_process(result)

    return (result)
