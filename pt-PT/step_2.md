## Cores aleatórias

+ Abre este trinket: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ Tu podes definir a cor de uma tartaruga dizendo quanto vermelho, verde e azul tu gostarias de 0 a 255.
    
    Adiciona o seguinte código para obter uma tartaruga roxa:
    
    ![captura de ecrã](images/modern-purple.png)
    
    O roxo é feito misturando vermelho e azul.

## \--- collapse \---

## title: "Erro - sequência de cores errada: (150, 0, 150)"

Tu recebes o erro ` sequência de cores errada: (150, 0, 150) ` ao executar o teu código.

Isto ocorre porque o trinket usa um modo de cor diferente para outros editores Python. Pode ser corrigido alterando o `colormode - modo de cor` para ` 255 `.

```python
from turtle import *

colormode(255)

shape("turtle")
color(150,0,150)
```

\--- /collapse \---

+ Tenta diferentes números para obter cores diferentes.
    
    Lembra-te de que cada número pode ser de 0 a 255.

+ Que tal escolher uma cor aleatória?
    
    Atualiza o teu código para escolher um número aleatório entre 0 e 255 para os valores vermelho, verde e azul:
    
    ![captura de ecrã](images/modern-random-colour.png)

+ Clica em "Executar" algumas vezes para obter diferentes tartarugas coloridas.

+ Isto é divertido, mas é muito para recordar e escrever todas as vezes que quiseres definir uma tartaruga para uma cor aleatória e não é muito fácil de ler.
    
    Em Python, podemos escrever ` def ` para definir uma função que podemos chamar sempre que precisarmos de definir a tartaruga para uma cor aleatória.
    
    Tu já estás a chamar funções, ` color () ` e ` randint () ` são funções que foram definidas para ti.
    
    Vamos colocar o código da cor aleatória numa função usando def:
    
    ![captura de ecrã](images/modern-colour-function.png)
    
    Certifica-te de indentar o código dentro da função. As funções geralmente são colocadas na parte superior do script após as importações.

+ Se tu 'Executares' o teu código agora não recebes nenhuma tartaruga de cor aleatória. Isso porque tu definiste a tua função, mas ainda não a chamaste.

+ Adicione uma linha para chamar a tua nova função:
    
    ![captura de ecrã](images/modern-call-colour.png)
    
    Observa que o teu novo código é muito mais fácil de entender porque a parte complexa está na função. É fácil descobrir o que ` corAleatoria() ` faz.