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
git config user.name "Taro Waseda"
git config user.email "tarowaseda@waseda.jp"
git config pull.rebase false
```

### 3. 提出用ブランチを作成する

各個人が作成したファイルを提出するために使用するブランチを`submit/{year}/{grade}-{family_name}`という名前で作成する。

```sh
git switch -c submit/2024/B4-Waseda
```

## 解答の作成・提出方法

### 1. 課題の解答を作成する

`assignments`以下の各ディレクトリに課題が記された`README.md`があるので、
それを満たすようなコードを同ディレクトリの`main.py`に記入する。

### 2. 変更したファイルをコミットする

解答を書いた`main.py`をステージして変更をコミットする。

```sh
# コマンド例： assignments/exampleを解いた場合
git add assignments/example/main.py
git commit -m "Solve example"
```

### 3. 変更をプッシュする

以下のコマンドを実行して、変更をリモートリポジトリ（今回は GitHub）へ反映する。

```sh
git push origin HEAD
```

プッシュすると自動的に解答コードがテストされる。
この作業を持って提出完了とする。

## アップデート方法

新しい課題が追加された時などにはリポジトリを更新する必要がある。
以下のコマンドで更新できる。

```sh
git pull origin master
```
