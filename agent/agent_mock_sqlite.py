import json
from agent_tools import run_shell_command

def mock_claude_sqlite(step):
    """
    Simulates Claude's reasoning process for discovering and querying a database.
    """
    if step == 1:
        # Step 1: Claude doesn't know the table names, so it checks the schema first.
        return {
            "stop_reason": "tool_use",
            "content": [
                {"type": "text", "text": "I need to find the Admin's secret code in the database. First, I should check the database schema to see what tables and columns exist."},
                {
                    "type": "tool_use",
                    "id": "toolu_db_001",
                    "name": "run_shell_command",
                    "input": {
                        "container_name": "ultimate-escape-room",
                        "command": "sqlite3 /app/my_database.db '.schema'"
                    }
                }
            ]
        }
    elif step == 2:
        # Step 2: Claude reads the schema output and formulates a specific SQL query.
        return {
            "stop_reason": "tool_use",
            "content": [
                {"type": "text", "text": "I see there is an 'employees' table with 'role' and 'secret_code' columns. I will query the secret code for the Admin role."},
                {
                    "type": "tool_use",
                    "id": "toolu_db_002",
                    "name": "run_shell_command",
                    "input": {
                        "container_name": "ultimate-escape-room",
                        "command": "sqlite3 /app/my_database.db \"SELECT secret_code FROM employees WHERE role='Admin';\""
                    }
                }
            ]
        }
    else:
        # Step 3: Claude finishes the task with the data.
        return {
            "stop_reason": "end_turn",
            "content": [
                {"type": "text", "text": "I have successfully queried the database! The Admin's secret code is AGENT_DB_FLAG_999."}
            ]
        }

def run_sqlite_agent():
    print("--- STARTING MISSION: SQLITE INFILTRATION ---")
    print("Goal: Extract the Admin's secret code from the database.\n")
    
    step_count = 0
    
    while True:
        step_count += 1
        print(f"🤔 Agent thinking (Step {step_count})...")
        
        # 1. Ask the "Fake" Claude API
        response = mock_claude_sqlite(step_count)
        
        # 2. Process the text and tools
        for block in response["content"]:
            if block["type"] == "text":
                print(f"🤖 Claude: {block['text']}")
                
            elif block["type"] == "tool_use":
                tool_name = block["name"]
                tool_args = block["input"]
                
                print(f"\n🛠️  Claude executing: '{tool_args['command']}'...")
                
                # --- EXECUTE THE REAL DOCKER COMMAND ---
                if tool_name == "run_shell_command":
                    result = run_shell_command(
                        container_name=tool_args["container_name"], 
                        command=tool_args["command"]
                    )
                    
                    print(f"📥 [Real Database Result]:\n{result}\n")
                    print("-" * 40)
        
        # 3. Check if we are done
        if response["stop_reason"] == "end_turn":
            print("\n✅ MISSION ACCOMPLISHED")
            break

if __name__ == "__main__":
    run_sqlite_agent()