# 1)Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

# def delete_words(file_name):
#     """It takes an argument - the name of the file.
# Reads the file and writes the matching words to a new list, then overwrites from this list to the file.
# I haven't figured out how to remove an even number, but maybe I can't think of it = ("""
#     count_delete = 0
#     new_lis_word = []
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             words = line.split()
#             # print(words)
#             for word in words:
#                 word_without_punc = delete_punc(word)
#                 if len(word_without_punc) < 3 or len(word_without_punc) > 5:
#                     new_lis_word.append(word_without_punc)
#                     count_delete += 1
#                 # print(new_lis_word, 'new')
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for word in new_lis_word:
#             file.write(word + ' ' + '\n')
#
# def delete_punc(word):
#     """Removes punctuation."""
#     from string import punctuation
#     for punc in punctuation:
#         if punc in word:
#             word = word.replace(punc, '')
#     return word
#
# delete_words('hw_file_1.txt')

# 2)Текстовый файл содержит записи о телефонах и их владельцах.
#     Переписать в другой файл телефоны тех владельцев, фамилии которых
# начинаются с букв К и С.

# def phone_number_selection(original_file, selected_file):
#     """The function takes two arguments. 1 - original file;
#     2 - the file into which we will write the selected data."""
#     with open(original_file, 'r', encoding='utf-8') as file:
#         for elem in file:
#             phone_lis = elem.split()
#             print(phone_lis)
#             for last_name in phone_lis:
#                 print(last_name)
#                 if last_name[0] == 'К' or last_name[0] == 'С':
#                     with open(selected_file, 'a', encoding='utf-8') as file_1:
#                         for elem in phone_lis:
#                             file_1.write(elem + ' ')
#                         file_1.write('\n')
#
#
# phone_number_selection('hw_file_2.txt', 'hw_file_2.2.txt')

# 3)Получить файл, в котором текст выровнен по правому
# краю путем равномерного добавления пробелов.

# def far_right_text(original_file, modified_file, len_line):
#         """Accepts two files and int value (how long the line should be).
#         With the help of rjust it is right-aligned."""
#     with open(original_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             # print(len(line))
#             modified_line = line.rjust(len_line)
#             with open(modified_file, 'a', encoding='utf-8') as mod_file:
#                 mod_file.write(modified_line)
#
# far_right_text('hw_file_3.txt', 'hw_file_3.2.txt', 60)

# 4)Дан текстовый файл со статистикой посещения сайта за неделю.
#     Каждая строка содержит ip адрес, время и название дня недели
# (например, 139.18.150.126 23:12:44 sunday). Создайте новый
# текстовый файл, который бы содержал список ip без повторений
# из первого файла. Для каждого ip укажите количество посещений,
#                                                     наиболее
# популярный день недели. Последней строкой в файле добавьте наиболее
# популярный отрезок времени в сутках длиной один час в целом для сайта.

# def data_ip(original_file, sorted_file):
#     """The function takes two files. Tricky with lists.
#     I could not fully implement this task at the time of completing my homework."""
#     ip_lis = []
#     ip_inner_lis = []
#     ip_count_dic = {}
#     day_dic = {}
#     day_count_lis = []
#     with open(original_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             ip_lis.append(line)
#         for elem in ip_lis:
#             # print(elem)
#             elem_lis = elem.split()
#             ip_inner_lis.append(elem_lis)
#
#         for elem_ip in ip_inner_lis:
#             # print(elem_lis[2])
#             ip_count_dic[elem_ip[0]] = ip_count_dic.get(elem_ip[0], 0) + 1
#
#         for elem_day in ip_inner_lis:
#             day_count_lis = elem_day[2]
#             day_dic[elem_day[0]] = day_dic.get(elem_day[0], elem_day[2])
#
#         for elem_res in ip_count_dic:
#             res_line = f'{elem_res} - {ip_count_dic[elem_res]}'
#             # print(elem_res, ip_count_dic[elem_res])
#             with open(sorted_file, 'a', encoding='utf-8') as file:
#                 file.write(res_line)
#                 file.write('\n')

    # print(ip_lis)
    # print(ip_inner_lis)
    # print(ip_count_dic)
    # print(day_dic)

# data_ip('hw_file_4.txt', 'hw_file_4.2.txt')