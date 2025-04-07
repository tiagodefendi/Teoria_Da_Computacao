'''
3. Obter um autômato finito que reconheça a linguagem L = {w ∈ {a, b}∗ | w contém uma
quantidade ímpar de símbolos a e uma quantidade múltipla de 3 de símbolos b}.
'''

from AFD import AFD

Q = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
Sigma = ['a', 'b']
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'q3',
    ('q3', 'a'): 'q4',
    ('q3', 'b'): 'q4',
    ('q4', 'a'): 'q5',
    ('q4', 'b'): 'q5',
    ('q5', 'a'): 'q0',
    ('q5', 'b'): 'q0',
}
F = ['q3']

testes = [
    "a",
    "ab",
    "",
    "aaa",
    "aab",
    "aabbba",
]

for teste in testes:
    saida = AFD((Q, Sigma, delta, 'q0', F), teste)

    print(f"{teste} - {saida}")
