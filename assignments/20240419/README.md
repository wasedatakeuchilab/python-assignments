# フィボナッチ数

整数 $n$ を引数で受け取り、第 $n$ 項のフィボナッチ数を返す関数`fibo()`を作成してください。
ただし、$n$ が負の場合は`ValueError`を送出してください。

フィボナッチ数は次のように定義されます。

$$
F_0 = 0, \; F_1 = 1 \\
F_n = F_{n-1} + F_{n-2} \quad \text{for} \; n > 1
$$

## 実行例 1

```python
>>> fibo(0)
0
>>> fibo(1)
1
>>> fibo(2)
1
>>> fibo(3)
2
```

## 実行例 2

```python
>>> fibo(-1)
ValueError: n must not be a negative number: -1
```

---

# Fibonacci Number

Create function `fibo()` that takes integer $n$ as a parameter and returns the $n \text{th}$ Fibonacci number.
If $n$ is negative, raise `ValueError`.

The Fibonacci numbers are defined as follows.

$$
F_0 = 0, \; F_1 = 1 \\
F_n = F_{n-1} + F_{n-2} \quad \text{for} \; n > 1
$$

## Execution Example 1

```python
>>> fibo(0)
0
>>> fibo(1)
1
>>> fibo(2)
1
>>> fibo(3)
2
```

## Execution Example 2

```python
>>> fibo(-1)
ValueError: n must not be a negative number: -1
```
