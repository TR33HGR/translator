import unittest
from hamcrest import assert_that, is_, calling, raises

from app.models import User


class TestUserModel(unittest.TestCase):
    def test_set_password_sets_the_users_password_to_the_given_password(self):
        user = User(username='tom', email='example@email.com')
        user.set_password('some_password')
        assert_that(user.check_password('some_password'), is_(True))

    def test_set_password_overwrite_any_previously_set_passwords(self):
        user = User(username='tom', email='example@email.com')
        user.set_password('some_password')
        user.set_password('some_other_password')
        assert_that(user.check_password('some_other_password'), is_(True))

    def test_check_password_errors_if_no_password_has_been_set(self):
        user = User(username='tom', email='example@email.com')
        assert_that(calling(user.check_password).with_args(
            'some_password'), raises(AttributeError))

    def test_check_password_fails_if_given_incorrect_password(self):
        user = User(username='tom', email='example@email.com')
        user.set_password('some_password')
        assert_that(user.check_password('not_some_password'), is_(False))


if __name__ == '__main__':
    unittest.main()
