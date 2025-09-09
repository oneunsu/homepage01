import httpx, xmltodict
from typing import Any, Dict, Tuple
from web.config import settings

DEFAULT_TIMEOUT = httpx.Timeout(15.0, connect=5.0)

class RDAAgriWeatherClient:
    def __init__(self, client: httpx.AsyncClient | None = None):
        if client is None:
            self._client = httpx.AsyncClient(
                timeout=DEFAULT_TIMEOUT,
                http2=False,
                headers={
                    "User-Agent": "agridata-proxy/1.0 (+https://localhost)"
                },
            )
        else:
            self._client = client
    async def close(self):
        await self._client.aclose()

    async def close(self):
        await self._client.aclose()

    def _endpoint(self, op: str) -> str:
        return (
            f"{settings.BASE_PUBLIC_DATA_URL}/1390802/AgriWeather/WeatherObsrInfo/"
            f"{settings.AGRI_WEATHER_VERSION}/GnrlWeather/{op}"
        )

    def _parse_xml(self, xml_text: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        data = xmltodict.parse(xml_text)
        resp = data.get("response", {})
        header = resp.get("header", {}) or {}
        body = resp.get("body", {}) or {}
        return header, body

    def _extract_list(self, body: Dict[str, Any]) -> Tuple[int, int, int, list[dict]]:
        rcdcnt = int(body.get("rcdcnt", 0) or 0)
        page_no = int(body.get("page_No", 1) or 1)
        total = int(body.get("total_Count", 0) or 0)

        items = body.get("items", {})
        item = items.get("item") if isinstance(items, dict) else []
        if isinstance(item, dict):
            rows = [item]
        elif isinstance(item, list):
            rows = item
        else:
            rows = []
        return total, page_no, rcdcnt, rows

    async def get_weather_time_list(
        self, *, date_time: str, spot_code: str | None,
        page_no: int = 1, page_size: int = 20, spot_name: str | None = None
    ) -> Dict[str, Any]:

        url = self._endpoint("getWeatherTimeList")
        params = {
            "serviceKey": settings.PUBLIC_DATA_API_KEY,
            "Page_No": page_no,
            "Page_Size": page_size,
            "data_Time": date_time,
        }
        if spot_code:
            params["obsr_Spot_Code"] = spot_code
        if spot_name:
            params["obsr_Spot_Nm"] = spot_name

        r = await self._client.get(url, params=params)
        r.raise_for_status()

        header, body = self._parse_xml(r.text)
        result_code = str(header.get("result_Code", ""))
        result_msg = header.get("result_Msg", "")
        if result_code != "200":
            raise httpx.HTTPStatusError(f"{result_code} {result_msg}", request=r.request, response=r)

        total, page_no, rcdcnt, rows = self._extract_list(body)
        return {
            "total": total,
            "page": page_no,
            "size": rcdcnt,
            "items": rows,
        }

    async def get_weather_term_day_list(
        self, *, begin_date: str, end_date: str, spot_code: str,
        page_no: int = 1, page_size: int = 20
    ) -> Dict[str, Any]:
        url = self._endpoint("getWeatherTermDayList")
        params = {
            "serviceKey": settings.PUBLIC_DATA_API_KEY,
            "Page_No": page_no,
            "Page_Size": page_size,
            "begin_Date": begin_date,
            "end_Date": end_date,
            "obsr_Spot_Code": spot_code,
        }
        r = await self._client.get(url, params=params)
        r.raise_for_status()

        header, body = self._parse_xml(r.text)
        result_code = str(header.get("result_Code", ""))
        result_msg = header.get("result_Msg", "")
        if result_code != "200":
            raise httpx.HTTPStatusError(f"{result_code} {result_msg}", request=r.request, response=r)

        total, page_no, rcdcnt, rows = self._extract_list(body)
        return {
            "total": total,
            "page": page_no,
            "size": rcdcnt,
            "items": rows,
        }