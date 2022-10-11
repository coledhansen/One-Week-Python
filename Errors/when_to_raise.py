def get_user_name():
    inp = input('please enter your name:\n> ')
    if not inp.isalpha():
        raise ValueError('alpha characters only')
    return inp

def register_user():
    user = get_user_name()
    # Database.save(user)