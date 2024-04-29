*** Settings ***
Library    OperatingSystem
Library    Calculator.py

*** Test Cases ***
Testar Soma de Dois Números
    ${resultado}    add    ${2}    ${3}
    Should Be Equal As Numbers    ${resultado}    5

Testar Soma com Números Negativos
    ${resultado}    add    ${-2}    ${3}
    Should Be Equal As Numbers    ${resultado}    1

Testar Subtação com Números Positivos
    ${resultado}    subtract    ${5}    ${3}
    Should Be Equal As Numbers    ${resultado}    2

Testar Subtação com Números Negativos
    ${resultado}    subtract    ${-1}    ${-3}
    Should Be Equal As Numbers    ${resultado}    2

Testar Multiplicação
    ${resultado}    multiply    ${-3}    ${6}
    Should Be Equal As Numbers    ${resultado}    -18
    ${resultado}    multiply    ${3}    ${6}
    Should Be Equal As Numbers    ${resultado}    18
    ${resultado}    multiply    ${-3}    ${-6}
    Should Be Equal As Numbers    ${resultado}    18

Testar Divisão
    ${resultado}    divide    ${18}    ${6}
    Should Be Equal As Numbers    ${resultado}    3
    ${resultado}    divide    ${-18}    ${6}
    Should Be Equal As Numbers    ${resultado}    -3
    ${resultado}    divide    ${-18}    ${-6}
    Should Be Equal As Numbers    ${resultado}    3

Testar Fatorial
    ${resultado}    factorial    ${12}
    Should Be Equal As Numbers    ${resultado}    479001600

Testar Seno
    ${resultado}    sin    ${0.5235987755982988}
    Should Be Equal As Numbers    ${resultado}    0.5

Testar Cosseno
    ${resultado}    cos    ${0.5235987755982988}
    Should Be Equal As Numbers    ${resultado}    0.866025

Testar Tangente
    ${resultado}    tan    ${0.5235987755982988}
    Should Be Equal As Numbers    ${resultado}    0.57735

Testar Graus para Radianos
    ${resultado}    degreesToRadians    ${30}
    Should Be Equal As Numbers    ${resultado}    0.5235987755982988

