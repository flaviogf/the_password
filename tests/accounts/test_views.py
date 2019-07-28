class TestAccounts:
    def test_should_access_accounts_return_status_200(self, client):
        response = client.get('/accounts', follow_redirects=True)

        assert 200 == response.status_code
