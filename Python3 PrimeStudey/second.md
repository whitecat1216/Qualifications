# Python3 エキスパート認定試験 対策問題集（第2回）

このドキュメントは Python の試験対策問題を**マークダウン形式**で整理し、**サルでもわかる**解説を付けたものです。

---

## 問1. Pythonの特徴

Pythonの特徴に関する次の記述のうち、**誤っているもの**はどれか。

- Pythonは柔軟な配列や集合、ディクショナリといった、非常に高水準のデータ型を組み込みで持つ。データ型の一般性が高いためPythonの対応可能な問題領域はAwkより広いが、**Perlと比べると同程度である。**
- Pythonは簡単に使えるとはいえ本格的なプログラム言語であり、大きなプログラムを書くために提供された構造やサポート、エラーチェック機構が、シェルスクリプトなどに比べはるかに多く存在する。
- PythonはWindows、MacOS、Linuxなど多くの環境で動作する、拡張可能なフリーのオープンソースソフトウェアである。
- Pythonでは、文のグルーピングはカッコで囲うことでなくインデントで行われるなど、プログラムを小さく読みやすく書けるという特徴がある。
- Pythonはインタープリタ言語であり、コンパイル等が必要でないため、プログラム開発における時間を節約してくれる。インタープリタは対話的に使うことも可能である。

### 正解

**「データ型の一般性が高いためPythonの対応可能な問題領域はAwkより広いが、Perlと比べると同程度である。」** が誤り。

### サルでもわかる解説

正しくは「**Perlより広い**」です。Pythonは書きやすさとできることの広さの両方で、Perlより対応できる分野が広いとされています。「Awkより広い」は正しいので、ひっかけは「Perlと同程度」の部分だけです。

---

## 問2. Pythonインタープリタ

Pythonインタープリタに関する次の記述のうち、**誤っているもの**はどれか。

- 標準入力がttyデバイスに接続された状態で起動した場合は、コマンドを対話的に読み込んで実行するが、引数にファイル名を与えたり、標準入力からファイルを与えて起動した場合は、このファイルに入った「スクリプト」を読み込んで実行する。
- インタープリタがスクリプト名（スクリプトのファイル名）と続く引数群を知らされると、これらは文字列のリストとなる。**import listitems を実行することで、このリストにアクセスできる。**
- デフォルトの設定では、プライマリプロンプトの記号は「>>>」、セカンダリプロンプトの記号は「…」である。
- インタープリタを対話モードで起動すると、はじめにバージョンと著作権からはじまるメッセージが表示され、その後にプライマリプロンプトが表示される。
- プログラムの冒頭で「# coding: （エンコーディング方式）」のようにすると、デフォルト以外のエンコーディングを使うことも可能である。

### 正解

**「import listitems を実行することで、このリストにアクセスできる。」** が誤り。

### サルでもわかる解説

コマンドライン引数（スクリプト名やその後の引数）にアクセスするのは **`sys.argv`** です。そのために **`import sys`** をして、`sys.argv` というリストを使います。**`listitems` というモジュールは存在しません**。名前が似ているだけのひっかけです。

---

## 問3. 数値

数値に関する次の記述のうち、**正しいもの**はどれか。

- 演算を行うための「 + 」や「 - 」などの記号はオペランドと呼ばれ、演算の対象は演算子と呼ばれる。
- 切り下げ除算を行って整数解を得たい場合（剰余を捨てたい場合）は「 / 」を使い、剰余のみ得たい場合は「 // 」を使う。
- **変数は、定義（値の代入）や宣言がなされないまま使おうとするとエラーとなる。**
- 整数はintという型を持つ。小数点を伴う数はfloatという型を持つ。除算は常にfloatを返す。
- 対話モードでは、最後に表示した式を変数「**」（アスタリスク2つ）に代入してある。

### 正解

**「変数は、定義（値の代入）や宣言がなされないまま使おうとするとエラーとなる。」**

### サルでもわかる解説

オペランド＝演算の**対象**（数など）、演算子＝「+」や「-」などの**記号**。問題文は逆になっているので誤り。切り下げ除算（商だけ欲しい）は **`//`**、剰余は **`%`**。`/` と `//` が逆の説明なので誤り。除算 `/` は Python 3 では常に float を返すが、「除算は常に float」だけだと `//` を忘れているので不正確。最後の式の結果が入る変数は **`_`**（アンダースコア1つ）。`**` ではない。よって、唯一正しいのは「未定義の変数を使うとエラー」です。

---

## 問4. 演算の実行結果

次のコードの実行結果として正しいものはどれか。

```python
a = 2
b = a ** 3
c = b / 2 + 3
d = 10
e = d // b
f = d % c
print('{1}, {0}'.format(e, f))
```

- 3.0, 1
- 3.0, 1.25
- 1.0, 1.25
- 4.0, 1
- 1.6666666666666667, 1

### 正解

**3.0, 1**

### サルでもわかる解説

- `a=2`, `b=8`, `c=7`, `d=10`, `e=10//8=1`, `f=10%7=3`
- `format(e, f)` では 0番目＝e、1番目＝f。`'{1}, {0}'` は「先に f、次に e」を表示するので「3, 1」です。

