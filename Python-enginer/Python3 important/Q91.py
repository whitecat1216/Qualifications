# 【問題９１】 次のコードを実行した場合、headers変数に含まれるデータとして、適切なものはどれですか？
import urllib.request

req=urllib.request.Request("http://example.com")
responce=urllib.request.urlopen(req)
headers=responce.getheaders()
print(headers)  # [('Content-Type', 'text/html; charset=UTF-8'), ('Content-Length', '1256'), ('Connection', 'keep-alive')]
# ④HTTPレスポンスヘッダーのキーと値を持つ辞書