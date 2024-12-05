from fastapi import APIRouter
from graphql_client import query_uniswap
import json
from redis_client import set_cache, get_cache

router = APIRouter()

@router.get("/swaps")
def get_recent_swaps():
    query = """
    {
      swaps(
        orderBy: timestamp, 
        where: {timestamp_gt: TIMESTAMP_4_HOURS_AGO, amountUSD_gt: 10000}
      ) {
        id
        timestamp
        amountUSD
        pair {
          token0 { symbol }
          token1 { symbol }
        }
      }
    }
    """
    result = query_uniswap(query)
    return json.loads(result)["data"]["swaps"]

@router.get("/eth_price")
def get_eth_price():
    cache_key = "eth_price"
    cached_price = get_cache(cache_key)

    if cached_price:
        return {"ethPrice": cached_price}

    query = """
    {
      bundle(id: "1") {
        ethPrice
      }
    }
    """
    result = query_uniswap(query)
    eth_price = json.loads(result)["data"]["bundle"]["ethPrice"]
    set_cache(cache_key, eth_price)
    return {"ethPrice": eth_price}
