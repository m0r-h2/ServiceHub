from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.models import db_helper
from . import crud

from .dependencies import get_user_id
from .shemas import UserCreate, UserUpdate, UserUpdatePartial, User, UserBase

router = APIRouter(
    tags=["Users👤"]
)


@router.get("/", response_model=list[User], status_code=status.HTTP_200_OK)
async def get_users(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_users(session=session)


@router.get("/{user_id}/", response_model=User, status_code=status.HTTP_200_OK)
async def get_user(
        user: User = Depends(get_user_id),
):
    return user


@router.post("/", response_model=UserBase)
async def create_user(
        new_user: UserCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_user(
        new_user=new_user,
        session=session,
    )


@router.put("/{user_id}", response_model=User)
async def update_user(
        user_update: UserUpdate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        user: User = Depends(get_user_id),
):
    return await crud.update_user(
        user_update=user_update,
        user=user,
        session=session
    )


@router.patch("/{user_id}", response_model=User)
async def update_user_partial(
        user_update: UserUpdatePartial,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        user: User = Depends(get_user_id),
):
    return await crud.update_user(
        user_update=user_update,
        user=user,
        session=session,
        partial=True
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        user: User = Depends(get_user_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await crud.delete_user(
        user=user,
        session=session
    )
