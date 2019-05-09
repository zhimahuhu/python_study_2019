import threading
import random
from faker import Faker

if __name__ == '__main__':
    tmp_ssn = Faker(locale='zh_CN').ssn()
    print(tmp_ssn)
