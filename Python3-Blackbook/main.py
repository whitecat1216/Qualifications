import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--command")
parser.add_argument("target",narga="+")
args=parser.parse_args()
print(args)
