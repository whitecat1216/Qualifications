#[問題69]
import os
os.mkdir("test_dir")  # "test_dir"という名前の新しいディレクトリを作成する
print(os.path.isdir("test_dir"))  # True