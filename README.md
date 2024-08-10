# ラベルなしグラフの数え上げ




## TODO：QIitaのリンクを貼る


## 必要な外部ライブラリ
matplotlib, sympy, networkx

いずれもpipからインストール可能


## python vs pypy

基本的にPyPyの方が速い。
steal.pyのみ多倍長の計算による影響が大きいせいかPythonの方が速い。


## 下界の実装
本実装では定義通り書いてるけど、メリットないかも。
- 実際の個数は整数値なので、切り上げた方がよりタイトな下界になる
- オーバーフローするので、大きな桁に対しては切り下げ除算にするのがいい

```python
def calc_lower_bound(n):
    return calc_upper_bound(n) / math.factorial(n)
```

