from fastapi import FastAPI, Query, HTTPException, Depends
from web.clients.agridata import RDAAgriWeatherClient
from web.schemas import WeatherResponse, WeatherItem

app = FastAPI(title="RDA AgriWeather Proxy", version="1.0.0")

async def get_client():
    client = RDAAgriWeatherClient()
    try:
        yield client
    finally:
        await client.close()

@app.get("/health")
async def health():
    return {"ok": True}

@app.get("/api/rda/weather/time", response_model=WeatherResponse)
async def weather_time(
    date: str = Query(..., description="YYYY-MM-DD"),
    spot_code: str | None = Query(None, description="관측지점코드"),
    spot_name: str | None = Query(None, description="관측지점명"),
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    client: RDAAgriWeatherClient = Depends(get_client),
):
    try:
        data = await client.get_weather_time_list(
            date_time=date, spot_code=spot_code,
            page_no=page, page_size=size, spot_name=spot_name
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {e}")

    items = [WeatherItem(**row) for row in data["items"]]
    return WeatherResponse(total=data["total"], page=data["page"], size=data["size"], items=items)

@app.get("/api/rda/weather/term-day", response_model=WeatherResponse)
async def weather_term_day(
    begin_date: str = Query(..., description="YYYY-MM-DD"),
    end_date: str = Query(..., description="YYYY-MM-DD"),
    spot_code: str = Query(..., description="관측지점코드"),
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    client: RDAAgriWeatherClient = Depends(get_client),
):
    try:
        data = await client.get_weather_term_day_list(
            begin_date=begin_date, end_date=end_date,
            spot_code=spot_code, page_no=page, page_size=size
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {e}")

    items = [WeatherItem(**row) for row in data["items"]]
    return WeatherResponse(total=data["total"], page=data["page"], size=data["size"], items=items)