def count_substring(string, sub_string):
    contador= len([i for i in range(len(string)) if string[i:i+len(sub_string)] == sub_string])
    return  contador