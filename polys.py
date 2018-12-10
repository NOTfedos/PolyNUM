import argparse
import requests
from PIL import Image

VALID_SYMBOLS = '-+x^'


class InvalidMults(BaseException):
    pass


def get_elem(arr, el):
    for x in arr:
        if x[1] == el:
            return x[0]
    return 0


def get_arrs(s):
    s = s.replace(' ', '')
    s = s.lower()
    res = []
    for j in range(len(s)):
        el = s[j]
        if not (el.isdigit() or (el in VALID_SYMBOLS)):
            raise InvalidMults
    s = s.replace('-', '+-')
    arr = s.split('+')
    mults = []
    flag = False
    max_rate = 0
    for el in arr:

        if el == '':
            continue

        degr = [0, 0]  # first - value, second - rank

        if '^' in el:
            el = el.replace('x', '')
            degr = el.split('^')
            if degr[0] == '':
                degr[0] = '1'
            if degr[0] == '-':
                degr[0] = '-1'
        else:  # if rank lower 2
            if 'x' in el:  # if rank eq 1
                degr[1] = '1'
                el = el.replace('x', '')
                if el == '':  # x
                    degr[0] = '1'
                else:
                    degr[0] = el
            else:  # if it's constant
                degr[1] = '0'
                degr[0] = el
        for i in range(len(mults)):
            if mults[i][1] == int(degr[1]):
                mults[i][0] += int(degr[0])
                flag = True
                break

        if not flag:
            mults.append([int(degr[0]), int(degr[1])])

        flag = False

        if int(degr[1]) > max_rate:
            max_rate = int(degr[1])

    for i in range(max_rate + 1):
        res.append(get_elem(mults, max_rate - i))

    return res


def sum(s1, s2):
    p1 = Polynom(s1)
    p2 = Polynom(s2)
    r = p1 + p2
    return str(r)


def sub(s1, s2):
    p1 = Polynom(s1)
    p2 = Polynom(s2)
    r = p1 - p2
    return str(r)


def mult(s1, s2):
    return ''


def div(s1, s2):
    return ''


def dxdy(s):
    return ''


class Polynom:
    def __init__(self, identifier):

        if type(identifier).__name__ == 'list':
            self.arr = identifier
            self.rate = len(identifier) - 1
            for el in identifier:
                try:
                    int(el)
                except ValueError:
                    raise InvalidMults
        elif type(identifier).__name__ == 'str':
            self.arr = get_arrs(identifier)
            self.rate = len(self.arr) - 1
        elif type(identifier).__name__ == 'int':
            self.arr = [identifier]
            self.rate = 0
        elif type(identifier).__name__ == 'Polynom':
            self.arr = identifier.arr
            self.rate = identifier.rate
        else:
            raise InvalidMults

    def __str__(self):
        res = []
        for i in range(len(self.arr)):
            if self.arr[i] != 0:

                if self.arr[i] == 1:
                    m = ''
                else:
                    m = str(self.arr[i])

                if i < self.rate - 1:
                    res.append(m + 'x^' + str(self.rate - i))
                else:
                    if i == self.rate - 1:
                        res.append(m + 'x')
                    elif i == self.rate:
                        res.append(str(self.arr[i]))
        return ' + '.join(res)

    def __add__(self, other):
        smults = self.arr[:]
        omults = other.arr[:]
        res = []

        if other.rate > self.rate:
            for i in range(other.rate - self.rate):
                smults = [0] + smults
        else:
            for i in range(self.rate - other.rate):
                omults = [0] + omults
        for i in range(max(self.rate, other.rate) + 1):
            res.append(smults[i] + omults[i])

        return Polynom(res)

    def __sub__(self, other):
        smults = self.arr[:]
        omults = other.arr[:]
        res = []

        if other.rate > self.rate:
            for i in range(other.rate - self.rate):
                smults = [0] + smults
        else:
            for i in range(self.rate - other.rate):
                omults = [0] + omults

        for i in range(max(self.rate, other.rate) + 1):
            res.append(smults[i] - omults[i])

        while res[0] == 0:
            res = res[1:]

        return Polynom(res)

    def calculate(self, x):
        if self.rate == 0:
            return self.arr[0]
        else:
            res = self.arr[0] * x + self.arr[1]
            j = 1
            for i in range(self.rate - 1):

                try:
                    a = self.arr[j + 1]
                    j = j + 1
                except BaseException:
                    pass

                res = res * x + a
            return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', default='output.gif')
    parser.add_argument('val')
    args = parser.parse_args()
    c = requests.get('http://latex.codecogs.com/gif.latex?', params=eval(args.val),
                     stream=True)
    img = Image.open(c.raw)
    img.show()
    img.save(args.o)
    try:
        print(eval(args.val))
    except InvalidMults:
        print('Invalid command')


if __name__ == '__main__':
    main()
