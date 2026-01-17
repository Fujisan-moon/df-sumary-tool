#各モジュールのインポート及びドライブをマウント
import pandas as pd
from google.colab import drive
drive.mount("/content/drive")

#カーレントディレクトリのセット
cd "【自分の環境に合わせてパスをセット】"

#dfのセット(各変数は自分でセットしてください)
df_train =pd.read_csv("~~.csv")


"""
DFの最初5行、行列数、文字型、データ数、平均、中央値および四分位数とnull数をまとめて出力する関数
Jupter環境では最初5行と文字型、データ数、平均、中央値および四分位数とnull数はHTMLで表示さます
"""
def MLBasicInfo(df, *, use_display=True):

  if use_display:
    try:
      from IPython.display import display
    except Exception:
      use_display = False

  head = df.head()
  shape_row,shape_column  = df.shape
  dtypes = df.dtypes
  count = df.count()
  describe = df.describe(include="all")
  isnullsum = df.isnull().sum()

  def show(x):

    if use_display:
      display(x)
    else:
      print(x)

  print("■1, 最初の5行分のデータ")
  show(head)

  print("\n\n■2, 行列数")
  print(f"行数(データ数)…{shape_row}行")
  print(f"列数(カテゴリ数)…{shape_column}列")

  print("\n\n■3, dtypes情報")
  show(dtypes)

  print("\n\n■4, count情報")
  show(count)

  print("\n\n■5, describe情報")
  show(describe)
  print("\n\n■6, null数の情報")
  show(isnullsum)