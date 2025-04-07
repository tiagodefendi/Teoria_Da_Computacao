'''
𝐿7 = {𝑎𝑚𝑏𝑛 ∣ 𝑚, 𝑛 ≥ 0 ∧ (𝑚 + 𝑛) mod 2 = 0}
'''

from AFD import AFD

Q = ['q0', 'q1', 'q2', 'q3', 'trap']
Sigma = ['a', 'b']
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'trap',
    ('q2', 'b'): 'q3',
    ('q3', 'a'): 'trap',
    ('q3', 'b'): 'q2',
    ('trap', 'a'): 'trap',
    ('trap', 'b'): 'trap',
}
F = ['q0', 'q3']

testes = [
    "a",
    "aa",
    "bb",
    "ab",
    "ba",
    "abb",
    "aabb",
    "aaab",
    "babab"
]

for teste in testes:
    saida = AFD((Q, Sigma, delta, 'q0', F), teste)

    print(f"{teste} - {saida}")
