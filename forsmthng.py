
# def sum_array(lst):
#     slag = lst.pop()
#     if len(lst) == 0:
#         return slag
#     return slag + sum_array(lst)
#
# print(sum_array([1, 2, 3, 4])


# def sort_array(lst):
#     lst_left = []
#     lst_right = []
#     if len(lst) < 2:
#         return lst
#     yak = lst[0]
#     for i in lst[1:]:
#         if yak > i:
#             lst_left.append(i)
#         else:
#             lst_right.append(i)
#     return sort_array(lst_left) + [yak] + sort_array(lst_right)
#
#
# def array_search(lst, item):
#     if len(lst) > 1:
#         if lst[len(lst)//2] > item:
#             new_lst = lst[:len(lst)//2]
#             return array_search(new_lst, item)
#         elif lst[len(lst)//2] < item:
#             new_lst = lst[len(lst) // 2:]
#             return array_search(new_lst, item)
#         else:
#             return True
#     else:
#         return True if lst[0] == item else False
#
# print(array_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))

# graph = {}
# graph['you'] = ['alice', 'bob', 'claire']
# graph['bob'] = ['anuj', 'peggy']
# graph['alice'] = ['peggy']
# graph['claire'] = ['thom', 'johnny']
# graph['anuj'] = []
# graph['peggy'] = []
# graph['thom'] = []
# graph['johnny'] = []
#
# def search_deep(name):
#     name_lst = graph[name]
#     while True:
#         try:
#             if name_lst[0].endswith('p'):
#                 return name_lst[0]
#             else:
#                 name_lst.extend(graph[name_lst[0]])
#                 del name_lst[0]
#         except IndexError:
#             print('There is no such word')
#             break
#         except KeyError:
#             print('There is no such word')
#             break
# print(search_deep('you'))

# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def array_search(lst, item):
#     first_index = 0
#     last_index = len(lst) - 1
#     while first_index != last_index:
#         if item == lst[(last_index + first_index) // 2]:
#             return (last_index + first_index) // 2
#         elif item < lst[(last_index + first_index) // 2]:
#             last_index = (last_index + first_index) // 2 - 1
#         else:
#             first_index = (last_index + first_index) // 2 + 1
#
#
# print(array_search(lst, 1))

# def factorial(k):
#     try:
#         assert k >= 0
#         if k <= 1:
#             return 1
#         else:
#             return factorial(k-1)*k
#     except AssertionError:
#         return 'Введите положительное число'
#
# print(factorial(-5))

# def megommetr(k):
#     res = 0
#     while k > 1:
#         k -= 1
#         res += k
#     return res
#
# print(megommetr(4))


# infinity = float('inf')
#
# graph = {
#     'start': {
#         'a': 6,
#         'b': 2
#     },
#     'a': {
#         'end': 1
#     },
#     'b': {
#         'a': 3,
#         'end': 5
#     },
#     'end': {}
# }
#
# costs = {
#     'a': 6,
#     'b': 2,
#     'end': infinity
# }
#
# parents = {
#     'a': 'start',
#     'b': 'start',
#     'end': None
# }
# processed = []
#
#
# def search_unit(unit):
#     '''Функция ищет соседа узла с минимальной стоимостью'''
#     pass
#
#
# def update(unit):
#     '''Функция, обновляющая стоимости соседних узлов и их родителей'''
#     pass
#
# base_unit = 'start'
# k = 0
#
#
# unit = search_unit(base_unit)
# while unit is not None:
#     update(unit)
#     processed.append(unit)
#     unit = search_unit(base_unit)
# base_unit = processed[k]
# k += 1


# def hash_decorator(func):
#     dict = {}
#     def wrapper(k):
#         if k in dict:
#             return dict[k]
#         else:
#             dict[k] = func(k)
#             return func(k)
#     return wrapper
#
#
# @hash_decorator
# def quad(k):
#     return k**4


# import os.path
#
# BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TEMPLATES_DIR = os.path.join(BASE, 'templates')
#
# print(TEMPLATES_DIR)
# print(os.path.abspath(__file__))
#
# names = [('qwer', 'tyu', 'iop'), ('asd', 'fgh', 'hjk')]
#
# import operator as op
#
# print(op.itemgetter(1)(names))
#
# def itemgetterdecoratormaker(index):
#     f = op.itemgetter(index)
#     def decorator(func):
#         def wrapper(iterable):
#             if index > 0:
#                 return f(func(iterable))
#         return wrapper
#     return decorator
#
# @itemgetterdecoratormaker(-1)
# def gen(iterable):
#     return [i**2 for i in range(iterable)]
#
# print(gen(10))
#
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)
#
# DIR = Path('D:  /python')
# print(DIR)
#
# print(type(BASE_DIR))
# print(type(BASE))
#
# os.makedirs(r'E:\python\first_bot', exist_ok=True)
#
# import socket
# from select import select
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('127.0.0.1', 5000))
# server_socket.listen()
# sockets = []
#
# def accept_connection(sock):
#         client_socket, addr = sock.accept()
#         print('Пришло подключение от ', addr)
#         sockets.append(client_socket)
#
# def send_message(sock):
#     while True:
#         data = sock.recv(4096)
#         if not data:
#             break
#         else:
#             sock.send(data)
#     sock.close()
#
# def main_loop():
#     while True:
#         readable, _, _ = select(sockets, [], [])
#         for sock in readable:
#             if sock is server_socket:
#                 accept_connection(sock)
#             else:
#                 send_message(sock)
#
#
#
# if __name__ == '__main__':
#     main_loop()

def transmit_dec_to_bin(number):
    bin = ''
    if number == 0:
        bin += '0'
        return bin
    while number > 0:
        if number % 2 == 1:
            bin += '1'
            number = number // 2
        else:
            bin += '0'
            number = number // 2

    return  int(bin[::-1])

print(transmit_dec_to_bin(45846415))
















