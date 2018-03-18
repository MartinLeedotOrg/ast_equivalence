#!/usr/bin/env python3
import ast
import unittest
import argparse
import dis

parser = argparse.ArgumentParser()
parser.add_argument("File1")
parser.add_argument("File2")
parser.add_argument("-v", dest="verbose", action="store_true")
args = parser.parse_args()


def get_bytecode(filename):
    with open(filename) as f:
        code = ast.parse(f.read())
        bytecode = dis.Bytecode(compile(code, '<string>', 'exec')).dis()
    return bytecode


bytecode1 = get_bytecode(args.File1)
bytecode2 = get_bytecode(args.File2)

if args.verbose:
    print(bytecode1)
    print(bytecode2)


class TestStringMethods(unittest.TestCase):
    if args.verbose:
        maxDiff = None

    def test_upper(self):
        self.assertEqual(bytecode1, bytecode2)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner().run(suite)
