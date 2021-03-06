## 무작위 위치

이번에는 거북이를 화면의 무작위 위치로 이동시키는 함수를 만들어 보겠습니다. 화면 중심의 좌표는 (0,0) 입니다. 따라서 우리는 화면 중심을 기준으로 둘러싸는 사각형 영역에 거북이를 위치시킬 것입니다.

+ `randomplace()` 함수를 추가하세요:
    
    ![스크린샷](images/modern-place-function.png)

+ 우리가 만든 함수를 호출해서 사용해보고 이어서 `stamp()`를 호출해보세요. 여러 번 호출해도 됩니다:
    
    ![스크린샷](images/modern-call-place.png)

+ 이런, 거북이가 움직일때 선이 그려지네요. 거북이가 움직이기 시작할 때는 펜을 들고, 끝나면 펜을 내리도록 해서 선이 그려지지 않게 해보세요:
    
    ![스크린샷](images/modern-place-pen.png)
    
    우리가 코드에서 하나의 부분만 수정했다는 것을 눈치챘나요? 이것이 함수의 또다른 장점입니다.

+ 이제 우리의 코드를 테스트해보세요.