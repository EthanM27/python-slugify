#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
   from slugify import slugify


@atheris.instrument_func
def test_input(data):
    fdp = atheris.FuzzedDataProvider(data)
    orig = fdp.ConsumeUnicode(4096)

    non = [" "]

    slugged = slugify(orig, allow_unicode=True)
    for c in non:
        if c in slugged:
            raise Exception("spaces detected when they shouldn't be")


def main():
    atheris.Setup(sys.argv, test_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
