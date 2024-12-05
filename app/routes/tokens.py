from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Token
from database import get_db
from graphql_client import query_uniswap
import json

router = APIRouter()

@router.get("/fetch_tokens")
def fetch_tokens(db: Session = Depends(get_db)):
    query = """
    {
      tokens(orderBy: tradeVolumeUSD, orderDirection: desc) {
        id
        symbol
        totalSupply
        tradeVolumeUSD
        totalLiquidity
        untrackedVolumeUSD
      }
    }
    """
    result = json.loads(query_uniswap(query))
    tokens = result["data"]["tokens"]

    for token_data in tokens:
        token = db.query(Token).filter(Token.id == token_data['id']).first()
        if token:
            token.tradeVolumeUSD = token_data["tradeVolumeUSD"]
            token.totalLiquidity = token_data["totalLiquidity"]
            token.untrackedVolumeUSD = token_data["untrackedVolumeUSD"]
        else:
            token = Token(**token_data)
        db.add(token)
    db.commit()
    return {"message": "Tokens updated successfully!"}

@router.get("/tokens")
def get_tokens(sortBy: str, limit: int, page: int, db: Session = Depends(get_db)):
    offset = (page - 1) * limit
    tokens = db.query(Token).order_by(getattr(Token, sortBy).desc()).offset(offset).limit(limit).all()
    return tokens
