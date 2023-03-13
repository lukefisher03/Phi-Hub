import bcrypt

def validate_username(username:str, csv_reader:str) -> list:
    '''
    Verify a given username. 

    Rules: 
        - Longer than 8 characters
        - No special characters
        - Not already taken
    
    Params: 
        - Username as a string
        - file object, optional. Defaults to None

    Returns: 
        String describing why it didn't pass the tests. 
        If it did pass then it returns an empty string.
    '''
    
    errors = list()

    for row in csv_reader:
        if list(row)[0] == username:
            errors.append("Username has already been taken")
            break

    if len(username) < 8:
        errors.append("The username must be longer than 8 characters")
    if any(not username.isalnum() for _ in username):
        errors.append("Special characters and whitespace are not allowed in usernames")
    if username[0].isnumeric():
        errors.append("Usernames cannot start with numbers")
    
    return errors

def validate_password(password:str) -> list:
    errors = list()

    if len(password) < 8:
        errors.append("The password must be longer than 8 characters")
    if " " in password:
        errors.append("You cannot have whitespace in your password")

    if not errors:
        bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        return [errors, hash]
    return [errors, None]