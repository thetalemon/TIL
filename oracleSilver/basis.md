## 基本

### ソースで宣言するもの
 - インポート宣言
 - パッケージ宣言

### クラスで宣言するもの
 - フィールド
 - メソッド
 - コンストラクタ（メソッドの一種）

### パッケージの役割
 - 名前空間の提供
 - アクセス制御の提供
 - クラスの分類を可能にする

##### たとえば…
 - src/sample1/main/main.class
 - src/sample1/main/db.class
 - src/sample2/main/main.class
 - src/sampme2/main/db.class
 <br><br>
 -  上記４つがあったとして、２つのdb.classに同名のメソッドがあっても、明示的なインポートをしない限りは、sample1のmain.classからsample2のdb.classのメソッドが参照されることはない。


### 自動インポートされるもの
  - java.langのクラス（C言語でいうstdio.hのようなもの）
  - 同じパッケージのクラス

### 無名パッケージについて
 - 無名パッケージは無形パッケージ同士でしかインポートできない
  - ので、できるだけ使用しないのがおすすめ

### package,import文について
 - package文の上にはコメントしかこない
 - メソッドをimportするときは()は不要
  - オーバロード系も一緒にインポートしてくれる

```
package sample1;
import java.io.*;
import static sample1.sampleValue;
import static sample1.sampleMethod;
```
