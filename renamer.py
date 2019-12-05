import re
import os
import argparse
from datetime import datetime
import time

parser = argparse.ArgumentParser(description='Renames all files in a directory to their creation date')
parser.add_argument('--recursive', type=bool, default=True, help='Should files be renamed recursively')
parser.add_argument('--dir', type=str, default=os.getcwd(), help='Directory to start in')
parser.add_argument('--regex', type=str, default="(.*).MOV", help='Get specific with filenames')

def doRename(r, fn):
    initial_name = os.path.join(r, fn)
    print initial_name + " > " + datetime.fromtimestamp(os.path.getmtime(initial_name)).strftime("%Y_%m_%d__%H_%M_%S")

if __name__ == "__main__":
    args = parser.parse_args()

    for r, d, f in os.walk(args.dir):
        for fn in f:
            if(re.search(args.regex, fn)):
                doRename(r, fn)
