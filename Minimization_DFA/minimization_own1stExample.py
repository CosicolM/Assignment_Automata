def simulate_minimized_dfa_latest(input_string):
    # Define the start state
    current_state = "A"
    
    # Define accepting states (States F and G are merged into 'FG' and are accepting)
    accepting_states = {"FG"}
    
    # Process each symbol in the input string
    for symbol in input_string:
        if symbol == '0':
            if current_state == "A":
                current_state = "A"
            elif current_state == "B":
                current_state = "C"
            elif current_state == "C":
                current_state = "DE"
            elif current_state == "DE":
                current_state = "FG"
            elif current_state == "FG":
                current_state = "FG"
        elif symbol == '1':
            if current_state == "A":
                current_state = "B"
            elif current_state == "B":
                current_state = "DE"
            elif current_state == "C":
                current_state = "FG"
            elif current_state == "DE":
                current_state = "C"
            elif current_state == "FG":
                current_state = "DE"
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
    user_input = input("Enter input string (e.g., 1100, 11001): ").strip()
    
    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
        
    # Run the simulation on the entered string
    result = simulate_minimized_dfa_latest(user_input)
    print(result)
    print("-" * 40)