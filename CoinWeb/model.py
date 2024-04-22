from sqlalchemy import Column, DateTime, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from CoinWeb import db
Base = db.Model

class BTCUSDT_1d(Base):
    __tablename__ = 'BTCUSDT_1d_latest'
    timestamp = Column(DateTime, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)
    close_time = Column(DateTime)
    quote_asset_volume = Column(Float)
    number_of_trades = Column(BigInteger)
    taker_buy_base_asset_volume = Column(Float)
    taker_buy_quote_asset_volume = Column(Float)
    ignore = Column(Float)
    
class Treasury20Y(Base):
    __tablename__ = 'treasury_20y'
    Date = Column(DateTime, primary_key=True)
    Yr20 = Column('20 Yr',Float, nullable=True)
    Yr10 = Column('10 Yr',Float, nullable=True)

class WtiOilPrice(Base):
    __tablename__ = 'wti_oil_price'
    DATE = Column(DateTime, primary_key=True)
    DCOILWTICO = Column(Float, nullable=True)
    
class Vix(Base):
    __tablename__ = 'vix'
    date = Column(DateTime, primary_key=True)
    open = Column(Float, nullable=True)
    high = Column(Float, nullable=True)
    low = Column(Float, nullable=True)
    close = Column(Float, nullable=True)
    adj_close = Column('adj close', Float, nullable=True)


class HistCoin(Base):
    __tablename__ = 'hist_coin'

    date = Column(DateTime, primary_key=True)
    open = Column(Float, nullable=True)
    high = Column(Float, nullable=True)
    low = Column(Float, nullable=True)
    close = Column(Float, nullable=True)
    volume = Column(BigInteger, nullable=True)
    dividends = Column(Float, nullable=True)
    stock_splits = Column('stock splits',Float, nullable=True)

class HistMstr(Base):
    __tablename__ = 'hist_mstr'

    date = Column(DateTime, primary_key=True)
    open = Column(Float, nullable=True)
    high = Column(Float, nullable=True)
    low = Column(Float, nullable=True)
    close = Column(Float, nullable=True)
    volume = Column(BigInteger, nullable=True)
    dividends = Column(Float, nullable=True)
    stock_splits = Column('stock splits',Float, nullable=True)

class GOLDDXYSNP(Base):
    __tablename__ = 'GOLDDXYSNP'

    Date = Column(DateTime, primary_key=True)
    Gold = Column(Float, nullable=True)
    Dollar = Column(Float, nullable=True)
    SnP = Column(Float, nullable=True)
    
    