from mocks.agent_mock_escape_room import run_mock_agent

def test_escape_room_puzzle():
    print("🧪 RUNNING EVALUATION: Escape Room File System (MOCK MODE)")
    
    # 1. The known right answer we hid in the Docker container
    EXPECTED_FLAG = "secret_agent_password_123"
    
    # 2. Run the MOCK agent
    final_agent_answer = run_mock_agent() 
    
    # 3. Grade the Agent
    print("\n" + "="*40)
    print("📊 EVALUATION RESULTS")
    print("="*40)
    
    if final_agent_answer and EXPECTED_FLAG in final_agent_answer:
        print("✅ PASS: The agent successfully decoded the base64 flag.")
        return True
    else:
        print("❌ FAIL: The agent did not return the correct flag.")
        print(f"Expected to find: {EXPECTED_FLAG}")
        print(f"Agent returned: {final_agent_answer}")
        return False

if __name__ == "__main__":
    test_escape_room_puzzle()