from app.models import User


class TestUser:
    def test_should_authenticate_return_true_when_authenticate(self, bcrypt):
        password_hash = bcrypt.generate_password_hash('sasuke')

        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password=password_hash)

        assert naruto.authenticate('sasuke')

    def test_should_authenticate_return_false_when_not_authenticate(self, bcrypt):
        password_hash = bcrypt.generate_password_hash('sasuke')

        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password=password_hash)

        assert not naruto.authenticate('wrong')
