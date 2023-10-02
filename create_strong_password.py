def get_password_variants(password):
    pass_variants = []
    substitutions = {
        'a': ['@', '4', 'A'],
        'e': ['3', 'E'],
        'i': ['1', '!', 'I'],
        'o': ['0', 'O'],
        's': ['$', '5', 'S'],
        't': ['7', 'T'],
        'z': ['2', 'Z']
    }
    
    for i in range(len(password)):
        if password[i] in substitutions:
            for sub in substitutions[password[i]]:
                pass_variant = password[:i] + sub + password[i+1:]
                pass_variants.append(pass_variant)
    
    pass_variants.append(password + '!')
    pass_variants.append(password + '123')
    pass_variants.append(password + '@')
    pass_variants.append(password + '#')
    pass_variants.append(password + '$')
    pass_variants.append(password + '%')
    pass_variants.append(password + '&')
    pass_variants.append(password + '*')
    pass_variants.append(password + '-')
    pass_variants.append(password + '_')
    pass_variants.append(password + '=')
    pass_variants.append(password + '+')    
    return pass_variants
password = input("Input your password: ")
result_variants = get_password_variants(password)
print(result_variants)