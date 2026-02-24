#1
# a="1000'
# print(int(a))
# SyntaxError: unterminated string literal (detected at line 2)
stocks={"apple":150, "banan":190,"birthday":180}
key=input("値引きしたい果物")
off_percent=input("値引き率(%):")
try:
    race=(100-int(off_percent))/100
    new_price=int(stocks[key]*race)
    stocks[key]=new_price
except(ValueError,KeyError):
    print("エラーが発生しました")
#3
try:
     raise ValueError("ValueErrorです")
except ValueError as error:
    print(error)
#4
def divide(number,divider):
    try:
        answer=number/divider
        return answer
    except ZeroDivisionError:
        print("ゼロ除算が行われました")
    except TypeError:
        print("引数の型が不正です")
    finally:
        print("--finall節の処理--")
answer=divide(100,"0")
print(f"結果:{answer}")