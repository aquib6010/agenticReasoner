# run_demo.py
import pandas as pd
from src.agent.data_handler import load_train_data, load_test_data, save_predictions

def simple_reasoner(problem, options):
    """
    Placeholder reasoning agent.
    Replace this with your actual reasoning model later.
    """
    # Example logic: pick the longest option (mock heuristic)
    best_option = max(options, key=len)
    reasoning = f"Based on analysis, '{best_option}' seems most appropriate."
    return reasoning, best_option

def main():
    # Load data
    print("oading data...")
    train_df = load_train_data()
    test_df = load_test_data()

    print(f"Train shape: {train_df.shape}")
    print(f"Test shape: {test_df.shape}")

    # Prepare predictions
    outputs = []
    print(" Running reasoning agent on test data...")
    for _, row in test_df.iterrows():
        problem = row["problem_statement"]
        options = [row[f"answer_option_{i}"] for i in range(1, 5)]
        reasoning, best_option = simple_reasoner(problem, options)

        outputs.append({
            "topic": row["topic"],
            "problem_statement": problem,
            "solution": reasoning,
            "correct_option": best_option
        })

    # Convert to DataFrame
    out_df = pd.DataFrame(outputs)

    # Save to ethosOut.csv
    save_predictions(out_df)

    print(" Finished generating ethosOut.csv!")

if __name__ == "__main__":
    main()

