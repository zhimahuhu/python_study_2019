def iszhishu(tmpint):
    if tmpint < 2:
        return False
    elif tmpint == 2:
        return True
    else:
        x = int(tmpint ** 0.5)
        for tmp in range(2, x + 1):
            if tmpint % tmp == 0:
                return False
        return True


def get_zhishu_list(num):
    tmplist = []
    for i in range(num + 1):
        if iszhishu(i):
            tmplist.append(i)
    return tmplist


def get_prime_list(count):
    prime_list = [2]
    j = 0
    prime = 2
    while j < count:
        prime += 1
        for tmp in prime_list:
            if prime % tmp == 0:
                break
        else:
            prime_list.append(prime)
            j += 1
    return prime_list


def get_prime_list_by_max(num):
    prime_list = [2]
    j = 0
    prime = 2
    while prime < num:
        prime += 1
        for tmp in prime_list:
            if prime % tmp == 0:
                break
        else:
            prime_list.append(prime)
            j += 1
    return prime_list


if __name__ == '__main__':
    prime_list0 = get_zhishu_list(128)
    print(prime_list0)

    prime_list1 = get_prime_list(-1)
    print(prime_list1)

    prime_list3 = get_prime_list_by_max(-1)
    print(prime_list3)
