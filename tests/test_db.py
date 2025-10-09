from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='matheus', email='matheus@email.com', password='1234')

    session.add(user)
    session.commit()
    # session.refresh(user)
    result = session.scalar(
        select(User).where(User.email == 'matheus@email.com')
    )

    assert result.username == 'matheus'
