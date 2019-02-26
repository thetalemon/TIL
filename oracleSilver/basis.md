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

### エントリポイントについて
```
public static void main(string[] args){
  // some code
}
```
 - publicであること
 - staticであること
 - 返り値はvoidであること
 - メソッド名はmainであること
 - 引数は可変長のstringであること

### 数値型配列への×進数での代入に使用する接頭辞
 - 2進数:0b
 - 8進数:0
 - 16進数:0x

### 数値リテラルで使用するアンダースコアについて
 - 記号の前後は使用不可（0b,0x,L,F,.など）
 - アンダースコア連続はOK

### char型について
 - ''で囲われた文字のみが代入可能
 - ""で囲ってあるものは、文字列なので１文字でも不可
 - 数字では0~65535が代入できる
 - \u0000のように４桁までの16進数でも表記できる
