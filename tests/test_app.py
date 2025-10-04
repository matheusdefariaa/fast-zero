from http import HTTPStatus


def test_read_root_dev_retorna_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'teste',
            'email': 'email@email.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'id': 1,
        'username': 'teste',
        'email': 'email@email.com',
    }


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'teste',
                'email': 'email@email.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        'users/1',
        json={
            'username': 'teste2',
            'email': 'teste@test.com',
            'id': 1,
            'password': '123',
        },
    )

    assert response.json() == {
        'username': 'teste2',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        'users/10',
        json={
            'username': 'teste2',
            'email': 'teste@test.com',
            'id': 1,
            'password': '123',
        },
    )

    assert response.json() == {'detail': 'NOT FOUND'}


def test_delete_user(client):
    response = client.delete('users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('users/10')

    assert response.json() == {'detail': 'NOT FOUND'}
