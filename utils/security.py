import bcrypt

def verify_username(username:str, f={}) -> list:
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
    print("username", username)
    if not username:
        errors.append("No username was given")
    if f.get(username, None):
        errors.append("This username has already been taken")
    if len(username) < 8:
        errors.append("The username must be longer than 8 characters")
    if any(not username.isalnum() for _ in username):
        errors.append("Special characters are not allowed in usernames")
    if username[0].isnumeric():
        errors.append("Usernames cannot start with numbers")
    
    return errors