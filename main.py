from swinpy import *


import argparse
# usage: app parse <filename> [-d <output-directory>|--print]
parser = argparse.ArgumentParser(
    description='Swing Parser, translates python classes into almost ready to use javax swing application')
parser.add_argument('filename', help='input file')
parser.add_argument('-d', '--directory',
                    help='output directory', default="build")
parser.add_argument('--print', help='print to stdout', action='store_true')
args = parser.parse_args()
source = open(args.filename, 'r').read()
result: JFrame = eval(source)
build = result.build()
if args.print:
    print(build)

elif args.directory:
    if not os.path.exists(args.directory):
        os.makedirs(args.directory)
    with open(os.path.join(args.directory, os.path.basename("Application.java")), 'w') as f:
        f.write(build)
        print(f"Saved to {args.directory}")
