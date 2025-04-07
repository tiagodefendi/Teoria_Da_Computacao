# Autômato Finito Determinístico

def AFD (M:tuple, cadeia:str) -> bool:
    '''
    Simulates the operation of a Deterministic Finite Automaton (DFA) on a given input string.
    Args:
        M (tuple): A tuple representing the DFA, where:
            - Q (set): A set of states.
            - Sigma (set): The alphabet (set of input symbols).
            - delta (dict): The transition function, represented as a dictionary where
                keys are tuples (current_state, input_symbol) and values are the next state.
            - q0 (any): The initial state.
            - F (set): A set of accepting (final) states.
        cadeia (str): The input string to be processed by the DFA.
    Returns:
        bool: True if the DFA ends in an accepting state after processing the input string,
                False otherwise.
    '''
    (Q, Sigma, delta, q0, F) = M
    qA = q0
    for x in cadeia:
        qA = delta[(qA, x)]
    return qA in F
