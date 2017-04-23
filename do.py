#!/usr/bin/env python3

import sys
import os
import argparse
import subprocess

def run_tests(args):
    command = ["python3", "-m", "unittest"]
    if args.verbose:
        command.append('-v')
    subprocess.call(command, stdout=sys.stdout, stderr=sys.stderr)

def create_tarball(args):
    command = ["tar", "-c", "-X .gitignore", ".", "|", "bzip2", ">"]
    command.append(args.filename)
    print('Running:', ' '.join(command))
    subprocess.call(' '.join(command), shell=True, stdout=sys.stdout, stderr=sys.stderr)

def print_graph_viz(args):
    import project_support.graph_viz as gviz
    for filename in args.filename:
        gviz.print_graph_viz_representation(filename)

def start_ipython(args):
    command = ["ipython3"]
    subprocess.call(command, stdout=sys.stdout, stdin=sys.stdin, stderr=sys.stderr)

###
### Main parser
parser = argparse.ArgumentParser(description='Scaffolding to support project development.')
parser.set_defaults(func=lambda args: parser.print_usage())
subparsers = parser.add_subparsers(help='action to perform')


## Test subparser
test_parser = subparsers.add_parser('test', aliases=['tests'],
                                        description='Perform unit tests',
                                        help='Perform unit tests (-v for verbose)')
test_parser.set_defaults(func=run_tests)
test_parser.add_argument('-v', '--verbose', action='store_true')


## Tar subparser
tar_parser = subparsers.add_parser('tar', description='Package project up',
                                       help='Package project up (-h for options)')
tar_parser.set_defaults(func=create_tarball)
default_tar_filename = os.getenv('USER', '') + '_algorithms_project.tbz'
tar_parser.add_argument('-f', '--filename',
                            default=default_tar_filename,
                            help='name for the output tar file')

## Viz subparser
viz_parser = subparsers.add_parser('viz', description='Print graph viz representation of graph file',
                                       help='Print graph viz representation of filename')
viz_parser.set_defaults(func=print_graph_viz)
viz_parser.add_argument('filename', nargs='+',
                        help='graph file to print')

## REPL subparser
repl_parser = subparsers.add_parser('repl', description='Start an interactive python session',
                                        help='Start an interactive python session')
repl_parser.set_defaults(func=start_ipython)


###
### Parse and dispatch
args = parser.parse_args()
args.func(args)
