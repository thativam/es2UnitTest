import subprocess

def test_calculator_operations():
    # Start the calculator script
    process = subprocess.Popen(
        ['python3', 'Calculator.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    # Simulate a series of user inputs:
    # 1. Add 5 and 3
    # 2. Multiply the result by 2
    # 3. Divide the result by 4
    # 4. Exit
    input_sequence = '''1\n5\n3\n3\n2\n5\n4\n16\n4\n4\n1\n0\n7\n90\n0\n'''
    output, errors = process.communicate(input_sequence)
    print(output)
    assert "Resultado: 8.0" in output
    assert "Resultado: 10.0" in output
    assert "Resultado: 4.0" in output

test_calculator_operations()