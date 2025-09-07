import random

# Predefined interview questions
TECHNICAL_QUESTIONS = {
    "Software Engineer": [
        "Explain the difference between a list and a tuple in Python.",
        "What is time complexity of binary search?",
        "How would you design a simple URL shortener?"
    ],
    "Data Analyst": [
        "What is the difference between INNER JOIN and LEFT JOIN in SQL?",
        "Explain the concept of data normalization.",
        "How would you handle missing values in a dataset?"
    ]
}

BEHAVIORAL_QUESTIONS = [
    "Tell me about a time you faced a challenge at work and how you handled it.",
    "Describe a situation where you had to work in a team to solve a problem.",
    "Give an example of when you showed leadership skills."
]

# Simple evaluation keywords
EVALUATION_KEYWORDS = {
    "python": ["list", "tuple", "mutable", "immutable"],
    "binary search": ["log", "time complexity", "divide"],
    "url shortener": ["hash", "database", "mapping", "redirect"],
    "sql": ["join", "key", "table"],
    "normalization": ["redundancy", "consistency", "normal form"],
    "missing values": ["drop", "mean", "median", "impute"]
}


def evaluate_answer(question, answer):
    """Very simple evaluation based on keyword matches."""
    score = 0
    feedback = []

    for topic, keywords in EVALUATION_KEYWORDS.items():
        if topic in question.lower():
            for kw in keywords:
                if kw in answer.lower():
                    score += 2
                    feedback.append(f"Good use of '{kw}'.")
            break

    if score == 0:
        feedback.append("Try to be more specific and include technical terms/examples.")

    return min(score, 10), " ".join(feedback)


def run_interview():
    print("=== Interview Simulator ===\n")

    # Choose role
    role = input("Choose role (Software Engineer / Data Analyst): ").strip()
    if role not in TECHNICAL_QUESTIONS:
        print("Invalid role. Defaulting to Software Engineer.")
        role = "Software Engineer"

    # Choose mode
    mode = input("Choose mode (Technical / Behavioral): ").strip().lower()
    if mode not in ["technical", "behavioral"]:
        print("Invalid mode. Defaulting to Technical.")
        mode = "technical"

    # Select questions
    if mode == "technical":
        questions = random.sample(TECHNICAL_QUESTIONS[role], 3)
    else:
        questions = random.sample(BEHAVIORAL_QUESTIONS, 3)

    total_score = 0
    print(f"\nStarting a {mode.title()} Interview for {role}...\n")

    # Ask questions
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q}")
        ans = input("Your answer: ")

        score, feedback = evaluate_answer(q, ans) if mode == "technical" else (5, "Good attempt! Try to use STAR method.")
        total_score += score

        print(f"Feedback: {feedback}")
        print(f"Score for this answer: {score}/10\n")

    # Final summary
    avg_score = total_score / len(questions)
    print("=== Interview Summary ===")
    print(f"Average Score: {avg_score:.1f}/10")

    if avg_score >= 7:
        print("Strengths: Clear understanding, confident answers.")
        print("Areas to improve: Add more depth/examples in answers.")
    else:
        print("Strengths: You attempted the questions well.")
        print("Areas to improve: Revise key concepts, practice explaining clearly.")

    print("Suggested Resources: LeetCode, InterviewBit, and STAR interview method guides.\n")


if __name__ == "__main__":
    run_interview()
