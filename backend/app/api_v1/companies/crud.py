from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from backend.app.core.auth_utils import hash_password
from backend.app.database.models import Company
from .shemas import CompanyCreate


async def get_companies(session: AsyncSession) -> list[Company]:
    stmt = select(Company).order_by(Company.rating.desc())
    result: Result = await session.execute(stmt)
    company = result.scalars().all()
    return list(company)


async def get_companies_email(email: str,session: AsyncSession) -> Company:
    stmt = select(Company).where(Company.email == email)
    result: Result = await session.execute(stmt)
    company = result.scalars().first()
    return company


async def create_company(new_company : CompanyCreate, session: AsyncSession) -> Company:
    company_data = new_company.model_dump()
    company_data["password"] = hash_password(new_company.password)
    company = Company(**company_data)
    session.add(company)
    await session.commit()
    return company

async def get_company_id(company_id: int, session: AsyncSession) -> Company | None:
    stmt = select(Company).where(Company.id == company_id)
    result = await session.execute(stmt)
    company = result.scalar_one_or_none()
    return company


