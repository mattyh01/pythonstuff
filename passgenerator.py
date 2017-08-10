chars = {"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-/p]["}
pass == ''
user = int(raw_input("Welcome to password generator. Pick how long you would like your password to be."))

for i in user:
    pass = random.random(chars)
    print pass
