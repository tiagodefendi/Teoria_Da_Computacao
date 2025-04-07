'''
𝐿2 = {0𝑛1𝑚|𝑛 ≥ 0 ∧ 𝑚 ≥ 0}
'''

from AFD import AFD

Q = ['q0', 'q1', 'trap']
Sigma = ['0', '1']
delta = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q1',
    ('q1', '0'): 'trap',
    ('q1', '1'): 'q1',
    ('trap', '0'): 'trap',
    ('trap', '1'): 'trap'
}
F = ['q0', 'q1']

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
