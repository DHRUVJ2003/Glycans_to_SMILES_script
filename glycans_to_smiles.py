"""
/******************************************************************************
  This source file is part of the Avogadro project.

  This source code is released under the New BSD License, (the "License").
******************************************************************************/
"""

import argparse
import json
import sys
from glyles import convert

# Some globals:
debug = True


def getOptions():
    userOptions = {}

    userOptions['glycan'] = {}
    userOptions['glycan']['label'] = 'convert glycan to smiles'
    userOptions['glycan']['type'] = 'string'
    userOptions['glycan']['default'] = "Gal"

    opts = {'userOptions': userOptions}

    return opts


def convert_to_smiles(opts):
    glycan= opts['glycan']
    smiles=convert(glycan)
    return smiles


def runCommand():
    # Read options from stdin
    stdinStr = sys.stdin.read()

    # Parse the JSON strings
    opts = json.loads(stdinStr)

    # Prepare the result
    result = convert_to_smiles(opts)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Convert glycans/sugars to smiles')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--print-options', action='store_true')
    parser.add_argument('--run-command', action='store_true')
    parser.add_argument('--display-name', action='store_true')
    parser.add_argument('--menu-path', action='store_true')
    parser.add_argument('--lang', nargs='?', default='en')
    args = vars(parser.parse_args())

    debug = args['debug']

    if args['display_name']:
        print("Convert to smiles")
    if args['menu_path']:
        print("&Build")
    if args['print_options']:
        print(json.dumps(getOptions()))
    elif args['run_command']:
        print(json.dumps(runCommand()))
