def check_inputs(user_choices):
    for i in user_choices:
        if (i != 'r') and (i != '-'):
            return False
    return True
