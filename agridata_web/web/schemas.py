from pydantic import BaseModel
from typing import Any, Optional, List

class WeatherItem(BaseModel):
    stn_Code: Optional[str] = None
    stn_Name: Optional[str] = None
    date: Optional[str] = None
    temp: Optional[str] = None
    max_Temp: Optional[str] = None
    min_Temp: Optional[str] = None
    hum: Optional[str] = None
    widdir: Optional[str] = None
    wind: Optional[str] = None
    rain: Optional[str] = None
    sun_Time: Optional[str] = None
    sun_Qy: Optional[str] = None
    condens_Time: Optional[str] = None
    gr_Temp: Optional[str] = None
    soil_Temp: Optional[str] = None
    soil_Wt: Optional[str] = None

class WeatherResponse(BaseModel):
    total: int
    page: int
    size: int
    items: List[WeatherItem]
