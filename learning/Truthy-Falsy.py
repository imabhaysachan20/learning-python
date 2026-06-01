def can_access(user, password_input):
    # user is a dict coming from DB or None

    if not user:
        return "No user found"

    stored_password = user.get("password")
    role = user.get("role")
    is_active = user.get("is_active")

    # tricky logic starts
    if (is_active and stored_password and password_input and stored_password == password_input) \
        or (role == "admin" and is_active):

        access_level = (
            role == "admin" and "full_access" or
            role == "editor" and "edit_access" or
            "read_only"
        )

    elif is_active == False and (stored_password == "" or stored_password is None):
        return "Inactive account with no password set"

    elif not (stored_password or password_input):
        return "Both passwords missing (edge case)"

    else:
        return "Access denied"

    # second layer of tricky checks
    if access_level and access_level != True:
        if access_level == "":
            return "Empty access bug"
        return f"Granted: {access_level}"

    return "Unexpected state"


# test data (realistic messy DB cases)
users = [
    None,
    {"password": "1234", "role": "admin", "is_active": True},
    {"password": "", "role": "editor", "is_active": True},
    {"password": None, "role": "viewer", "is_active": False},
    {"password": "pass", "role": "editor", "is_active": True},
    {"password": "0", "role": "viewer", "is_active": True},
]

inputs = ["1234", "", None, "wrong"]

for u in users:
    for inp in inputs:
        print(u, "|", inp, "=>", can_access(u, inp))