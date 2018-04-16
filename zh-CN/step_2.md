## 随机颜色



+ 打开这个 trinket：<a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>。 

+ 你可以通过表明你想要的红色、绿色和蓝色色值（在 0 到 255 之间选择）来设置海龟的颜色。 

    添加以下代码来获得一只紫色海龟：

    ![screenshot](images/modern-purple.png)
   
    紫色是通过混合红色和蓝色而得出的。

+ 尝试一些不同的数值来得到不同的颜色。 

    请记得每个数值都在 0 到 255 之间。 

+ 选择一个随机颜色怎么样呢？

    更新你的代码来选择一个 0 到 255 之间的随机数值作为红色、绿色和蓝色色值：
    
    ![screenshot](images/modern-random-colour.png)

+ 多次点击“运行”来获取不同颜色的海龟。

+ 这很有意思，但每次你想将海龟设置成一个随机颜色，都需要记住并输入许多数值，而且不容易读取。 

    在 Python 中，我们可以编写 `def` 来定义一个函数，我们可以在每次需要将海龟设为随机颜色时调用此函数。 

    你已经调用了函数，`color()`（颜色）和 `randint()`（随机整数）是已经为你定义的函数。 

    让我们使用 def 将随机颜色代码放在函数中：
  
    ![screenshot](images/modern-colour-function.png)
    
  请确保你将代码缩进在函数内部。函数通常位于导入之后的脚本顶部。 
  
+ 如果你现在“运行”你的代码，你不会得到一只随机颜色的海龟。这是因为你定义了你的函数，但还未调用它。 
  
+ 添加一行来调用你的新函数：
  
    ![screenshot](images/modern-call-colour.png)

    请注意由于复杂的部分在函数中，因此你的新代码更易于理解。很容易就能弄清楚 `randomcolour()`（随机颜色）的作用。

