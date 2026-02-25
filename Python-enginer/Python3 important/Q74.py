#【問題７４】
import argparse
parser = argparse.ArgumentParser()  # ← () が必要！
parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity")
args = parser.parse_args() 
print(f"Verbosity level: {args.verbose}")