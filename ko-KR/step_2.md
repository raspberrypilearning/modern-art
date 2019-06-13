## 무작위 색상

+ 다음 Trinket 파일을 열어주세요. <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ 당신은 0에서 255까지 빨강, 초록, 파랑의 양을 말함으로써 거북의 색깔을 설정할 수 있습니다.
    
    보라색 거북이를 만드려면 다음 코드를 추가하십시오.
    
    ![스크린샷](images/modern-purple.png)
    
    보라색은 빨간색과 파란색을 섞어서 만듭니다.

\--- collapse \---

* * *

## 제목: "오류 - 잘못된 색상 순서: (150, 0, 150)"

코드를 실행할 때 `색상 순서가 잘못되었습니다 (150, 0, 150)` 오류가 발생합니까?

Trinket은 다른 파이썬 편집기와 다른 색 모드를 사용하기 때문입니다. ` colormode `를 ` 255 `로 변경하여 수정할 수 있습니다.

```python
거북 가져 오기에서 *

colormode (255)

shape("turtle")
color(150,0,150)
```

\--- / collapse \---

+ 다른 색상을 사용하여 다른 숫자를 사용해보십시오.
    
    각 숫자는 0에서 255까지 가능하다는 것을 기억하십시오.

+ 컬러를 무작위로 선택하는 것은 어떻습니까?
    
    빨간색, 녹색 및 파란색 값에 대해 0에서 255 사이의 임의의 숫자를 선택하도록 코드를 업데이트하십시오.
    
    ![screenshot](images/modern-random-colour.png)

+ 다른 색상의 거북이를 얻으려면 '실행'을 몇 번 클릭하십시오.

+ That’s fun, but it’s a lot to remember and type every time you want to set a turtle to a random colour and it’s not very easy to read.
    
    In Python we can write `def` to define a function that we can call whenever we need to set the turtle to a random colour.
    
    You’ve been calling functions already, `color()` and `randint()` are functions that have been defined for you.
    
    Let’s put the random colour code into a function using def:
    
    ![screenshot](images/modern-colour-function.png)
    
    Make sure you indent the code inside the function. Functions are usually placed at the top of the script after the imports.

+ If you ‘Run’ your code now you don’t get a random coloured turtle. That’s because you have defined your function, but not called it yet.

+ Add a line to call your new function:
    
    ![screenshot](images/modern-call-colour.png)
    
    Notice that your new code is much easier to understand because the complex part is in the function. It’s easy to work out what `randomcolour()` does.