---

## 問5. 文字列

文字列に関する次の記述のうち、**正しいもの**はどれか。なお「\」はバックスラッシュに読み替えること。

- バックスラッシュを前置した文字が特殊文字に解釈されるのが嫌な時は、最初の引用符の前に「print(raw'C:\some\name')」のように「raw」を記述する。
- 文字列リテラルを複数行にわたり書く一つの方法は、トリプルクオートを使う方法である。最初の改行などの行末文字が文字列に含まれることを避けたい場合は、行末に「-」を置く。
- 変数と文字列リテラルの連結、そして変数同士の連結には「.」（ドット）を使う。
- 文字列は「*」で繰り返すことができる。「'w' + 3 * 'o'」は対話型インタープリタで出力「wwwo」が得られる。
- **対話型インタープリタでは文字列は引用符に囲まれ、特殊文字はバックスラッシュでエスケープされた状態で出力される。print()関数では全体を囲む引用符が除去され、エスケープ文字や特殊文字がプリントされた状態で出力される。**

### 正解

**「対話型インタープリタでは文字列は引用符に囲まれ……print()関数では全体を囲む引用符が除去され、エスケープ文字や特殊文字がプリントされた状態で出力される。」**（上記最後の選択肢）

### サルでもわかる解説

raw 文字列は先頭に **`r`** を付ける（例：`r'C:\some\name'`）。「raw」という単語は使わない。複数行で行末を文字列に含めたくないときは行末に **`\`** を置く。「-」ではない。文字列の連結は **`+`**。`.` はメソッド呼び出し用。`'w' + 3*'o'` は **`'wooo'`**（wが1つ、oが3つ）。「wwwo」ではない。対話モードでは引用符付き・エスケープ見える形、print() では人が読む形で出力、という説明が正しいです。

---

## 問6. スライスと format（sNow）

以下の結果を得たい場合、コードの【A】に入るものとして正しいものはどれか。

**[実行結果]**  
sNow

**[コード]**

```python
Zen = 'NowIsBetterThanNever'
print('{}{}{}'.format(【A】))
```

- Zen[5], Zen[-4], Zen[2:4]
- Zen[4], Zen[-6], Zen[1:3]
- **Zen[4], Zen[-5], Zen[1:3]**
- Zen[4], Zen[-5], Zen[1:2]
- Zen[5], Zen[-4], Zen[1:3]

### 正解

**Zen[4], Zen[-5], Zen[1:3]**

### サルでもわかる解説

インデックスは0始まり。**Zen[4]**＝5文字目＝**'s'**。**Zen[-5]**＝後ろから5番目＝**'N'**（-1=r, -2=e, -3=e, -4=V, -5=N）。**Zen[1:3]**＝1番目～2番目＝**'oW'**。つなげると **s + N + oW = "sNow"** になります。

---

## 問7. エラーとならない操作

次の変数 Zen に関して指定した場合、実行時に**エラーとならない**ものはどれか。

```python
Zen = 'BeautifulIsBetterThanUgly'
```

- **Zen[1000:10000]**
- Zen[50]
- Zen[10] = 'a'
- Zen['B']
- Zen[1:10] + b

### 正解

**Zen[1000:10000]**

### サルでもわかる解説

スライス（`[始まり:終わり]`）は、範囲外でも**空文字列 `''` を返すだけ**でエラーになりません。Zen[50]は IndexError、Zen[10]='a' は文字列がイミュータブルで TypeError、Zen['B'] はインデックスは整数で TypeError、Zen[1:10]+b は b が未定義で NameError になります。

---

## 問8. while とフィボナッチ

次のコードの実行結果として正しいものはどれか。

```python
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a+b
```

- 1,1,2,3,5,8,
- **0,1,1,2,3,5,8,**
- 1,2,3,5,8,13,
- 0,1,2,3,5,8,
- 0,1,2,2,3,5,

### 正解

**0,1,1,2,3,5,8,**

### サルでもわかる解説

最初に a=0 を表示してから a,b=1,1。次に a=1 を表示して a,b=1,2。その次 a=2 → a,b=2,3 … とフィボナッチ数列になり、a&lt;10 の間だけなので最後は 8 まで。表示は「0,1,1,2,3,5,8,」です。

---

## 問9. リストの append / insert と for

次のコードの実行結果として正しいものはどれか。

```python
months = ['January', 'March', 'May', 'July']
months.append('September')
for month in months[:]:
    if len(month) > 5:
        months.insert(0,month)

