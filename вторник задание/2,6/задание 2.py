def main():
    import sys
    
    input_lines = sys.stdin.read().strip().split('\n')
    
    passwd_lines = []
    passwords = []
    is_passwd_section = True
    
    for line in input_lines:
        if line == "":
            is_passwd_section = False
            continue
        
        if is_passwd_section:
            passwd_lines.append(line)
        else:
            passwords = line.split(';')
            break
    
    common_passwords = set(password.strip() for password in passwords)

    results = []
    
    for line in passwd_lines:
        fields = line.split(':')
        if len(fields) < 7:
            continue
        
        username = fields[0]
        password = fields[1]
        user_info = fields[4].split(',')[0].strip()
        if password in common_passwords:
            results.append(f"To: {username}")
            results.append(f"{user_info}, ваш пароль слишком простой, смените его.")
    
    
    if results:
        print('\n'.join(results))

if __name__ == "__main__":
    main()
