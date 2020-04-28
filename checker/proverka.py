def proverka(password):
    if len(password) < 6:
        return 'Недопустимый пароль'
    elif password.isdigit() or password.lower() or password.upper():
        return 'Ненадежный пароль'
    elif password.islower() or password.isupper():
        return 'Слабый пароль'
    return 'Надёжный пароль'


print(proverka('ABCDEgggghh228'))