print(months, end = '')
```

- ['March', 'January', 'January', 'March', 'May', 'July']
- ['March', 'January', 'January', 'March', 'May', 'July', 'September']
- ['September', 'March', 'January', 'January', 'March', 'May', 'July', 'September']
- **['September', 'January', 'January', 'March', 'May', 'July', 'September']**
- ['September', 'March', 'January', 'May', 'July']

### 正解

**['September', 'January', 'January', 'March', 'May', 'July', 'September']**

### サルでもわかる解説

append で末尾に September 追加。for month in months[:] でコピーを回しているので、ループ中にリストを変えてもループ順は変わらない。len(month)&gt;5 のときだけ insert(0, month) で先頭に挿入。6文字より長いのは January, July, September。この順で先頭に挿入されていくので、上記の並びになります。

---

## 問10. 素数判定（【A】【B】）

次の結果を得たい場合、コード【A】【B】に入る組み合わせとして適切なものはどれか。なお【A】は★aの行と、【B】は★bの行と同じ数の空白でインデントされている。

**[実行結果]**

```
2 is a prime number
3 is a prime number
4 equals 2 * 2
...
```

**[コード]**

```python
for n in range(2, 10):
    for x in range(2, n):  # ★b
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)  # ★a
            【A】
    【B】
        print(n,'is a prime number')
```

- 【A】continue 【B】 else:
- 【A】continue 【B】 else
- 【A】break 【B】 each:
- 【A】break: 【B】 else
- **【A】break 【B】 else:**

### 正解

**【A】break 【B】 else:**

### サルでもわかる解説

n % x == 0 のときは「n = x * (n//x)」と表示してその n の判定を終えるので **break**。for ループの **else** は「break で抜けなかったときだけ」実行される。つまり「どの x でも割り切れなかったとき」＝素数なので、【B】は **else:** で「素数」を表示。「each:」や「else」だけ（コロンなし）は文法エラーなので×。

---

## 問11. range(-3, -18, -3)

次のコードの実行結果として正しいものはどれか。

```python
for i in range(-3, -18, -3):
    print(i, end=", ")
```

- -3, 0, 3, 6, 9, 12, 15,
- -3, -6, -9, -12, -15, -18,
- **-3, -6, -9, -12, -15,**
- -6, -9, -12, -15, -18,
- -6, -9, -12, -15,

### 正解

**-3, -6, -9, -12, -15,**

### サルでもわかる解説

range(始まり, 終わり, ステップ) で、**終わりは含まない**。-3 から -3 ずつ進めて -18 の手前（-15）まで。だから -3, -6, -9, -12, -15 の5個。**-18 は出てこない**。

---

## 問12. enumerate の代替

次の結果を得たい場合、コードの2行目以降を代替するものとして正しいものはどれか。なお各選択肢の次の行には「 print(i, Zen[i]) 」が記述されるものとする。

**[実行結果]**

```
0 Now
1 is
2 better
3 than
4 never
```

**[コード]**

```python
Zen = ['Now','is','better','than','never']
for i, v in enumerate(Zen):
    print(i, v)
```

- **for i in range(len(Zen)):**
- in i for Zen[0:5]:
- for i in range(Zen[0:5]):
- while i < range(len(Zen)):
- while i < len(Zen):

### 正解

**for i in range(len(Zen)):**

### サルでもわかる解説

enumerate(Zen) は「(0, 先頭の要素), (1, 2番目), …」を返す。同じことをするには i を 0～len(Zen)-1 で回して Zen[i] を使えばよい。つまり **for i in range(len(Zen)):** が正解。「in i for」「while i < range(...)」などは文法として不正なので×。

---

## 問13. グローバル変数と関数

次のコードの実行結果として正しいものはどれか。

```python
i = 1
i = 2

def f(arg):
    i = 3
    print(arg)

i = 4
i = 5

f(i)
```

- 1
- 2
- 3
- 4
- **5**

### 正解

**5**

### サルでもわかる解説

グローバルで i が何度か代入され、最後が i=5。f(i) は f(5) なので arg=5。関数内の i=3 はローカルの i で、arg には影響しない。print(arg) なので **5** が出力されます。

---

## 問14. 可変デフォルト引数（【A】の出力）

次のコードに関し、【A】の行の出力として正しいものはどれか。

```python
def culc(a, b, squares=[], cubes=[]):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(2,2))
print(culc(3,3))
print(culc(4,4))  # 【A】
print(culc(5,5))
```

- ([16], [64])
- ([4, 8], [9, 27], [16, 64])
- ([4, 6, 8], [6, 9, 12])
- **([4, 9, 16], [8, 27, 64])**
- ([8, 27, 64], [4, 9, 16])

### 正解

**([4, 9, 16], [8, 27, 64])**

### サルでもわかる解説

デフォルト引数の squares=[], cubes=[] は、関数定義時に1回だけ作られたリストをずっと使い回します。1回目: squares=[4], cubes=[8]。2回目: [4,9], [8,27]。3回目: [4,9,16], [8,27,64]。だから print(culc(4,4)) では **([4, 9, 16], [8, 27, 64])** が正解です。

---

## 問15. キーワード引数

次の関数を呼び出す際に、引数の指定として**正しい**ものはどれか。

```python
def location(city, state='NewYork', country='USA'):
    print("I live in", country, ".")
    print("My company is located in", city, ",", state, ".")
