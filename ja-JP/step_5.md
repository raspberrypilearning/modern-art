## 四角形のモダンアートを作る。

さあ、いろんなサイズと色の四角形をたくさん描いてモダンアートを作ってみましょう。

+ 最初に、次のコードをあなたのスクリプトの下に追加し、あなたがカメのアートのコードを試した後に画面をクリアし、通常の方向にカメを向ける様にして下さい。
    
    ![スクリーンショット](images/modern-reset.png)

+ カメのアートコードのそれぞれの行の先頭に`#`を置いてコメントアウトすると、四角形のモダンアートの作業をしている間、実行しないようすることができます。 （そうすれば、後でコメントを外してすべての作業を表示することができます。）
    
    ![スクリーンショット](images/modern-comment.png)

+ では、ランダムな大きさで、ランダムな色の四角形をランダムな場所に描く関数を追加しましょう！
    
    あなたの他の関数の後に、`drawrectangle()` 関数を追加して下さい。
    
    ![スクリーンショット](images/modern-rect-function.png)
    
    入力する時間を節約したい場合は、`snippets.py `のヘルパーコードを調べてください。

+ `main.py `の最後に次のコードを追加して、あなたの新しい関数を呼び出します。
    
    ![スクリーンショット](images/modern-call-rect.png)
    
    スクリプトを何回か実行して、高さと幅の違いを見てみましょう。

+ その長方形は常に同じ色で、同じ場所から始まりますね。
    
    今度は、カメをランダムな色に設定して、それをランダムな場所に移動する必要があります。 ねえ、あなたはすでにそれを行うための関数を作りませんでしたか？ すばらしい！ drawrectangle関数の最初から、それを呼び出すだけですみます。
    
    ![スクリーンショット](images/modern-random-rect.png)
    
    うわー、それははるかに少ない作業で、読むのがずっと簡単ですね。

+ 次に、ループの中で`drawrectangle()`を呼び出して、いくつかのクールなモダンアートを作ってみましょう。
    
    ![スクリーンショット](images/modern-rect-art.png)

+ おやまあ、これはちょっと遅くなかったですか！ ラッキーなことに、あなたはカメのスピードを上げることができます。
    
    ラッキーなことに、あなたはカメのスピードを上げることができます。
    
    ![スクリーンショット](images/modern-speed.png)
    
    `speed(0)`が最も速く、または1（遅い）から10（速い）までの数字を使用できます。 あなたが好きなスピードを見つけるまで試してみてください。