def password_check(password):
    # Input validation
    if not isinstance(password, str):
        return "Password must be a string"
    
    if password is None:
        return "Password cannot be None"
    
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character"
    
    # Check for sequential characters
    lower_password = password.lower()
    sequences = ['123', '234', '345', '456', '567', '678', '789', 'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']
    if any(seq in lower_password for seq in sequences):
        return "Password must not contain sequential characters"
    
    # Check for repeated patterns (enhanced)
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return "Password must not contain repeated characters (3 or more)"
    
    # Check for repeated segments (like Aa1!Aa1!)
    for length in range(2, len(password) // 2 + 1):
        for i in range(len(password) - length * 2 + 1):
            segment = password[i:i+length]
            if password[i+length:i+length*2] == segment:
                return "Password must not contain repeated segments"
    
    # Enhanced L33t speak normalization
    leet_map = {'0': 'o', '1': 'i', '3': 'e', '4': 'a', '5': 's', '7': 't', '@': 'a', '!': 'i'}
    normalized = lower_password
    for leet, normal in leet_map.items():
        normalized = normalized.replace(leet, normal)
    
    # Check for L33t speak patterns in original password
    leet_patterns = ['passw0rd', 'p@ssw0rd', 'p@ssword', 'adm1n', 'w3lcome', 'qu3rty']
    if any(pattern in lower_password for pattern in leet_patterns):
        return "Password must not use L33t speak substitutions"
    
    # Expanded common passwords and patterns
    common_passwords = [
        'password', 'password1', 'password2', 'password3', 'passw0rd', 'p@ssword', 'p@ssw0rd',
        '12345678', '87654321', 'qwerty', 'qwerty1', 'qwerty123', 'asdfgh', 'zxcvbn',
        'abc123', 'admin', 'admin123', 'administrator', 'letmein', 'welcome', 'welcome1',
        'monkey', 'dragon', 'master', 'shadow', 'superman', 'michael', 'football',
        'baseball', 'liverpool', 'jordan', 'harley', 'ranger', 'buster', 'hunter'
    ]
    
    # Check normalized password against common passwords
    if normalized in common_passwords:
        return "Password is too common and easily guessed"
    
    # Check for keyboard patterns
    keyboard_patterns = ['qwerty', 'asdfgh', 'zxcvbn', 'qwertyui', 'asdfghjk', 'zxcvbnm']
    if any(pattern in lower_password for pattern in keyboard_patterns):
        return "Password must not contain keyboard patterns"
    
    # Check for dictionary words (basic implementation)
    common_words = ['password', 'welcome', 'admin', 'login', 'user', 'guest', 'test', 'demo', 'sample']
    for word in common_words:
        if word in lower_password:
            return "Password must not contain common dictionary words"
    
    # Check for password variations (password + numbers)
    base_words = ['password', 'admin', 'welcome', 'qwerty']
    for word in base_words:
        if lower_password.startswith(word) and any(c.isdigit() for c in lower_password[len(word):]):
            return "Password must not be a variation of common words with numbers"
    
    return "Password is valid"

# Test the function (without exposing passwords)
test_cases = ["test1", "test2", "test3", "test4"]
for i, result in enumerate([password_check("weak"), password_check("WeakPassword"), password_check("WeakPassword1"), password_check("WeakPassword1!")]):
    print(f"Test {i+1}: {result}")