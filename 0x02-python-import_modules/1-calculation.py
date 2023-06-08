#!/usr/bin/python3
    if __name__ == "__main__":
      a = 10
      b = 5
      from calculator_1 import add, sub, mul, div
      text = "{} {} = {}"
      print(text.format(a, '+', b, add(a, b)))
      print(text.format(a, '-', b, sub(a, b)))
      print(text.format(a, '*', b, mul(a, b)))
      print(text.format(a, '/', b, div(a, b)))
