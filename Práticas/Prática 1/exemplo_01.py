'''
𝐿1 = {0𝑛1𝑚|𝑛 ≥ 1 ∧ 𝑚 ≥ 1}
'''

from AFD import AFD

Q = ['q0', 'q1', 'q2', 'trap']
Sigma = ['0', '1']
delta = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'trap',
    ('q1', '0'): 'q1',
    ('q1', '1'): 'q2',
    ('q2', '1'): 'q2',
    ('q2', '0'): 'trap',
    ('trap', '0'): 'trap',
    ('trap', '1'): 'trap'
}
F = ['q2']

testes = [
    "0000000011111111",
    "01",
    "0",
    "1",
    "100000",
    "0100",
]

for teste in testes:
    saida = AFD((Q, Sigma, delta, 'q0', F), teste)

    print(f"{teste} - {saida}")
