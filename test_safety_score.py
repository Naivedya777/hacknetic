# -------------------------
# Tester for Safety Score
# -------------------------

from ai.safety_score import analyze_messages
from ai.demo_dataset import apps_dataset

if __name__ == "__main__":

    # ---- Interactive Mode ----
    print("=== Safety Score Interactive Tester ===")
    print("Type 'exit' to quit.\n")

    batch = []
    while True:
        text = input("Enter a message (or 'exit' to finish): ")
        if text.lower() == "exit":
            break
        batch.append(text)

    if batch:
        analysis = analyze_messages(batch)
        print("\n--- Batch Analysis ---")
        print(f"Average Score: {analysis['average_score']} -> {analysis['overall_status']}\n")
        for r in analysis["results"]:
            print(f"Message: {r['message']}")
            print(f"  Score: {r['score']} | Status: {r['status']}")
            if r["detected_words"]:
                print(f"  Detected Words: {list(r['detected_words'].keys())}")
            print(f"  Suggestion: {r['suggestion']}\n")

    # ---- Predefined App Demo ----
    print("\n=== Predefined App Dataset Test ===")
    for app, comments in apps_dataset.items():
        result = analyze_messages(comments)
        print(f"{app}: {result['average_score']} -> {result['overall_status']}")