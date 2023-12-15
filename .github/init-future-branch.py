#!/usr/bin/env python

import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('branch', type=str)
args = parser.parse_args()

try:
    term = re.match(r'^future-(?:[ws]{2})-?(?:20)?([0-9]{2})$', args.branch).group(1)
    term = int(term)
except AttributeError:
    print(f'Malformed branch name: "{args.branch}"')
    sys.exit(1)

preamble_filename = 'assignments/preamble.sty'
with open(preamble_filename) as fp:
    preamble = fp.read()

def get_substitution(tex):
    match = re.search(r'\\courseterm\{(.*?)([0-9]{2})/(20)?[0-9]{2}\}', tex)
    token = match.group(0)
    replacement = r'\courseterm{' + match.group(1) + str(term) + '/' + match.group(3) + str(term + 1) + '}'
    return token, replacement

token, replacement = get_substitution(preamble)
preamble = preamble.replace(token, replacement)
assert get_substitution(preamble)[0] == replacement

with open(preamble_filename, 'w') as fp:
    fp.write(preamble)
