from fastapi import status, Path, HTTPException
from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.models import db_helper, Task
from . import crud

async def get_task_id(
        task_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Task:
    task = await crud.get_task(
        task_id=task_id,
        session=session
    )
    if Task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Заявка не найдена"
        )

    return task



