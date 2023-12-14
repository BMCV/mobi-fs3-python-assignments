#!/usr/bin/env python

from datetime import date
import os
import pathlib


today  = date.today()
year   = today.year % 2000
branch = f'future-ws{year + 1}'

init_script_filename = pathlib.Path(__file__).parents[0] / 'init-future-branch.py'

os.system(f'git checkout -b {branch}')
os.system(f'python {init_script_filename} {branch}')
