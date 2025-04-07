'''
𝐿6 = {𝑤 ∈ {𝑎, 𝑏}∗ ∣ (|𝑤|𝑎 + |𝑤|𝑏) mod 2 = 0}
'''

from AFD import AFD

Q = ['q0', 'q1']
Sigma = ['a', 'b']
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q0',
}
F = ['q0']

testes = [
    "a",
    "ab",
    "ba",
    "bba",
    "ababa",
    "baabab",
    "ababab"
]

for teste in testes:
    saida = AFD((Q, Sigma, delta, 'q0', F), teste)

    print(f"{teste} - {saida}")
