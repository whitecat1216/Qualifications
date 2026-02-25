# 【問題７８】
# 次のコードについて、glob.glob("data/**/*.txt", recursive=True)が返す結果に関する説明として、適切なものはどれですか？
import glob
result = glob.glob("data/**/*.txt", recursive=True)
print(result)  
# ①dataディレクトリ内のすべての.txtファイルを検索する 
# ②Dataディレクトリ以下のすべてのサブディレクトリを含む.txtファイルを検索する 
# ③現在のディレクトリ内のすべての.txtファイルを検索する 
# ④dataディレクトリ内のすべてのファイルを検索する
# ②Dataディレクトリ以下のすべてのサブディレクトリを含む.txtファイルを検索する