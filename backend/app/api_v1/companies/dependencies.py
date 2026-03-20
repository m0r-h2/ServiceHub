from fastapi import Cookie, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import jwt

from backend.app.database.models import Company, db_helper
from backend.app.core.config import settings
from backend.app.api_v1.companies import crud


async def get_current_company(
    access_token: str | None = Cookie(None),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Company | None:

    if not access_token:
        return None

    try:
        payload = jwt.decode(access_token, settings.auth.secret_key, algorithms=[settings.auth.algorithm])
        company_id: str = payload.get("sub")

        company = await crud.get_company_id(company_id=int(company_id), session=session)
        return company
    except Exception as e:
        print(f"DEBUG: Ошибка декодирования: {e}")
        return None