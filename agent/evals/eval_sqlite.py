from mocks.agent_mock_sqlite import run_sqlite_agent

def test_database_puzzle():
    print("🧪 RUNNING EVALUATION: SQLite Database Puzzle (MOCK MODE)")
    
    # 1. The known right answer (Deterministic!)
    EXPECTED_FLAG = "AGENT_DB_FLAG_999"
    
    # 2. Run the MOCK agent
    # Note: Make sure your ultimate-escape-room container is running!
    final_agent_answer = run_sqlite_agent() 
    
    # 3. Grade the Agent
    print("\n" + "="*40)
    print("📊 EVALUATION RESULTS")
    print("="*40)
    
    if final_agent_answer and EXPECTED_FLAG in final_agent_answer:
        print("✅ PASS: The agent successfully found the correct database flag.")
        return True
    else:
        print("❌ FAIL: The agent did not return the correct flag.")
        print(f"Expected to find: {EXPECTED_FLAG}")
        print(f"Agent returned: {final_agent_answer}")
        return False

if __name__ == "__main__":
    test_database_puzzle()