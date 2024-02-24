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
                 # Using the 'days_qty' parameter, users can select a data range that is suitable for OLAP solutions.
                 days_qty: int = Query(ge=90, le=365, description='quantity of day before report_date')
                 ) -> None:
        self.report_date = report_date
        self.days_qty = days_qty


@reports_routers.get('/get_report_by_date', response_class=HTMLResponse,
                     description="**Events quantity per day**\n"
                                 "Report periods: 90 - 365 days.\n"
                                 "End report date = report_date parameter\n"
                                 "start report date = report_date - days_qty")
async def get_report(qp: QueryParams = Depends(), ch_session: AsyncSession = Depends(get_cursor)):
    start_date = qp.report_date - timedelta(days=qp.days_qty)
    end_date = qp.report_date
    data = await select_report_data(start_date, end_date, session=ch_session)

    if data:
        x_label = "Periods"
        y_label = "Quantity of events"
        title = "Quantity of events per days"

        response = visualise(data=data, x_label=x_label, y_label=y_label, title=title)

        headers = {'Content-Disposition': 'inline; filename="out.png"'}
        media_type = 'image/png'
        code = 200
    else:
        response = f"<html>No data found for period: {start_date} - {end_date}</html>"
        headers = None
        media_type = 'text/html'
        code = 404
    return Response(response, headers=headers, media_type=media_type, status_code=code)
