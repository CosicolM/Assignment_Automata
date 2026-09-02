import java.util.*;

public class assignment {

    // Epsilon transition:
    // q2 --ε--> q3
    static Set<Integer> epsilonClosure(Set<Integer> states) {

        Set<Integer> closure = new HashSet<>(states);

        if (closure.contains(2)) {
            closure.add(3);
        }

        return closure;
    }

    // NFA transition function
    static Set<Integer> move(Set<Integer> states, char input) {

        Set<Integer> nextStates = new HashSet<>();

        for (int state : states) {

            // q0 --/--> q1
            if (state == 0 && input == '/') {
                nextStates.add(1);
            }

            // q1 --*--> q2
            if (state == 1 && input == '*') {
                nextStates.add(2);
            }

            // q2 --a--> q2
            // q2 --/--> q2
            if (state == 2 && input != '*') {
                nextStates.add(2);
            }

            // q3 --a--> q3
            if (state == 3 && input != '*') {
                nextStates.add(3);
            }

            // q3 --*--> q4
            if (state == 3 && input == '*') {
                nextStates.add(4);
            }

            // q4 --*--> q4
            if (state == 4 && input == '*') {
                nextStates.add(4);
            }

            // q4 --a--> q3
            if (state == 4 && input != '*' && input != '/') {
                nextStates.add(3);
            }

            // q4 --/--> q5
            if (state == 4 && input == '/') {
                nextStates.add(5);
            }
        }

        return nextStates;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        while (true) {

            System.out.print("\nEnter a string (or type 'exit' to quit): ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("exit")) {
                System.out.println("Program ended.");
                break;
            }

            // Start state q0
            Set<Integer> currentStates = new HashSet<>();
            currentStates.add(0);

            // Process every character
            for (int i = 0; i < input.length(); i++) {

                char c = input.charAt(i);

                /*
                 * In the NFA:
                 * 'a' represents an ordinary character.
                 *
                 * Therefore:
                 * H, e, l, l, o, etc. are treated as 'a'.
                 */
                if (c != '*' && c != '/') {
                    c = 'a';
                }

                // Apply epsilon transition BEFORE reading
                // the next character.
                currentStates = epsilonClosure(currentStates);

                // Follow the NFA transitions
                currentStates = move(currentStates, c);

                // If there are no possible states, reject
                if (currentStates.isEmpty()) {
                    break;
                }
            }

            // Apply epsilon closure one last time
            currentStates = epsilonClosure(currentStates);

            System.out.println("String: " + input);

            // q5 is the final/accepting state
            if (currentStates.contains(5)) {
                System.out.println("Output: Accepted");
            } else {
                System.out.println("Output: Rejected");
            }
        }

        

        scanner.close();
    }
}