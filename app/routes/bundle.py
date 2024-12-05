@router.get("/eth_price")
def get_eth_price():
    cache_key = "eth_price"
    price = cache_get(cache_key)

    if not price:
        query = """
        {
          bundle(id: "1") {
            ethPrice
          }
        }
        """
        result = query_uniswap(query)
        price = json.loads(result)['data']['bundle']['ethPrice']
        cache_setex(cache_key, price, 30)

    return {"ethPrice": price}
