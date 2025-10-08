# run_demo.py
import pandas as pd
from src.agent.planner import Planner
from src.agent.creative_ideator import CreativeIdeator
from src.agent.executor import Executor
from src.agent.verifier import Verifier

def main():
    # 1. Load dataset
    test_df = pd.read_csv("data/ethosTest.csv")  # adjust path if needed
    print(f"Loaded {len(test_df)} test samples.")

    # 2. Initialize agents
    planner = Planner()
    ideator = CreativeIdeator()
    executor = Executor()
    verifier = Verifier()

    # 3. Multi-agent reasoning loop
    results = []
    for i, row in test_df.iterrows():
        problem = str(row["text"]) if "text" in row else str(row[0])
        print(f"\n🧠 Processing item {i+1}: {problem[:60]}...")

        # Step 1: planning
        plan = planner.plan(problem)
        print("🗂️ Plan created.")

        # Step 2: creative ideation (divergent reasoning)
        ideas = ideator.brainstorm(problem)
        creative_hint = " | ".join(ideas[:2])
        print("💡 Ideas generated.")

        # Step 3: execution
        exec_result = executor.execute(plan + "\n" + creative_hint)
        print("⚙️ Execution complete.")

        # Step 4: verification
        verified = verifier.verify(problem, exec_result)
        print("✅ Verified answer ready.")

        results.append({
            "id": row.get("id", i),
            "text": problem,
            "answer": verified
        })

    # 4. Save output
    out_df = pd.DataFrame(results)
    out_df.to_csv("ethosOut.csv", index=False)
    print("\n🎯 Saved results to ethosOut.csv")

if __name__ == "__main__":
    main()
