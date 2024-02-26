from datetime import date, timedelta

from fastapi import APIRouter, Depends, Response, Query
from fastapi.responses import HTMLResponse

from sqlalchemy.ext.asyncio import AsyncSession

from db.crud.reports import select_report_data, select_report_data_group_by_hours
from db.database import get_cursor
from utils.responce_manager import create_response
from utils.reports_parts import daily_events_report, daily_events_report_12_hour_groups

reports_routers = APIRouter(prefix="/v1/reports")


class QueryParams:
    def __init__(self,
                 report_date: date = Query(example='2023-02-01'),
                 # users have to select a data range that is suitable for OLAP solutions.
                 days_qty: int = Query(ge=90, le=365, description='quantity of day before report_date')
                 ) -> None:
        self.report_date = report_date
        self.days_qty = days_qty


@reports_routers.get('/get_daily_events_report', response_class=HTMLResponse,
                     description="**Events quantity per day**.<br>"
                                 "Report periods: 90 - 365 days.<br>"
                                 "End report date = report_date parameter.<br>"
                                 "start report date = report_date - days_qty")
async def get_report(qp: QueryParams = Depends(), ch_session: AsyncSession = Depends(get_cursor)):
    start_date = qp.report_date - timedelta(days=qp.days_qty)
    end_date = qp.report_date
    data = await select_report_data(start_date, end_date, session=ch_session)

    response, headers, media_type, code = create_response(data, start_date, end_date, **daily_events_report)
    return Response(response, headers=headers, media_type=media_type, status_code=code)


@reports_routers.get('/get_daily_events_report_12_hour_groups', response_class=HTMLResponse,
                     description="**Events quantity per day, grouped by every 12 hours**.<br>"
                                 "Report periods: 90 - 365 days.<br>"
                                 "End report date = report_date parameter.<br>"
                                 "start report date = report_date - days_qty")
async def get_report(qp: QueryParams = Depends(), ch_session: AsyncSession = Depends(get_cursor)):
    start_date = qp.report_date - timedelta(days=qp.days_qty)
    end_date = qp.report_date
    data = await select_report_data_group_by_hours(start_date, end_date, session=ch_session)

    response, headers, media_type, code = create_response(data, start_date, end_date,
                                                          **daily_events_report_12_hour_groups)
    return Response(response, headers=headers, media_type=media_type, status_code=code)
