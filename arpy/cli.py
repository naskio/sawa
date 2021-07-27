#!/usr/bin/env python3
'''
ꦱꦮ is an open source programming language, an interpreter to be precise, where you can write Python code using Javanese character.
https://github.com/naskio/arpy/docs/
Licensed under ABRMS License
Copyright (c) 2021 ꦱꦮ  
'''
import sys
import os
import argparse
import arpy.main as mn
from subprocess import call


def error(_error, message):
    """ Print errors to stdout
    """
    print("[-] {}: {}".format(_error, message))
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description='Extensions')
    parser.add_argument('name', type=str, help='filename with extension .بايثون')
    args = parser.parse_args()

    if not 'بايثون' in args.name:
        error("Error",
              "Please use .بايثون as extension.")
    file_name = args.name.split('.')
    if os.path.isfile(file_name[0] + '.py'):
        os.remove(file_name[0] + '.py')
    mn.main(args.name)
    call('python3 %s.py' % (file_name[0]), shell=True)
    os.remove(file_name[0] + '.py')


def run_as_command():
    version = ".".join(str(v) for v in sys.version_info[:2])
    if float(version) < 3.6:
        print("[-] بايثون بالعربي يتطلب الاصدار 3.6 او اكثر للبايثون")
        sys.exit(0)

    main()


if __name__ == '__main__':
    main()
