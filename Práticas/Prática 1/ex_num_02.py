'''
Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
𝐿8 = {𝑥 ∈ Σ∗ ∣ 𝑥 mod 5 = 0}
'''

from AFD import AFD

Q = ['q0', 'q1', 'trap']
Sigma = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
delta = {
    ('q0', '0'): 'q1',
    ('q0', '5'): 'q1',
    ('q0', '2'): 'trap',
    ('q0', '4'): 'trap',
    ('q0', '6'): 'trap',
    ('q0', '8'): 'trap',
    ('q0', '1'): 'trap',
    ('q0', '3'): 'trap',
    ('q0', '7'): 'trap',
    ('q0', '9'): 'trap',

    ('q1', '0'): 'q1',
    ('q1', '5'): 'q1',
    ('q1', '2'): 'trap',
    ('q1', '4'): 'trap',
    ('q1', '6'): 'trap',
    ('q1', '8'): 'trap',
    ('q1', '1'): 'trap',
    ('q1', '3'): 'trap',
    ('q1', '7'): 'trap',
    ('q1', '9'): 'trap',

    ('trap', '0'): 'q1',
    ('trap', '5'): 'q1',
    ('trap', '2'): 'trap',
    ('trap', '4'): 'trap',
    ('trap', '6'): 'trap',
    ('trap', '8'): 'trap',
    ('trap', '1'): 'trap',
    ('trap', '3'): 'trap',
    ('trap', '7'): 'trap',
    ('trap', '9'): 'trap',
}
F = ['q1']

testes = [
    "1",
    "5",
    "20",
    "35",
    "38",
    "353",
    "222",
]

for teste in testes:
    saida = AFD((Q, Sigma, delta, 'q0', F), teste)

    print(f"{teste} - {saida}")
