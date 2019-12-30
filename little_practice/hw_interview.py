import re


def find_pos(str1, str2):
    if str1 not in str2:
        print('bu cun zai')
    else:
        print(str2.index(str1) + 1)
        print(re.search(str1, str2).span()[0] + 1)


def get_ip(ip_str):
    # pattern = re.compile(
    #     r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)')
    # ip_list = []
    # result = pattern.findall(ip_str)
    # print(result)
    ip_list = []
    ip_str_len = len(ip_str)
    for i in range(1, 4):
        if i >= ip_str_len:
            break
        for j in range(i + 1, i + 4):
            if j >= ip_str_len:
                continue
            for k in range(j + 1, j + 4):
                if k >= ip_str_len:
                    continue
                # print('i', i, 'j', j, 'k', k)
                a = ip_str[:i]
                b = ip_str[i:j]
                c = ip_str[j:k]
                d = ip_str[k:]
                # print('a', a, 'b', b, 'c', c, 'd', d)
                if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255:
                    continue
                ip_s = '.'.join([a, b, c, d])
                if len(ip_s) != len(ip_str) + 3:
                    continue
                ip_list.append(ip_s)
    print(ip_list)


def test_re(str1):
    pattern = re.compile(r'.*(\d).*')
    print(pattern.findall(str1))


if __name__ == '__main__':
    print('debug')
    get_ip('25525511135')
    # find_pos('abc', '34abchjk')
    # test_re('12345')
