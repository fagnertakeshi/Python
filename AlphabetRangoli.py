    
#Let's break down the code print((s+s[::-1][1:]).center(n*4-3, '-')):

#(s+s[::-1][1:]): This concatenates the string s with a reversed version of s, excluding the first character. The [::-1] syntax creates a reversed copy of s, and [1:] slices this reversed copy to exclude the first character. So, if s is "abc", (s+s[::-1][1:]) would evaluate to "abccba".

#.center(n*4-3, '-'): This centers the resulting string from step 1 within a field of width n*4-3, with '-' characters as the padding. The n*4-3 expression calculates the desired width of the centered string, and the '-' character specifies the padding character.

#So, overall, the code is concatenating the input string s with a reversed version of itself (excluding the first character), and then centering the resulting string within a field of width n*4-3, with '-' characters as padding.


def print_rangoli(size):
    for i in range(size):
        s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(n*4-3, '-'))

    for i in range(size-1):
        s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
        print((s+s[::-1][1:]).center(n*4-3, '-'))
