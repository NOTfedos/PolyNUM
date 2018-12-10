import argparse
import requests
from PIL import Image


class InvalidMults(BaseException):
    pass


def get_elem(arr, el):
    for x in arr:
        if x[1] == el:
            return x[0]
    return 0


def get_arrs(s):
    s = s.replace(' ', '')
    res = []
    for el in s:
        if not (el.isdigit() or el == '^'):
            raise InvalidMults
    arr = s.split('+')
    mults = []
    flag = False
    max_rate = 0
    for el in arr:
        if '^' in el:
            degr = el.split('^')
            for i in range(len(mults)):
                el = mults[i]
                if el[1] == int(degr[1]):
                    mults[0] += int(degr[0])
                    flag = True
                    break
                if not flag:
                    mults.append([int(degr[0]), int(degr[1])])
            if int(degr[1]) > max_rate:
                max_rate = int(degr[1])
        else:
            for l in range(len(mults)):
                el = mults[l]
                if el[1] == 0:
                    mults[l][0] += int(el)
                    flag = True
                    break
    for i in range(max_rate + 1):
        res.append(get_elem(mults, max_rate - i))

    return res


class Polynom:
    def __init__(self, arr):

        if type(arr).__name__ == 'list':
            self.arr = arr
            self.rate = len(arr) - 1
            for el in arr:
                if not(el.isdigit()):
                    raise InvalidMults

        elif type(arr).__name__ == 'str':
            self.arr = get_arrs(arr)
            self.rate = len(self.arr) - 1

    def __str__(self):
        res = ''
        for i in range(len(self.arr)):
            el = self.arr[i]
            if i == self.rate - 1:
                if el == 0:
                    res = res[:-3]
                else:
                    res += str(el)
            elif i == self.rate - 2:
                res += str(el) + 'x + '
            else:
                if el != 0:
                    res += str(el) + 'x^' + str(i) + ' + '
        return res

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--latex-name', '-lm', default='output.gif')
    parser.add_argument('val')
    args = parser.parse_args()
    c = requests.get('http://latex.codecogs.com/gif.latex?', params=eval(args.val),
                     stream=True)
    img = Image.open(c.raw)
    img.show()
    img.save(args.latex_name)
    print(eval(args.val))


if __name__ == '__main__':
    main()
