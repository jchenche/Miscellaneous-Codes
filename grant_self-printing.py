#!/usr/bin/env python3

file_name = input("File to be granted the ability to self-print: ")
with open(file_name, "r") as input_file:
    data = input_file.read()
with open(file_name, "a") as output_file:
    if data[-1] != '\n':
        output_file.write("\n")
        data += "\n"

    data_list = list(data)
    for i in range(len(data_list)):
        if data_list[i] == '\n':
            data_list[i] = '\\n'
        if data_list[i] == '\\':
            data_list[i] = '\\\\'
        if data_list[i] == '\'':
            data_list[i] = '\\\''
        if data_list[i] == '{':
            data_list[i] = '{{'
        if data_list[i] == '}':
            data_list[i] = '}}'
    data = ""
    for x in data_list:
        data += x

    escape_curly = "{0}"
    output_file.write('''s = r\'\'\'print('{0}s = r\\'\\'\\'{1}\\'\\'\\'\\n{1}'.format(s))\'\'\'\n'''.format(data, escape_curly))
    output_file.write('''print('{0}s = r\\'\\'\\'{1}\\'\\'\\'\\n{1}'.format(s))'''.format(data, escape_curly))