```

- location(city='chiyoda', state='Tokyo', zipcode='1000004')
- location(state='California', country='USA', 'San Francisco')
- **location(state='Jakarta', city='Cikini')**
- location('Geelong', city='Melbourne')
- location()

### 正解

**location(state='Jakarta', city='Cikini')**

### サルでもわかる解説

city は必須（デフォルトなし）。state と country は省略可能。正解では city と state がキーワードで指定されており、country は省略なのでデフォルトの 'USA' が使われます。他は「必須の city がない」「位置引数がキーワード引数の後にある」などでエラーになります。

---

## 問16. *args と **kwargs（【A】【B】）

次のコード1行目の【A】【B】に入る組み合わせとして正しいものはどれか。

**[コード]**

```python
def shop(name, 【A】, 【B】):
    print("flowershop:", name)
    keys = sorted(argsX.keys())
    for kw in keys:
        print(kw, ":", argsX[kw])
    for Y in argsY:
        print(Y)

shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.", bouquet="Sunflower", plants="Pachira", dried="Rose")
```

- 【A】argsX 【B】argsY
- **【A】*argsY 【B】**argsX**
- 【A】**argsY 【B】*argsX
- 【A】*argsX 【B】**argsY
- 【A】**argsX 【B】*argsY

### 正解

**【A】*argsY 【B】**argsX**

### サルでもわかる解説

*argsY＝余った位置引数がタプルで入る。**argsX＝キーワード引数が辞書で入る。コード内で argsX.keys() を使っているので、argsX が辞書でないといけない → argsX は ** で受け取る。だから【A】*argsY 【B】**argsX が正解です。

---

## 問17. 関数注釈・docstring・PEP8

次の記述のうち、**誤っている**ものはどれか。

- 関数注釈（アノテーション）は関数の __annotations__ 属性にディクショナリとして格納され、関数のほかの部分にはいかなる影響も及ぼさない。
- **例えば「def func(a: int, b: str) -> value」と関数を記述したときにアノテーションに該当するものは「-> value」のみである。**
- docstringの1行目は、常にオブジェクトの目的の短く簡潔な要約を記述し、大文字で始まりピリオドで終わる行とすべきである。
- docstringに2行目以降がある場合、2行目は空行としてようやくと他の記述を視覚的に分離すべきである。
- PEP 8では、演算子の周囲やカンマの後ろにはスペースを入れるが、カッコのすぐ内側にはスペースを入れるべきではないとされる。

### 正解

**「例えば『def func(a: int, b: str) -> value』と関数を記述したときにアノテーションに該当するものは『-> value』のみである。」** が誤り。

### サルでもわかる解説

アノテーションは引数の **`: 型`** と戻り値の **`-> 型`** の**両方**を指します。なので「-> value のみ」という説明が誤りです。他の選択肢は正しい説明です。

---

## 問18. リスト内包（[0, 9, 36, 81]）

次の結果を得たい場合に、コードの1行目～3行目を代替するものとして正しいものはどれか。

**[実行結果]**  
[0, 9, 36, 81]

**[コード]**

```python
squares = []
for x in range(0, 10, 3):
    squares.append(x ** 2)
print(squares)
```

- squares = [x in x ** 2 for range(0, 10, 3)]
- squares = [x for x ** 2 in range(0, 10, 3)]
- squares = [x ** 2 in x for range(0, 10, 3)]
- squares = [x ** 2 for range(0, 10, 3) in x]
- **squares = [x ** 2 for x in range(0, 10, 3)]**

### 正解

**squares = [x ** 2 for x in range(0, 10, 3)]**

### サルでもわかる解説

range(0, 10, 3) → 0, 3, 6, 9。それぞれを2乗すると 0, 9, 36, 81。リスト内包の形は【結果 for 変数 in イテラブル】なので、**x ** 2 for x in range(...)** が正解です。

---

## 問19. 行列の転置（zip）

次の実行結果を得たい場合に、コードの2行目（★印の行）を代替するものとして正しいものはどれか。

**[実行結果]**  
[(1, 4, 8), (3, 9, 27), (5, 25, 125)]

**[コード]**

```python
matrix = [[1, 3, 5], [4, 9, 25], [8, 27, 125]]
power = [[row[i] for row in matrix] for i in range(3)]  # ★
print(power)
```

- **power = list(zip(*matrix))**
- power = list(sum(*matrix))
- power = list(zip(matrix))
- power = set(sum(*matrix))
- power = set(sum(matrix))

### 正解

**power = list(zip(*matrix))**

### サルでもわかる解説

*matrix でリストのリストを「1つずつ引数として」渡す。zip(リスト1, リスト2, リスト3) は「1番目同士、2番目同士、3番目同士」をタプルにする。つまり zip(*matrix) で「列」をまとめたタプルが得られ、転置になります。list(zip(...)) で同じ結果になります。

---

## 問20. リスト内包（組み合わせ）

次の実行結果を得たい場合に、コード1行目～5行目を代替するものとして正しいものはどれか。

**[実行結果]**  
[(1, 3), (1, 2), (1, 5), (2, 3), (2, 5), (3, 2), (3, 5)]

**[コード]**

```python
combs = []
for x in [1,2,3]:
    for y in [3,2,5]:
        if x != y:
            combs.append((x, y))
