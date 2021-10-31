def filter_gmail(dictionary):
    gmail = []
    for user in dictionary:
        if "@gmail" in user["email"]:
            gmail.append(user)
    return gmail


def filter_low_password(dictionary):
    lowPass = []

    for user in dictionary:
        if len(user["password"]) < 8:
            lowPass.append(user)

    return lowPass
