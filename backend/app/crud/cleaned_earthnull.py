from fastapi import HTTPException, status
from sqlalchemy.orm import Session ,load_only
from app.models.cleaned_earthnull import CleanedEarthNull
from app.schemas.cleaned_earthnull import CleanedEarthNullAttribute
from datetime import datetime


def insert_cleaned_earthnull(request:CleanedEarthNullAttribute, db:Session):
    db_cleaned_earthnull =CleanedEarthNull(cleaned_earthnull_station_id = request.cleaned_earthnull_station_id,
                       cleaned_earthnull_timestamp = request.cleaned_earthnull_timestamp,
                       cleaned_earthnull_lat = request.cleaned_earthnull_lat,
                       cleaned_earthnull_long = request.cleaned_earthnull_long,
                       cleaned_earthnull_pm25 = request.cleaned_earthnull_pm25,
                       cleaned_earthnull_pm10 = request.cleaned_earthnull_pm10,
                       cleaned_earthnull_wind_dir = request.cleaned_earthnull_wind_dir,
                       cleaned_earthnull_wind_speed = request.cleaned_earthnull_wind_speed,
                       cleaned_earthnull_RH = request.cleaned_earthnull_RH)
    db.add(db_cleaned_earthnull)
    db.commit()
    db.refresh(db_cleaned_earthnull)
    return db_cleaned_earthnull

def get_all_cleaned_earthnull(db:Session):
    return db.query(CleanedEarthNull).all()

def get_all_cleaned_earthnull_by_station(station_id:str, db:Session):
    return db.query(CleanedEarthNull).filter(CleanedEarthNull.cleaned_earthnull_station_id == station_id).order_by(CleanedEarthNull.cleaned_earthnull_timestamp.desc()).all()

def get_latest_cleaned_earthnull_by_station(station_id:str, db:Session):
    return db.query(CleanedEarthNull).filter(CleanedEarthNull.cleaned_earthnull_station_id == station_id).order_by(CleanedEarthNull.cleaned_earthnull_timestamp.desc()).first()

def get_n_latest_cleaned_earthnull_by_station(n_limits:int, station_id:str, db:Session):
    return db.query(CleanedEarthNull).filter(CleanedEarthNull.cleaned_earthnull_station_id == station_id).order_by(CleanedEarthNull.cleaned_earthnull_timestamp.desc()).limit(n_limits).all()

def get_n_latest_pm25_cleaned_earthnull_by_station(n_limits:int, station_id:str, db:Session):
    fields = ['cleaned_earthnull_station_id', 'cleaned_earthnull_pm25']
    return db.query(CleanedEarthNull).filter(CleanedEarthNull.cleaned_earthnull_station_id == station_id).order_by(CleanedEarthNull.cleaned_earthnull_timestamp.desc()).options(load_only(*fields)).limit(n_limits).all()