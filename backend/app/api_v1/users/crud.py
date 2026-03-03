from sqlalchemy import select, Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import User
from .shemas import UserUpdate, UserCreate, UserUpdatePartial


async def get_users(session: AsyncSession) -> list[User]:
    stat = select(User).order_by(User.user_id)
    result: Result = await session.execute(stat)
    user = result.scalars().all()
    return list(user)


async def get_user(user_id: int, session: AsyncSession) -> User | None:
    return await session.get(User, user_id)


async def create_user(new_user: UserCreate, session: AsyncSession) -> User:
    try:
        user = User(**new_user.model_dump())
        session.add(user)
        await session.commit()
        return user
    except IntegrityError as e:
        raise Exception(f"Пользователь с emall: {new_user.email} уже существует")


async def update_user(
        user: User,
        user_update: UserUpdate | UserUpdatePartial,
        session: AsyncSession,
        partial: bool = False
) -> User:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user(user: User, session: AsyncSession) -> None:
    await session.delete(user)
    await session.commit()
