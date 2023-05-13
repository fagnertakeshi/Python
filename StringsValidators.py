if __name__ == '__main__':
    s = input()
    hasNumber= any(char.isdigit() for char in s)
    hasAlphaNumeric=any(char.isalnum() for char in s)
    hasAnyAlpha=any(char.isalpha() for char in s)
    haslowerCase=any(char.islower() for char in s)
    hasUpperCase=any(char.isupper() for char in s)
    if hasAlphaNumeric:
        print ("True")
    else:
        print("False")
    if hasAnyAlpha:
        print ("True")
    else:
        print("False")
    if hasNumber:
        print("True")
    else:
        print("False")
    if haslowerCase:
        print("True")
    else:
        print("False")
    if hasUpperCase:
        print("True")
    else:
        print("False")
