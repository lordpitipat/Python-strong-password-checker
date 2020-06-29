def strong_password(p_str: str) -> bool:
    length = 6 <= len(p_str) <= 12
    
    # searching for digits
    digit = any(c.isdigit() for c in p_str)

    # searching for uppercase
    uppercase = any(c.isupper() for c in p_str)

    # # searching for lowercase
    lowercase = any(c.islower() for c in p_str)

    # # searching for symbols
    symbol = False
    for sym in ['$','#','@']:
        if sym in p_str:
            symbol = True
    
    consecutive = False   
    for i in range(len(p_str)):
        if p_str[i] != p_str[-1]:
            if p_str[i] == p_str[i+1]:
                consecutive = True
    
    strong = length and digit and uppercase and lowercase and symbol and not(consecutive)   
    return strong   
