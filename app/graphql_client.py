from graphqlclient import GraphQLClient

UNISWAP_ENDPOINT = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"

client = GraphQLClient(UNISWAP_ENDPOINT)

def query_uniswap(query, variables=None):
    response = client.execute(query, variables)
    return response
