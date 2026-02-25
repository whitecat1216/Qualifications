#【問題７０】
# 次のコードを実行した場合の出力として、適切なものはどれですか
import argparse

parser = argparse.ArgumentParser()  # ← () が必要！

parser.add_argument("-n", "--name", required=True, help="Specify the name")
parser.add_argument("-a", "--age", type=int, help="Specify the age")

args = parser.parse_args()

print(f"Name: {args.name}, Age: {args.age}")