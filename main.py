import string
import socket
import threading

key_word = input('Key word: ')
words_lst = []
domain_zone = ['com', 'ru', 'net', 'org', 'info', 'cn', 'es', 'top', 'au', 'pl',
               'it', 'uk', 'tk', 'ml', 'ga', 'cf', 'us', 'xyz', 'top', 'site', 'win', 'bid']


def strategy_1(word):
    '''добавление символа в конце строки'''
    abc = string.ascii_letters
    for syb in abc:
        words_lst.append(word+syb)


def strategy_2(word):
    '''поиск homoglyph'''
    homoglyph_dict = {'o': ['0'], '0': ['o'], '1': [
        'i', 'l'], 'i': ['1', 'l'], 'l': ['1', 'i']}
    for ind, syb in enumerate(word):
        for i_homo in homoglyph_dict:
            if i_homo == syb:
                words_lst.append(
                    word[:ind]+homoglyph_dict[i_homo][0]+word[ind+1:])
                try:
                    words_lst.append(
                        word[:ind]+homoglyph_dict[i_homo][1]+word[ind+1:])
                except:
                    pass


def strategy_3(word):
    '''добавление точки'''
    abc = string.ascii_letters
    for ind, syb in enumerate(word):
        if ind != len(word)-1:
            if syb in abc and word[ind+1] in abc:
                words_lst.append(word[:ind+1]+'.'+word[ind+1:])


def strategy_4(word):
    '''удаление одного символа'''
    for ind, syb in enumerate(word):
        words_lst.append(word[:ind]+word[ind+1:])


strategy_1(key_word)
strategy_2(key_word)
strategy_3(key_word)
strategy_4(key_word)

word_domain = []

for w in words_lst:
    for d in domain_zone:
        word_domain.append(f'{w}.{d}')


def main_func(host):
    try:
        s = socket.gethostbyname(host)
        print(f'Domain {host} \tIP {s}')
    except:
        pass


for host in word_domain:
    flow = threading.Thread(target=main_func, args=(host,))
    flow.start()
