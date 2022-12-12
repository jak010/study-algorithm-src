import sys


def count_character(strings):
    """ 입력받은 알파벳의 개수를 카운팅함 """
    alphabet_dict = {}
    for ch in strings.replace("\n", ""):
        ch = ch.upper()
        if ch not in alphabet_dict:
            alphabet_dict[ch] = 1
        else:
            alphabet_dict[ch] += 1
    return alphabet_dict


def get_value_max_key():
    """ 알파벳 카운팅 dict에서 value가 가장 큰 값을 뽑아 list로 뽑아냄"""

    _ch_list = []
    for key, val in alphabet.items():
        if val == max(alphabet.values()):
            _ch_list.append(key.upper())
    return _ch_list


def show_print(alphabet: list):
    """ 조건에 따라 어떤 문자를 print 할지 고름 """
    if len(alphabet) > 1:
        print("?")
    else:
        print(alphabet[0])


if __name__ == '__main__':
    strings = str(sys.stdin.readline())

    alphabet = count_character(strings)
    _chs = get_value_max_key()
    show_print(_chs)
