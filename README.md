# Python 課題 <!-- omit in toc -->

- [最初にすること](#最初にすること)
  - [1. リポジトリをクローンする](#1-リポジトリをクローンする)
  - [2. リポジトリの設定をする](#2-リポジトリの設定をする)
  - [3. 提出用ブランチを作成する](#3-提出用ブランチを作成する)
- [解答の作成・提出方法](#解答の作成提出方法)
  - [1. 課題の解答を作成する](#1-課題の解答を作成する)
  - [2. 変更したファイルをコミットする](#2-変更したファイルをコミットする)
  - [3. 変更をプッシュする](#3-変更をプッシュする)
- [アップデート方法](#アップデート方法)

## 最初にすること

### 1. リポジトリをクローンする

任意のディレクトリで以下のコマンドを実行する。

```sh
git clone https://github.com/wasedatakeuchilab/python-assignment
cd python-assignment
```

### 2. リポジトリの設定をする

```sh
# ダブルクォーテーションの部分は自身のものに置き換える
git config user.name "Shuhei Nitta"
git config user.email "nittashuhei99@toki.waseda.jp"
git config pull.rebase true
```

### 3. 提出用ブランチを作成する

各個人が作成したファイルを提出するために使用するブランチを`submit/{year}/{family_name}`という名前で作成する。

```sh
# 実行コマンドの例
git switch -c submit/2024/Nitta
```

## 解答の作成・提出方法

### 1. 課題の解答を作成する

`assignments`以下の各ディレクトリに課題が記された`README.md`があるので、
それを満たすようなコードを同ディレクトリの`main.py`に記入する。

### 2. 変更したファイルをコミットする

以下のコマンドを入力して作成した解答をコミットする。

```sh
git add path/to/main.py  # path/toの部分は実際のパスに置き換える
git commit -m "Update main.py"
```

ex.

```sh
git add assignments/example/main.py
git commit -m "Update main.py"
```

### 3. 変更をプッシュする

以下のコマンドを実行して、変更をリモートリポジトリ（今回は GitHub）へ反映する。

```sh
git push origin HEAD -f
```

プッシュすると自動的に解答コードがテストされる。
この作業を持って提出完了とする。

> `-f`オプションをつけたフォースプッシュは共同作業者のローカルブランチを破壊しうるため本来してはいけないが、
> 今回は各個人でブランチを分けて作業するので良しとする。

## アップデート方法

新しい課題が追加された時などにはリポジトリを更新する必要がある。
以下のコマンドで更新できる。

```sh
git pull origin master
```
