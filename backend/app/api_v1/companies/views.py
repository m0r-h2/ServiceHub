from fastapi import Depends, status, APIRouter, Response
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .shemas import CompanyResponse, CompanyCreate
from backend.app.database.models import db_helper
from backend.app.core.auth_utils import create_access_token

router = APIRouter(
    tags=["Company"]
)



@router.get("/", response_model=list[CompanyResponse], status_code=status.HTTP_200_OK)
async def get_companies(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_companies(session=session)




@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_company(
        response: Response ,
        new_company: CompanyCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    # 1. Создаем компанию через ваш CRUD
    company = await crud.create_company(new_company=new_company, session=session)

    # 2. Генерируем JWT (в payload обычно кладем id или email)
    access_token = create_access_token(data={"sub": str(company.id)})

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True, # Защита от кражи токена через JS
        max_age=1800 # Срок жизни (например, 1 день)
    )

    # 3. Возвращаем и данные компании, и токен
    return {
        "company": company,
        "access_token": access_token,
        "token_type": "bearer"
    }