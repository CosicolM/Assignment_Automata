def simulate_minimized_dfa_ex1(input_string):
    # Define the start state
    current_state1 = "AC"
    
    # Define accepting states (State E is the final/accepting state)
    accepting_states = {"E"}
    
    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            if current_state1 == "AC":
                current_state1 = "B"
            elif current_state1 == "B":
                current_state1 = "B"
            elif current_state1 == "D":
                current_state1 = "B"
            elif current_state1 == "E":
                current_state1 = "B"
        elif symbol == '1':
            if current_state1 == "AC":
                current_state1 = "AC"
            elif current_state1 == "B":
                current_state1 = "D"
            elif current_state1 == "D":
                current_state1 = "E"
            elif current_state1 == "E":
                current_state1 = "AC"
        else:
            return f"Error: Invalid character '{symbol}' in input."

    # Check if final state is an accepting state
    if current_state1 in accepting_states:
        return f"Input '{input_string}' is **ACCEPTED** (Ended in state {current_state1})"
    else:
        return f"Input '{input_string}' is **REJECTED** (Ended in state {current_state1})"

# Main loop for testing inputs
print("DFA Simulation (First Example) Started. Type 'exit' to quit.\n")

while True:
    user_input = input("Enter input string (e.g., 0110, 011011): ").strip()
    
    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
        
    # Run the simulation on the entered string
    result = simulate_minimized_dfa_ex1(user_input)
    print(result)
    print("-" * 40)