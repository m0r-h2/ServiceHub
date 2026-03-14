from fastapi import Depends, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .shemas import CompanyResponse, CompanyCreate
from backend.app.database.models import db_helper

router = APIRouter(
    tags=["Company"]
)



@router.get("/", response_model=list[CompanyResponse], status_code=status.HTTP_200_OK)
async def get_companies(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_companies(session=session)



@router.post("/", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
async def create_company(
        new_company: CompanyCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_company(
        new_company=new_company,
        session=session
    )