print(combs)
```

- combs = [(a,b) in a for [1,2,3] in b for [3,2,5] if a != b]
- combs = [[a,b] for a in [3,2,5] for b in [1,2,3] if a = b]
- combs = [(a,b) for list[1,2,3] for list[3,2,5] if a != b]
- **combs = [(a,b) for a in [1,2,3] for b in [3,2,5] if a != b]**
- combs = [[a,b] in a for [1,2,3] in b for [3,2,5] if a = b]

### 正解

**combs = [(a,b) for a in [1,2,3] for b in [3,2,5] if a != b]**

### サルでもわかる解説

「a を [1,2,3]、b を [3,2,5] で回して、a≠b のとき (a,b) を入れる」がそのままの形。for a in ... for b in ... の順と if a != b を付ける形です。[a,b] だとリストになり、(a,b) がタプル。a=b は代入なので比較には使えず、a!=b が正しいです。

---

## 問21. リストの append / sort / insert / pop

次のコードの実行結果として正しいものはどれか。

```python
list = [-10, 1, 15, 20, 30]
list.append(50)
list.sort(reverse = True)
list.insert(2,5)
list.pop(-1)
print(list)
```

- [50, 2, 30, 20, 15, 1]
- [50, 30, 20, 15, 1, -10]
- **[50, 30, 5, 20, 15, 1]**
- [-10, 1, 5, 15, 20, 30]
- [30, 20, 15, 5, 1, -10]

### 正解

**[50, 30, 5, 20, 15, 1]**

### サルでもわかる解説

初期: [-10, 1, 15, 20, 30]。append(50)→[-10, 1, 15, 20, 30, 50]。sort(reverse=True)→[50, 30, 20, 15, 1, -10]。insert(2,5)→[50, 30, **5**, 20, 15, 1, -10]。pop(-1)→最後を削除→[50, 30, 5, 20, 15, 1]。※組み込み名 list を変数名に使うのは避けましょう。

---

## 問22. スライス Zen[0:20:3]

次のコードの実行結果として正しいものはどれか。

```python
Zen = 'FlatIsBetterThanNested'
print(Zen[0:20:3])
```

- FItTNe
- tBtTns
- FtBtTnsd
- **FtBtTns**
- FItTN

### 正解

**FtBtTns**（0, 3, 6, 9, 12, 15, 18 番目の文字を連結したもの）

### サルでもわかる解説

[始まり:終わり:ステップ] で、終わりは含まない。0, 3, 6, 9, 12, 15, 18 番目を連結した文字列が結果です。実際に手で数えるか、対話モードで Zen[0:20:3] を実行すると確実です。

---

## 問23. データ構造

データ構造に関する次の記述のうち**正しい**ものはどれか。

- ディクショナリに対する帰属性判定演算子「in」「not in」による判定において、「含まれるかどうか」の判定の対象は「キー」ではなく「値」である。
- 「set = {}」において{}は空集合を生成する式であり、{}は空辞書を生成することはできない。
- リストとタプルは変更可能（mutable）、集合は変更不能（immutable）である。
- ディクショナリは変更不能（immutable）であるが、キーの型は変更可能（mutable）であり、その値は一意でなければならない。
- **リストとタプルは順序を持つ要素の集まりであるという共通点がある。**

### 正解

**「リストとタプルは順序を持つ要素の集まりであるという共通点がある。」**

### サルでもわかる解説

in / not in の対象は**キー**（値ではない）。{} は**空の辞書**。空集合は set() で作る。タプルはイミュータブル。集合（set）はミュータブル。辞書はミュータブル。キーはイミュータブルでないとダメな場合が多い。リストもタプルも「何番目が何」が決まっている＝順序あり、という説明が正しいです。

---

## 問24. 対話モードで True が返るもの

対話モードで入力したときに「**True**」が返されるものは次のうちどれか。

- (-1, -10, -3, -4) > (-1, -2, -5)
- **1 > -1 == (1-2)**
- (1, 2) > (1, 2, -1)
- 'Matplotlib' > 'NumPy' > 'pandas' > 'scikit-learn'
- ('bb', 'c') > ('bcd', 'a')

### 正解

**1 > -1 == (1-2)**

### サルでもわかる解説

比較が連鎖すると、隣同士が両方 True のときだけ全体が True になる。**1 > -1**→True。**(1-2)=-1** なので **-1 == (1-2)**→True。だから **1 > -1 == (1-2)** は True and True で **True** です。

---

## 問25. モジュール

モジュールに関する次の記述のうち、**誤っている**ものはどれか。

- パッケージとは、「ドット区切モジュール名」を使って、Pythonのモジュールを構築する方法である。
- あるモジュールがインポートされるときにインタープリタが検索する順序は、まずビルトインモジュール、次にsys.path変数で得られるディレクトリである。シンボリックリンクを置いてあるディレクトリはモジュール検索パスに入らない。
- **sys.pathが初期化されている場所は、入力スクリプトのあるディレクトリ、PYTHONPATHであり、インストールごとのデフォルトは含まれない。**
- Pythonはソースファイルの最終更新日時をコンパイル済みのバージョンと比較し、再コンパイルが必要か判断する。これは完全に自動的に行われる。
- コンパイル済みのモジュールはプラットフォーム非依存なので、ひとつのライブラリを異なるアーキテクチャのシステム間で共有できる。

### 正解

**「sys.pathが初期化されている場所は、入力スクリプトのあるディレクトリ、PYTHONPATHであり、インストールごとのデフォルトは含まれない。」** が誤り。

### サルでもわかる解説

sys.path には、インストール時に決まるデフォルトのディレクトリも含まれます。なので「デフォルトは含まれない」という部分が誤りです。

---

## 問26. モジュールの名前を確認（【A】）

モジュールが定義している名前を対話モードで確認したい。次のコードの２行目【A】に入るものとして正しいものはどれか。

```python
import sys
【A】
```

- mod(systems)
- mod(sys)
- mod()
- dir(mod)
- **dir(sys)**

### 正解

**dir(sys)**

### サルでもわかる解説

dir(オブジェクト) で、そのオブジェクトが持っている名前（属性・メソッドなど）のリストが得られます。mod() や mod(sys) のような関数は標準にはありません。だから【A】= dir(sys) が正解です。

---

## 問27. format と math

次のコードの実行結果として正しいものはどれか。

```python
import math
print('{1:.5f}, {0:.3f}'.format(math.pi, math.e))
```

- 3.142, 2.71828
- 3.14159, 2.718
- **2.71828, 3.142**
- 2.718, 3.14159
- 1:3.14159f, 0:2.718f

### 正解

**2.71828, 3.142**

### サルでもわかる解説

format(math.pi, math.e) では {0}=pi、{1}=e。'{1:.5f}, {0:.3f}' は「1番目を小数点5桁、0番目を小数点3桁」なので、e を .5f、pi を .3f。つまり 2.71828, 3.142 の順で表示されます。

---

## 問28. 例外処理（整数 a=3, b=0）

次のコードを実行して「整数a:」に「3」、「整数b:」に「0」を入力した場合の正しい結果はどれか。なお選択肢中の「, 」は改行に読み替えること。

```python
try:
    int_a = int(input('整数a:'))
    int_b = int(input('整数b:'))
    print(int_a ** 3)
    print((int_a ** 3) / int_b)
