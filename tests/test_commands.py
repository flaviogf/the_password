from app.commands import create_user
from app.models import User


class TestCreateUser:
    def test_should_output_return_success_message_when_create_user(self, runner):
        result = runner.invoke(create_user,
                               ['--name', 'Naruto',
                                '--email', 'naruto@email.com',
                                '--password', 'sasuke'])

        assert 'user created successfully.' in result.output

    def test_should_database_contains_a_user_when_create_a_user(self, runner):
        result = runner.invoke(create_user,
                               ['--name', 'Naruto',
                                '--email', 'naruto@email.com',
                                '--password', 'sasuke'])

        result = User.query.count()

        assert result == 1
