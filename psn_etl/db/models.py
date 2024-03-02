from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from .db import Base

class TrophyTitleModel(Base):
    __tablename__ = "trophy_titles"

    id = Column(Integer, primary_key=True)
    psn_username = Column(String(255), nullable=False)
    game_id = Column(String(255), nullable=False)
    game_name = Column(String(255), nullable=False)
    platform = Column(String(255), nullable=False)
    progress = Column(Integer, default=0)
    last_played = Column(DateTime, nullable=True)
    trophies_version = Column(Float(2), nullable=False)
    game_icon_url = Column(String(255), nullable=True)
    has_extra_trophies = Column(Boolean, default=False)
    earned_silver = Column(Integer, default=0)
    earned_bronze = Column(Integer, default=0)
    earned_gold = Column(Integer, default=0)
    earned_platinum = Column(Integer, default=0)
    total_silver = Column(Integer, default=0)
    total_bronze = Column(Integer, default=0)
    total_gold = Column(Integer, default=0)
    total_platinum = Column(Integer, default=0)