except(ZeroDivisionError):
    print('C')
except(ValueError) as v:
    print(type(v))
    print('D')
except:
    print('E')
else:
    print('F')
finally:
    print('G')
```

- 27, 0, C, E, F, G
- 27, 0, C, F, G
- 27, C, E, F, G
- 27, F, G
- **27, C, G**

### 正解

**27, C, G**

### サルでもわかる解説

print(int_a ** 3) で 27 を表示。print((int_a**3)/int_b) で 27/0 となり ZeroDivisionError。except ZeroDivisionError で 'C' を表示。finally で 'G' を表示。else は例外が起きなかったときだけなので、ここでは実行されません。

---

## 問29. エラーと例外

エラーと例外に関する次の記述のうち**誤っている**ものはどれか。

- raise文を用いることで、指定の例外を意図的に発生させることができる。raiseの引数は送出する例外を示すものであり、例外インスタンスでも、Exceptionクラスの派生クラスであるクラス（例外クラス）でも構わない。
- 発生した例外に値が付随することもあり、これを例外の引数と呼ぶ。except 節では、例外名の後に変数を指定することができる。この変数は例外インスタンスに結び付けられており、instance.args に例外インスタンス生成時の引数が格納される。
- **[Ctrl]+[C]キーなどでユーザーがプログラムに割り込みをかけると、KeyError例外が送出される。**
- パーサ（構文解釈器）は違反のある行を表示し、最初にエラーが検知された点を小さな矢印で示す。エラーは矢印より前のトークンが原因である。
- 例外のほとんどはプログラムでは処理されず、その結果はエラーメッセージにあらわれる。エラーメッセージの最終行には、NameError、TypeErrorなど例外の型が記されている。

### 正解

**「[Ctrl]+[C]キーなどでユーザーがプログラムに割り込みをかけると、KeyError例外が送出される。」** が誤り。

### サルでもわかる解説

キーボード割り込みで送出されるのは **KeyboardInterrupt** です。KeyError は「辞書に存在しないキーを参照したとき」の例外。名前が似ているので混同しないように。

---

## 問30. with 文とクリーンアップ

次のコードを実行した場合には適切な方法で、あるクリーンアップがなされる。具体的にはどのような処理がなされているか。

```python
with open("file.txt") as f:
    for line in f:
        print(line, end="")
