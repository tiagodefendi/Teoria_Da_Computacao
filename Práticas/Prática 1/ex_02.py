'''
𝐿5 = {𝑥 ∈ {𝑎, 𝑏}∗ ∣ |𝑥| mod 3 = 0}
'''

from AFD import AFD

Q = ['q0', 'q1', 'q2']
Sigma = ['a', 'b']
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q0',
    ('q2', 'b'): 'q0',
}
F = ['q0']

testes = [
    "bba",
    "ababa",
    "baabab",
    "ababab"
]

for teste in testes:
    saida = AFD((Q, Sigma, delta, 'q0', F), teste)

    print(f"{teste} - {saida}")
