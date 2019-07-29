from app.models import Accounts


class TestAccounts:
    def test_should_access_accounts_return_status_200(self, client):
        response = client.get('/accounts', follow_redirects=True)

        assert 200 == response.status_code

    def test_should_access_create_return_status_200(self, client):
        response = client.get('/accounts/create', follow_redirects=True)

        assert 200 == response.status_code

    def test_should_create_return_field_required_when_not_inform_name(self, client):
        data = {
            'name': '',
            'login': 'naruto@gmail.com',
            'password': 'sasuke'
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required.' in response.data

    def test_should_create_return_field_required_when_not_inform_login(self, client):
        data = {
            'name': 'Naruto',
            'login': '',
            'password': 'sasuke'
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required.' in response.data

    def test_should_create_return_field_required_when_not_inform_password(self, client):
        data = {
            'name': 'Naruto',
            'login': 'naruto@gmail.com',
            'password': ''
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required.' in response.data

    def test_should_create_return_account_created_successfully_when_create_account(self, client):
        data = {
            'name': 'Naruto',
            'login': 'naruto@gmail.com',
            'password': 'sasuke'
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        assert b'Account created successfully.' in response.data

    def test_should_create_insert_account_in_database_when_create_account(self, client):
        data = {
            'name': 'Naruto',
            'login': 'naruto@gmail.com',
            'password': 'sasuke'
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        result = Accounts.query.count()

        assert 1 == result
