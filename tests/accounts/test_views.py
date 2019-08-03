from app.models import Accounts


class TestPagination:
    def test_should_access_return_status_200(self, client):
        response = client.get('/accounts', follow_redirects=True)

        assert 200 == response.status_code


class TestCreate:
    def test_should_access_return_status_200(self, client):
        response = client.get('/accounts/create', follow_redirects=True)

        assert 200 == response.status_code

    def test_should_return_field_required_when_not_inform_name(self, client):
        data = {
            'name': '',
            'login': 'naruto@gmail.com',
            'password': 'sasuke'
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required.' in response.data

    def test_should_return_field_required_when_not_inform_login(self, client):
        data = {
            'name': 'Naruto',
            'login': '',
            'password': 'sasuke'
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required.' in response.data

    def test_should_return_field_required_when_not_inform_password(self, client):
        data = {
            'name': 'Naruto',
            'login': 'naruto@gmail.com',
            'password': ''
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required.' in response.data

    def test_should_return_account_created_successfully_when_create_account(self, client):
        data = {
            'name': 'Naruto',
            'login': 'naruto@gmail.com',
            'password': 'sasuke'
        }

        response = client.post('/accounts/create',
                               data=data,
                               follow_redirects=True)

        assert b'Account created successfully.' in response.data

    def test_should_insert_account_in_database_when_create_account(self, client):
        data = {
            'name': 'Naruto',
            'login': 'naruto@gmail.com',
            'password': 'sasuke'
        }

        client.post('/accounts/create',
                    data=data,
                    follow_redirects=True)

        result = Accounts.query.count()

        assert 1 == result


class TestUpdate:
    def test_should_access_return_status_200_when_account_exists(self, client, db):
        account = Accounts(name='microsoft',
                           login='naruto@email.com',
                           password='test123')

        db.session.add(account)

        db.session.commit()

        response = client.post('/accounts/1', follow_redirects=True)

        assert 200 == response.status_code

    def test_should_access_return_status_404_when_account_not_exists(self, client):
        response = client.post('/accounts/1', follow_redirects=True)

        assert 404 == response.status_code

    def test_should_update_account_update_name(self, client, db):
        account = Accounts(name='microsoft',
                           login='naruto@email.com',
                           password='test123')

        db.session.add(account)

        db.session.commit()

        data = {
            'name': 'test',
            'login': 'test',
            'password': 'test'
        }

        client.post('/accounts/1', data=data, follow_redirects=True)

        account = Accounts.query.first()

        assert 'test' == account.name

    def test_should_update_account_update_login(self, client, db):
        account = Accounts(name='microsoft',
                           login='naruto@email.com',
                           password='test123')

        db.session.add(account)

        db.session.commit()

        data = {
            'name': 'test',
            'login': 'test',
            'password': 'test'
        }

        client.post('/accounts/1', data=data, follow_redirects=True)

        account = Accounts.query.first()

        assert 'test' == account.login

    def test_should_update_account_update_password(self, client, db):
        account = Accounts(name='microsoft',
                           login='naruto@email.com',
                           password='test123')

        db.session.add(account)

        db.session.commit()

        data = {
            'name': 'test',
            'login': 'test',
            'password': 'test'
        }

        client.post('/accounts/1', data=data, follow_redirects=True)

        account = Accounts.query.first()

        assert 'test' == account.password

    def test_should_return_account_updated_successfuly_when_update(self, client, db):
        account = Accounts(name='microsoft',
                           login='naruto@email.com',
                           password='test123')

        db.session.add(account)

        db.session.commit()

        data = {
            'name': 'test',
            'login': 'test',
            'password': 'test'
        }

        response = client.post('/accounts/1', data=data, follow_redirects=True)

        assert b'Account updated successfully.' in response.data
