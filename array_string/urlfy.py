# print(list("sifat nas  ".strip()))
string = "Mr Jhon Smith  "
string = list(string.strip())
for i in range(len(string)):
    if string[i] == " ":
        string[i] = "%20"
print("".join(string))
