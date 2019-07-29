from app.models import User


class TestLogin:
    def test_should_access_return_status_200(self, client):
        response = client.get('/login', follow_redirects=True)

        assert 200 == response.status_code

    def test_should_redirect_to_accounts_when_login(self, client, db, bcrypt):
        password = bcrypt.generate_password_hash('sasuke')

        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password=password)

        db.session.add(naruto)

        db.session.commit()

        data = {
            'email': naruto.email,
            'password': 'sasuke'
        }

        response = client.post('/login',
                               data=data,
                               follow_redirects=True)

        assert b'The Password - Search Accounts' in response.data

    def test_should_return_email_or_password_incorrect_when_not_login(self, client, db, bcrypt):
        password = bcrypt.generate_password_hash('sasuke')

        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password=password)

        db.session.add(naruto)

        db.session.commit()

        data = {
            'email': naruto.email,
            'password': 'wrong'
        }

        response = client.post('/login',
                               data=data,
                               follow_redirects=True)

        assert b'Email or password incorrect.' in response.data

    def test_should_return_field_required_when_not_inform_email(self, client):
        data = {
            'email': '',
            'password': 'test123'
        }

        response = client.post('/login',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required.' in response.data

    def test_should_return_field_required_when_not_inform_password(self, client):
        data = {
            'email': 'naruto@gmail.com',
            'password': ''
        }

        response = client.post('/login',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required.' in response.data


class TestLogout:
    def test_should_redirect_to_login_when_logout(self, client):
        response = client.get('/logout', follow_redirects=True)

        assert b'The Password - Login' in response.data
