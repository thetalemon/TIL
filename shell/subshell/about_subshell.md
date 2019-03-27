# 作成中


### サブシェルとreturnとexitについて

##### サブシェルとは
- $("command --hogehoge")
- シェル内で実行されるシェルのこと
- 変数なども引き継がれる

#### exit と return
- exitはその名の通り「シェルをexitする」
- returnは「実行結果をreturnする」
- exitは「サブシェルで呼ばれた場合は、サブシェルをexitする」が、普通に関数で呼ばれた場合は「シェルを　exitする」
 - subshell_exit.shを実行すると、`$(test_exit)`のあとは
 ```
 echo "resultcode:$?"
 echo "3"
 ```