```

- close("file.txt")
- file.close()
- file.clean()
- **f.close()**
- f.clean()

### 正解

**f.close()**

### サルでもわかる解説

with 文では、ブロックを抜けるときに**ファイルオブジェクト f の close()** が自動で呼ばれます。だから「適切なクリーンアップ」＝**f.close()** が正解です。

---

## 問31. 例外の流れ（【A】【B】【C】【D】）

次の実行結果を得たい場合、コードの【A】【B】【C】【D】に入る組み合わせとして適切なものはどれか。

**[実行結果]**

```
David is a
strategic
AI
```

**[コード]**（raise_his_character で print(a, '【B】') のあと raise wexal、except wexal で print('【A】')、raise Exception、except Exception で print('【D】')）

- **【A】strategic 【B】is a 【C】naughty boy 【D】AI**
- 【A】is a 【B】strategic 【C】naughty boy 【D】AI
- 【A】strategic 【B】is a 【C】AI 【D】naughty boy
- 【A】naughty boy 【B】is a 【C】strategic 【D】AI
- 【A】AI 【B】strategic 【C】is a 【D】naughty boy

### 正解

**【A】strategic 【B】is a 【C】naughty boy 【D】AI**

### サルでもわかる解説

func(name) で name='David'≠0 なので raise_his_character('David') が呼ばれる。print('David', '【B】') で【B】='is a'。raise wexal。except wexal で print('【A】') で【A】='strategic'、raise Exception。except Exception で print('【D】') で【D】='AI'。【C】は raise の後の print なので実行されない（naughty boy は出ない）。出力順は「David is a」→「strategic」→「AI」です。

---

## 問32. local / nonlocal / global

次のコードの実行結果として正しいものはどれか。なお各選択肢内は改行されているものとして読み替えること。

```python
def scope():
    loc = "init"
    def do_local():
        loc = "local"
    def do_nonlocal():
        nonlocal loc
        loc = "nonlocal"
    def do_global():
        global loc
        loc = "global"

    do_local()
    print("A:", loc)
    do_nonlocal()
    print("B:", loc)
    do_global()
    print("C:", loc)

