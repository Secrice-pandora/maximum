def is_palindrome(string):
    return string == string[::-1]
input_string = 'noon'
print(is_palindrome(input_string))