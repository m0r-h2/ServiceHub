from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from .shemas import User
from . import crud
from backend.app.database.models import db_helper


async def get_user_id(
        user_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> User:
    user = await crud.get_user(
        user_id=user_id,
        session=session
    )
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User id: {user_id} not found",
    )
