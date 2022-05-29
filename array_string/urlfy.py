"""
Write a method replace all spaces in a string with %20. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given
the true length of the string.
example:
input: "Mr. Jhon Smith    ", 13
output: "Mr.%20Jhon%20Smath"
"""
string = "Mr Jhon Smith  "
string = list(string.strip())
for i in range(len(string)):
    if string[i] == " ":
        string[i] = "%20"
print("".join(string))
