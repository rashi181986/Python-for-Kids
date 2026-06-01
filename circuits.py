def solve_circuit(A, B, C):
    # Breakdown of gates
    gate1 = A & B           # Top AND
    gate2 = B | C           # Middle OR
    gate3 = B & C           # Bottom AND
    gate4 = gate2 & gate3   # Second-level AND
    
    # Final Output Q
    Q = gate1 | gate4       # Final OR
    return Q

# Generate Truth Table
print(f"{'A':<3} {'B':<3} {'C':<3} | {'Q':<3}")
print("-" * 15)

for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            output = solve_circuit(a, b, c)
            print(f"{a:<3} {b:<3} {c:<3} | {output:<3}")
