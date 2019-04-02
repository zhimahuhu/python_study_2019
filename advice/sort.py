import random


def bubble(tmplist):
    count = 0
    for i in range(len(tmplist)):
        count += 1
        flag = True
        for j in range(len(tmplist) - i - 1):
            if tmplist[j] > tmplist[j + 1]:
                tmplist[j], tmplist[j + 1] = tmplist[j + 1], tmplist[j]
                flag = False
        if flag:
            print('hah', count)
            return tmplist
    print(count)
    return tmplist


if __name__ == '__main__':
    # test_tmplist_1 = [2, 1, 6, 3, 7]
    # assert bubble(test_tmplist_1) == [1, 2, 3, 6, 7]
    #
    # test_tmplist_2 = [0]
    # assert bubble(test_tmplist_2) == [0]
    #
    # test_tmplist_3 = [1, 1, 1, 1, 1]
    # assert bubble(test_tmplist_3) == [1, 1, 1, 1, 1]
    #
    # test_tmplist_4 = [1, 2, 3, 4, 5]
    # assert bubble(test_tmplist_4) == [1, 2, 3, 4, 5]
    #
    # test_tmplist_5 = [0.1, 0.5, 0.6, 0.7]
    # assert bubble(test_tmplist_5) == [0.1, 0.5, 0.6, 0.7]
    #
    # test_tmplist_6 = [0.1, 1, 0.7, 0.6]
    # assert bubble(test_tmplist_6) == [0.1, 0.6, 0.7, 1]
    #
    # test_tmplist_7 = [100, 1000, 10]
    # assert bubble(test_tmplist_7) == [10, 100, 1000]

    test_tmplist_8 = random.sample(range(-1000, 1000), 10)
    print(test_tmplist_8)
    sort_list = bubble(test_tmplist_8)
    print(sort_list)
    for i in range(len(sort_list) - 1):
        assert sort_list[i] < sort_list[i + 1], "排序有误"
