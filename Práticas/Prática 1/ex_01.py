'''
𝐿4 = {𝑏𝑎𝑛𝑏𝑎 ∣ 𝑛 ≥ 0}
'''

from AFD import AFD

Q = ['q0', 'q1', 'q2', 'q3', 'trap']
Sigma = ['a', 'b']
delta = {
    ('q0', 'a'): 'trap',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'trap',
    ('q3', 'a'): 'trap',
    ('q3', 'b'): 'trap',
    ('trap', 'a'): 'trap',
    ('trap', 'b'): 'trap'
}
F = ['q3']

testes = [
    "bba",
    "ababa",
    "baaaaaaaaba",
    "baaaaaaaabaaaaa"
    "baaaaaaaabb"
]

for teste in testes:
    saida = AFD((Q, Sigma, delta, 'q0', F), teste)

    print(f"{teste} - {saida}")
