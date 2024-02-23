from datetime import date, timedelta

from fastapi import APIRouter, Depends, Response, Query
from fastapi.responses import HTMLResponse

from sqlalchemy.ext.asyncio import AsyncSession

from db.crud.reports import select_report_data
from db.database import get_cursor
from utils.visualizer import visualise

reports_routers = APIRouter(prefix="/v1/reports")


class QueryParams:
    def __init__(self,
                 report_date: date = Query(example='2023-02-01'),
                 days_qty: int = Query(example='95', ge=90, le=365, description='quantity of day from star_date')
                 ) -> None:
        self.report_date = report_date
        self.days_qty = days_qty


@reports_routers.get('/get_report_by_date', response_class=HTMLResponse,
                     description="endpoint return data for period of 3 to 36 month")
async def get_report(qp: QueryParams = Depends(), ch_session: AsyncSession = Depends(get_cursor)):

    start_date = qp.report_date - timedelta(days=qp.days_qty)
    end_date = qp.report_date
    data = await select_report_data(start_date, end_date, session=ch_session)

    if data:
        response = visualise(data=data)
        headers = {'Content-Disposition': 'inline; filename="out.png"'}
        media_type = 'image/png'
        code = 200
    else:
        response = f"<html>No data found for period: {qp.report_date} - {qp.end_date}</html>"
        headers = None
        media_type = 'text/html'
        code = 404
    return Response(response, headers=headers, media_type=media_type, status_code=code)
