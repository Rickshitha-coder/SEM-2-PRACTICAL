string=input()
string_l=list(string)
rev_string=string_l[::-1]
if rev_string==string_l:
    print("Palindrome")
else:
    print("Not Plaindrome")
