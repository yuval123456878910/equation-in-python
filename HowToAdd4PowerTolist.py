# poc is the output.
# hen is the store numbers then relis
# text is the culculator input

text = input("Input: ")

num = 0
poc = list()

hen = str()

for i in text:
    if i in "+-*/":
        poc.append(hen)
        hen = str()
        poc.append(str(i))
    else:
        hen += i
if hen != "":
    poc.append(hen)

# key part if i int text not equls to + or - or / or * its store the number in hen if its equls its relis to poc.
# if its hen stil store deta its relis to poc.

print(poc)

# print poc to see if this work.
