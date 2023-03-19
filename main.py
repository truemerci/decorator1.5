authorized = {}


def decorator(func):
    def inner():
        login = input("Enter login: ")
        password = input("Enter password: ")
        if login in authorized and authorized[login] == password:
            return func()
        else:
            print("No such user exists")
    return inner


@decorator
def greetings():
    print("Authorization successful")


greetings()
