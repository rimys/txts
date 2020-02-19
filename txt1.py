''' считывание файла as is'''
filename = 'learning_python.txt'
with open(filename) as sample_text:
    text1 = sample_text.read()
print(text1)
print()

''' считывание файла построчно в список'''
with open(filename) as sample_text:
    lines = sample_text.readlines()
for line in lines:
    print(line.rstrip())
print()

'''складывание в одну строку'''
txt_string = ''
for line in lines:
    txt_string += line.rstrip() + ' '


print(txt_string)
print()
for line in lines:

    print(line.replace('Python', 'Ruby').rstrip())