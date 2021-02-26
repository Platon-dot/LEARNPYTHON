with open('text.txt', 'r', encoding='utf-8') as my_file: 
# my_file.write('\tНа этом все!')  # открываем, создаем и записываем инфу
#    content = my_file.read()
#    print(content)
    for ln in my_file:
        ln = ln.upper()
        ln = ln.replace('\n', '')
        print(ln)