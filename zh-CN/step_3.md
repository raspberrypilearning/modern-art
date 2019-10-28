## 随机位置

让我们创建另一个函数，将海龟移动到屏幕上的随机位置。 屏幕的中心是(0,0)，因此我们将海龟放置在围绕中心的正方形区域中。

+ 添加`randomplace()`函数：
    
    ![screenshot](images/modern-place-function.png)

+ 通过调用来尝试你的新函数，然后调用 `stamp()`，你可以多次调用它：
    
    ![screenshot](images/modern-call-place.png)

+ Ooops, the turtle draws when it moves. Let’s put the pen up at the beginning and down at the end so that the turtle doesn’t draw while it’s moving:
    
    ![screenshot](images/modern-place-pen.png)
    
    Did you notice that you only had to 'fix' the code in one place? That's another good thing about functions.

+ Now test your code a few times.