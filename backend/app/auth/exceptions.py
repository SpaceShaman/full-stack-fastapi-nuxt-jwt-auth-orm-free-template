class IncorrectUsernameOrPassword(Exception):
    pass


class UserAlreadyExists(Exception):
    pass


class UserNotFound(Exception):
    pass


class UserIsNotActive(Exception):
    pass


class PasswordIsTooWeak(Exception):
    pass


class ActivationCodeNotFound(Exception):
    pass
