from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from backend.app.database.models import Company
from .shemas import CompanyCreate

async def get_companies(session: AsyncSession) -> list[Company]:
    stmt = select(Company).order_by(Company.id)
    result: Result = await session.execute(stmt)
    company = result.scalars().all()
    return list(company)


async def create_company(new_company : CompanyCreate, session: AsyncSession) -> Company:
    company = Company(**new_company.model_dump())
    session.add(company)
    await session.commit()
    return company


