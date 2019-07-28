import json


from app.models import User


class TestLogin:
    def test_should_access_login_return_status_200(self, client):
        response = client.get('/login', follow_redirects=True)

        assert 200 == response.status_code

    def test_should_redirect_to_accounts_when_login(self, client, db):
        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password='sasuke')

        db.session.add(naruto)

        db.session.commit()

        data = {
            'email': naruto.email,
            'password': naruto.password
        }

        response = client.post('/login',
                               data=json.dumps(data),
                               follow_redirects=True)

        assert b'The Password - Accounts' in response.data

    def test_should_return_email_or_password_incorrect_when_not_login(self, client, db):
        pass

    def test_should_return_field_required_when_not_inform_email(self, client):
        pass

    def test_should_return_field_required_when_not_inform_password(self, client):
        pass
