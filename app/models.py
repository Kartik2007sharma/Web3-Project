from sqlalchemy import Column, String, Float, Integer
from database import Base

class Token(Base):
    __tablename__ = "tokens"
    id = Column(String, primary_key=True)
    symbol = Column(String)
    totalSupply = Column(Float)
    tradeVolumeUSD = Column(Float)
    totalLiquidity = Column(Float)
    untrackedVolumeUSD = Column(Float)

class Swap(Base):
    __tablename__ = "swaps"
    id = Column(String, primary_key=True)
    timestamp = Column(Integer)
    amountUSD = Column(Float)
    token0 = Column(String)
    token1 = Column(String)
