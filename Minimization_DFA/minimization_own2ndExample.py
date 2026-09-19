def simulate_minimized_dfa_ex2(input_string):
    # Define the start state
    current_state = "AD"
    
    # Define accepting states (State E is the final/accepting state)
    accepting_states = {"E"}
    
    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            if current_state == "AD":
                current_state = "C"
            elif current_state == "B":
                current_state = "B"
            elif current_state == "C":
                current_state = "E"
            elif current_state == "E":
                current_state = "B"
        elif symbol == '1':
            if current_state == "AD":
                current_state = "B"
            elif current_state == "B":
                current_state = "B"
            elif current_state == "C":
                current_state = "AD"
            elif current_state == "E":
                current_state = "AD"
        else:
            return f"Error: Invalid character '{symbol}' in input."

    # Check if final state is an accepting state
    if current_state in accepting_states:
        return f"Input '{input_string}' is **ACCEPTED** (Ended in state {current_state})"
    else:
        return f"Input '{input_string}' is **REJECTED** (Ended in state {current_state})"

# Main loop for testing inputs
print("DFA Simulation (Example 2) Started. Type 'exit' to quit.\n")

while True:
    user_input = input("Enter input string (e.g., 0100, 01001): ").strip()
    
    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
        
    # Run the simulation on the entered string
    result = simulate_minimized_dfa_ex2(user_input)
    print(result)
    print("-" * 40)