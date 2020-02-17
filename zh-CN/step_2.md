## 随机颜色

+ 打开此Trinket: <a href="https://trinket.io/python/5c2f5a25cf" target="_blank">trinket.io/python/5c2f5a25cf</a>。

+ 你可以通过表明你想要的红色、绿色和蓝色色值（在 0 到 255 之间选择）来设置海龟的颜色。
    
    添加以下代码来获得一只紫色海龟：
    
    ![截图](images/modern-purple.png)
    
    紫色是通过混合红色和蓝色而得到的。

--- collapse ---
---
title: "Error - bad color sequence: (150, 0, 150)"
---

当你运行代码时是否遇到`bad color sequence: (150, 0, 150)`这个错误。

这是因为Trinket使用了与其他Python编辑器不同的颜色模式。 可以通过更改`colormode`（颜色模式）至`255`解决这个问题 。

```python
from turtle import *

colormode(255)

shape("turtle")
color(150,0,150)
```

--- /collapse ---

+ 尝试一些不同的数字以获得不同的颜色。
    
    请记住，每个数字只能在0到255之间。

+ 如何选择随机颜色？
    
    修改你的代码，为红色，绿色和蓝色值选择一个介于0到255之间的随机数：
    
    ![截图](images/modern-random-colour.png)

+ 重复点击“Run”可以获得不同颜色的乌龟。

+ 这很有趣，但你每次想要为一只海龟设置随机颜色时，都要记住这段代码并重新输入，而且这样不便于阅读。
    
    在 Python 中，可以用 `def`来定义一个随机设置海龟颜色的函数，以便我们随时调用。
    
    你已经调用过函数，`color()`和`randint()`就是已为你定义好功能的函数。
    
    让我们把随机颜色的代码放入 def 定义的函数中：
    
    ![截图](images/modern-colour-function.png)
    
    请确保你在函数内缩进代码。 函数通常放在脚本的顶部，跟在imports后面。

+ 如果你现在点击“Run”运行你的代码却没有得到一个随机颜色的海龟。 那是因为你定义了函数，但尚未调用它。

+ 添加一行代码以调用新函数：
    
    ![截图](images/modern-call-colour.png)
    
    注意，新代码更容易理解，因为复杂的部分都在函数内。 现在就很容易理解`randomcolour()`做了什么。