scope()
print("D:", loc)
```

- A: init　B: local　C: nonlocal　D: global
- A: init　B: nonlocal　C: nonlocal　D: global
- A: init　B: local　C: global　D: global
- **A: init　B: nonlocal　C: global　D: global**
- A: local　B: nonlocal　C: nonlocal　D: global

### 正解

**A: init　B: nonlocal　C: global　D: global**

### サルでもわかる解説

do_local() の loc="local" は関数内の新しい変数なので、外の loc は変わらない→A: init。do_nonlocal() の nonlocal loc は「ひとつ外の scope の loc」を書き換える→B: nonlocal。do_global() の global loc は「モジュールの loc」を "global" に変える→C: global。最後の print("D:", loc) はモジュールの loc を参照→D: global。

---

## 問33. クラス継承（【A】【B】【C】）

次の実行結果を得たい場合、コードの【A】【B】の行および【C】に入る組み合わせとして適切なものはどれか。なお【A】は★aの行と、【B】は★bの行と同じ数の空白でインデントされている。

**[実行結果]**

```
Need Speed?
I'm Saya.
Need Speed?
I'm David.
```

**[コード]**（kusanagi の s() で "Need Speed?" と【A】、wexal が【B】で "I'm David."、w.【C】で上記出力）

- **【A】self.m() 【B】m(self): 【C】s()**
- 【A】self.m() 【B】self(m): 【C】s()
- 【A】self(m) 【B】m(self): 【C】s()
- 【A】self(m) 【B】self(m): 【C】s(self)
- 【A】self.s() 【B】m(self): 【C】s(self)

### 正解

**【A】self.m() 【B】m(self): 【C】s()**

### サルでもわかる解説

kusanagi の s() で「Need Speed?」と self.m()。wexal は kusanagi を継承し、m(self): をオーバーライドして「I'm David.」を表示。w.s() は親の s() が呼ばれ、「Need Speed?」→self.m() で wexal の m()→「I'm David.」。だから【A】= self.m()、【B】= m(self):、【C】= s() が正解です。

---

## 問34. sys.argv

コマンドライン上で「python3 script.py one two three four five」を実行したときに、以下の結果を得たい。コード２行目の【A】に入るものとして正しいものはどれか。

**[実行結果]**  
['script.py', 'one', 'two']

**[script.pyのコード]**

```python
import sys
print(【A】)
```

- sys.argv[0:2]
- **sys.argv[0:3]**
- sys.argv[1:3]
- sys.args[1:3]
- sys.args[1:4]

### 正解

**sys.argv[0:3]**

### サルでもわかる解説

sys.argv に [0]=script.py, [1]=one, [2]=two, ... が入ります。[0:3] でインデックス 0, 1, 2 → 'script.py', 'one', 'two' が得られます。sys.args は存在しないので×。

---

## 問35. 正規表現でエラーになるもの

次の正規表現を用いたコードの【A】の部分に入れたとき**エラーとなる**ものはどれか。

```python
import re
prog = re.compile('(K|S)u(r|s)(a|o)nf?(a|o)(o|m)?g?i?(saya)?', re.IGNORECASE)
【A】
print(ret[0])
```

- ret = prog.search('KUSANAGI')
- ret = prog.search('Kuronami')
- **ret = prog.search('kurofune')**
- ret = prog.search('SUSANOO')
- ret = prog.search('kusanomi')

### 正解

**ret = prog.search('kurofune')**（マッチしないので ret が None、ret[0] でエラー）

### サルでもわかる解説

re.search がマッチしないと **None** を返します。None[0] は TypeError（または AttributeError）になります。正規表現に合わない文字列を選べばよいです。「kurofune」はパターンと合わないので ret が None になり、ret[0] でエラーになります。

---

## 問36. random モジュール（【A】【B】【C】）

対話モードで random モジュールを用い以下のような各結果を得たい場合、各コード【A】～【C】に入る正しい組み合わせはどれか。

```
>>> import random
>>> random.【A】(['apple', 'pear', 'banana'])
'apple'
>>> random.【B】(range(10), 3)
[3, 7, 5]
>>> random.【C】(5)
4
```

- 【A】choice 【B】random 【C】rand
- 【A】choice 【B】sample 【C】rand
- **【A】choice 【B】sample 【C】randrange**
- 【A】sample 【B】choice 【C】rand
- 【A】sample 【B】random 【C】randrange

### 正解

**【A】choice 【B】sample 【C】randrange**

### サルでもわかる解説

random.choice(リスト)→要素を**1つ**ランダムに返す。random.sample(範囲, 個数)→重複なしで**複数個**取り出す。random.randrange(終わり)→0以上終わり未満の**整数**を1つ返す。だから【A】= choice、【B】= sample、【C】= randrange が正解です。

---

## 問37. 今日の日付（datetime）

今日の日付を次の実行結果のように得たい場合、コードの1行目【A】と2行目の【B】に入る適切なものはどれか。

**[実行結果]**  
2020-06-27

**[コード]**

```python
【A】
now = 【B】
print(now)
```

- 【A】import date 【B】datetime.date(today)
- 【A】from date 【B】datetime.today()
- 【A】import datetime from date 【B】datetime.today()
- **【A】from datetime import date 【B】date.today()**
- 【A】import date from datetime 【B】datetime.today()

### 正解

**【A】from datetime import date 【B】date.today()**

### サルでもわかる解説

from datetime import date で date クラスだけをインポート。date.today() で今日の日付オブジェクトを得て、print(now) で YYYY-MM-DD 形式で表示されます。import datetime の場合は datetime.date.today() と書きます。

---

## 問38. logging の優先度

loggingモジュールのメッセージの優先度として正しいものはどれか。**左から順に優先度が低い**ものとする。

- **DEBUG、INFO、WARNING、ERROR、CRITICAL**
- INFO、DEBUG、WARNING、ERROR、CRITICAL
- DEBUG、INFO、ERROR、WARNING、CRITICAL
- INFO、DEBUG、ERROR、CRITICAL、WARNING
- DEBUG、INFO、CRITICAL、ERROR、WARNING

### 正解

**DEBUG、INFO、WARNING、ERROR、CRITICAL**

### サルでもわかる解説

左から右に優先度が**低い**→**高い**の順です。DEBUG &lt; INFO &lt; WARNING &lt; ERROR &lt; CRITICAL です。

---

## 問39. pip

仮想環境とパッケージに関する次の記述のうち**誤っている**ものはどれか。

- pip install でパッケージ名を指定し、そのパッケージ名の後ろに==とバージョン名を付けると、そのバージョンのパッケージをインストールできる。
- pip install --upgrade とすることで、当該パッケージを最新バージョンにアップグレードすることができる。
- **「pip list パッケージ名」で、ある特定のパッケージの詳細情報が表示される。**
- pip uninstall にパッケージ名を指定すると、その仮想環境からパッケージを削除できる。削除対象となるパッケージの複数指定も可能である。
- pip freeze はその仮想環境にインストールされたすべてのパッケージを、pip install 向けの形式で出力する。

### 正解

**「pip list パッケージ名」で、ある特定のパッケージの詳細情報が表示される。** が誤り。

### サルでもわかる解説

pip list は「インストール済みパッケージの一覧」で、**引数にパッケージ名は取りません**。特定パッケージの**詳細**を見るのは **pip show パッケージ名** です。pip install ==、--upgrade、uninstall、freeze の説明は正しいです。

---

## 問40. 対話環境の補完

次の記述に関して**誤っている**ものはどれか。

- デフォルト設定ではユーザーディレクトリの「.python_history」ファイルにヒストリが保存される。ヒストリは対話型インタープリタセッションで利用できる。
- [Tab]キーを押すと補完機能が呼び出せる。この機能はPythonの文（命令）の名前、現在のローカル変数、使用できるモジュール名を検索するものである。
- 拡張された対話型インタープリタとして bpython がある。これはタブ補完、オブジェクト探索、高度なヒストリ管理などの機能を持つ。
- bpython に類似した拡張対話環境に IPython がある。IPython は「pip install ipython」でインストールでき、IPython の対話モードは ipython コマンドで起動できる。
- **変数とモジュールの補完機能は、インタープリタの起動時には有効になっていないため設定が必要である。**

### 正解

**「変数とモジュールの補完機能は、インタープリタの起動時には有効になっていないため設定が必要である。」** が誤り。

### サルでもわかる解説

標準の対話型インタープリタでも、Tab 補完（変数・モジュール名など）は**特に設定しなくても使える**ことが多いです。「起動時には有効になっていない」「設定が必要」という説明が誤りとされます。.python_history、Tab の補完、bpython、IPython の説明は正しいです。

---

## このドキュメントの使い方

- 各問の **正解** と **サルでもわかる解説** を読んで、なぜその答えになるかを理解しましょう。
- コードは実際に手元で実行して挙動を確認すると、より覚えやすくなります。
- 間違えた問題は、解説を読み直してからもう一度解き直すと効果的です。
