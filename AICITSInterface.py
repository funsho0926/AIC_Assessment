from owlready2 import *
import math

# Load the ontology from an .rdf file
onto = get_ontology("file://rules_of_indices.rdf").load()

# Global: Fetch explanations of all rules
def fetch_rule_explanations():
    """Fetch and print rule explanations from the ontology."""
    print("\n--- Rule Explanations ---")
    for rule in onto.RuleExplanation.instances():
        print(f"Rule: {rule.name}")
        print(f"Explanation: {rule.hasInstructionText[0]}\n")


# Function to simplify indices using the Multiplication Rule
def simplify_multiplication(base, exponent1, exponent2):
    """Simplify multiplication of indices with the same base."""
    rule = onto.search_one(name="MultiplicationInstruction")
    explanation = rule.hasInstructionText[0] if rule else "No explanation found."
    simplified_exponent = exponent1 + exponent2

    print("\n--- Simplification using Multiplication Rule ---")
    print(f"Base: {base}")
    print(f"Original Exponents: {exponent1}, {exponent2}")
    print(f"Rule Applied: {explanation}")
    print(f"Result: {base}^{simplified_exponent}")

    return f"{base}^{simplified_exponent}"


# Function to simplify indices using the Division Rule
def simplify_division(base, exponent1, exponent2):
    """Simplify division of indices with the same base."""
    rule = onto.search_one(name="DivisionInstruction")
    explanation = rule.hasInstructionText[0] if rule else "No explanation found."
    simplified_exponent = exponent1 - exponent2

    print("\n--- Simplification using Division Rule ---")
    print(f"Base: {base}")
    print(f"Original Exponents: {exponent1}, {exponent2}")
    print(f"Rule Applied: {explanation}")
    print(f"Result: {base}^{simplified_exponent}")

    return f"{base}^{simplified_exponent}"


# Function to simplify indices using the Power Rule
def simplify_power(base, exponent1, exponent2):
    """Simplify power of indices."""
    rule = onto.search_one(name="PowerInstruction")
    explanation = rule.hasInstructionText[0] if rule else "No explanation found."
    simplified_exponent = exponent1 * exponent2

    print("\n--- Simplification using Power Rule ---")
    print(f"Base: {base}")
    print(f"Original Exponents: {exponent1}, {exponent2}")
    print(f"Rule Applied: {explanation}")
    print(f"Result: {base}^{simplified_exponent}")

    return f"{base}^{simplified_exponent}"


# Function to calculate power expressions numerically
def calculate_power(base, exponent):
    """Calculate the numerical value of a power expression."""
    correct_feedback = onto.search_one(name="CorrectFeedback1")
    correct_text = correct_feedback.hasFeedbackText[0] if correct_feedback else "Good job!"
    result = math.pow(base, exponent)

    print("\n--- Power Calculation ---")
    print(f"Expression: {base}^{exponent}")
    print(f"Result: {result}")
    print(f"Feedback: {correct_text}")

    return result


# Function to track and update student progress
def update_student_progress(student_name, activity, score):
    """Update student progress after completing an activity."""
    student = onto.search_one(name=student_name) or onto.Student(student_name)
    progress = onto.Progress(f"{student_name}_Progress")
    progress.hasCurrentScore.append(score)

    # Link student to progress
    student.hasProgress.append(progress)

    print("\n--- Updating Student Progress ---")
    print(f"Student: {student_name}")
    print(f"Completed Activity: {activity}")
    print(f"Score: {score}")
    print("Progress Updated Successfully.")


# Function to run a complete session for learning indices rules
def run_learning_session():
    """Simulate a learning session for a student."""
    print("Welcome to the Intelligent Tutoring System for Rules of Indices!")

    # Step 1: Fetch and display rule explanations
    fetch_rule_explanations()

    # Step 2: Practice simplification using the multiplication rule
    simplified_multiplication = simplify_multiplication("x", 2, 3)  # Example: x^2 * x^3
    print("Simplified Expression (Multiplication):", simplified_multiplication)

    # Step 3: Practice simplification using the division rule
    simplified_division = simplify_division("y", 5, 2)  # Example: y^5 / y^2
    print("Simplified Expression (Division):", simplified_division)

    # Step 4: Practice simplification using the power rule
    simplified_power = simplify_power("z", 3, 2)  # Example: (z^3)^2
    print("Simplified Expression (Power):", simplified_power)

    # Step 5: Perform a power calculation
    power_result = calculate_power(2, 3)  # Example: 2^3
    print("Calculated Value:", power_result)

    # Step 6: Update student progress
    update_student_progress("Alice", "Quiz on Rules of Indices", 95.0)


# Run the session
if __name__ == "__main__":
    run_learning_session()
