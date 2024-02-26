from datetime import date
from typing import List
import traceback

from sqlalchemy.exc import TimeoutError, StatementError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, func, text

from schemas.events import Events
from utils.project_logger import logger as log


async def select_report_data(star_date: date, end_date: date, session: AsyncSession) -> List[dict]:
    result_set = None
    query = select(
        Events.events_date, func.count(Events.events_date).label('qty')
    ).group_by(
        Events.events_date
    ).where(and_(
        Events.events_date > star_date,
        Events.events_date <= end_date
    ))
    try:
        result_set = await session.execute(query)
    except (TimeoutError, StatementError, Exception) as ex:
        log.error(traceback.format_exc(chain=False))
    return [{**row._mapping} for row in result_set.fetchall()] if result_set else []


async def select_report_data_group_by_hours(star_date: date, end_date: date, session: AsyncSession) -> List[dict]:
    result_set = None
    query = """select count(1) as qty, toStartOfInterval(event_ts, INTERVAL 12 HOUR) as events_timestamp
             from default.events 
             where events_date >= '{star_date}' and events_date < '{end_date}'
             group by events_timestamp
             order by events_timestamp"""
    try:
        result_set = await session.execute(
            text(query.format(star_date=star_date, end_date=end_date)))
    except (TimeoutError, StatementError, Exception) as ex:
        log.error(traceback.format_exc(chain=False))
    return [{**row._mapping} for row in result_set.fetchall()] if result_set else []
