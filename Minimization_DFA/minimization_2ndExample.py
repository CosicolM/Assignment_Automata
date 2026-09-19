def simulate_minimized_dfa(input_string):
    # Define the start state
    current_state = "AB"
    
    # Define accepting states
    accepting_states = {"CDE"}
    
    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            if current_state == "AB":
                current_state = "AB"
            elif current_state == "CDE":
                current_state = "CDE"
            elif current_state == "F":
                current_state = "F"
        elif symbol == '1':
            if current_state == "AB":
                current_state = "CDE"
            elif current_state == "CDE":
                current_state = "F"
            elif current_state == "F":
                current_state = "F"
        else:
            return f"Error: Invalid character '{symbol}' in input."

    # Check if final state is an accepting state
    if current_state in accepting_states:
        return f"Input '{input_string}' is **ACCEPTED** (Ended in state {current_state})"
    else:
        return f"Input '{input_string}' is **REJECTED** (Ended in state {current_state})"

# Main loop for testing inputs
print("DFA Simulation Started. Type 'exit' to quit.\n")

while True:
    user_input = input("Enter input string (e.g., 010, 111): ").strip()
    
    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
        
    # Run the simulation on the entered string
    result = simulate_minimized_dfa(user_input)
    print(result)
    print("-" * 40)