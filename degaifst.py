
from td2dot import read_graph_in
from collections import defaultdict as ddict
from itertools import combinations

VERSION = "0.0 alpha"

if __name__ == "__main__":
    '''
    Taken from laibgaf/redecomp.py, initially verbatim, to be finished
    '''

    # Handle the input
    filename = "e7" 
    # ~ filename = "titanic_" # TO BE REPLACED BY ARGUMENT PARSING AS FOLLOWS

    # ~ from argparse import ArgumentParser
    # ~ argp = ArgumentParser(
        # ~ description = ("Construct dot-coded decomposition of a graph or 2-structure"),
        # ~ prog = "python[3] redecomp.py or just ./redecomp"
        # ~ )

    # ~ argp.add_argument('-V', '--version', action = 'version', 
                                         # ~ version = "redecomp " + VERSION,
                                         # ~ help = "print version and exit")

    # ~ argp.add_argument('dataset', nargs = '?', default = None, 
                      # ~ help = "name of optional dataset file (default: none, ask user)")
    
    # ~ args = argp.parse_args()

    # ~ if args.dataset:
        # ~ filename = args.dataset
    # ~ else:
        # ~ print("No dataset file specified.")
        # ~ filename = input("Dataset File Name? ")
    
    if '.' in filename:
        fullfilename = filename
        filename, ext = filename.split('.', maxsplit = 1)
        if ext != "td":
            print("Found extension", ext, "instead of td for file", filename)
    else:
        fullfilename = filename + ".td"

    # Construct labeled graph: labels are filtered multiplicities
    g, items = read_graph_in(fullfilename)
