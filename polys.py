import argparse
import requests
from PIL import Image


class Polynom:
    def __init__(self, arr):
        self.arr = arr
        self.rate = len(arr) - 1

    def __str__(self):
        res = ''
        for i in range(len(arr)):
            if i == self.rate - 1:
                res += str(arr[i])
            elif i == self.rate - 2:
                res += str(arr[i]) + 'x + '
            else:
                res += str(arr[i]) + 'x^' + str(i) + ' + '
        return res


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
