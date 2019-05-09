import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-varone", type=int, required=True,
                    metavar="ONE",
                    help="Var one description")
parser.add_argument("-vartwo", type=str, required=False,
                    metavar="TWO",
                    help="Var two description")
args = parser.parse_args()

varone = args.varone
vartwo = args.vartwo