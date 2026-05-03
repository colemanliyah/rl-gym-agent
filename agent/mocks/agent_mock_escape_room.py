import json
# We are still importing your REAL Docker tool!
from agent_tools import run_shell_command

def mock_claude_response(step):
    """
    Simulates Claude's responses based on what step of the loop we are in.
    """
    if step == 1:
        # Step 1: Claude looks for the environment variable
        return {
            "stop_reason": "tool_use",
            "content": [
                {"type": "text", "text": "I need to find the TARGET_SYSTEM environment variable first."},
                {
                    "type": "tool_use",
                    "id": "toolu_001",
                    "name": "run_shell_command",
                    "input": {
                        "container_name": "ultimate-escape-room",  
                        "command": "env | grep TARGET_SYSTEM"
                    }
                }
            ]
        }
    elif step == 2:
        # Step 2: Claude looks for the file and decodes it using a Linux pipe
        return {
            "stop_reason": "tool_use",
            "content": [
                {"type": "text", "text": "I see the environment variable. Now I will decode the flag in /tmp."},
                {
                    "type": "tool_use",
                    "id": "toolu_002",
                    "name": "run_shell_command",
                    "input": {
                        "container_name": "ultimate-escape-room",
                        "command": "cat /tmp/encoded_flag.txt | base64 --decode"
                    }
                }
            ]
        }
    else:
        # Step 3: Claude finishes the task
        return {
            "stop_reason": "end_turn",
            "content": [
                {"type": "text", "text": "I have successfully decoded the flag. The password is: secret_agent_password_123"}
            ]
        }

def run_mock_agent():
    print("--- STARTING MISSION (MOCK MODE) ---")
    print("Goal: Find the TARGET_SYSTEM environment variable and decode the flag in /tmp.\n")
    
    step_count = 0
    
    while True:
        step_count += 1
        print(f"🤔 Agent thinking (Step {step_count})...")
        
        # 1. Ask the "Fake" Claude API
        response = mock_claude_response(step_count)
        
        # 2. Process the text and tools
        for block in response["content"]:
            if block["type"] == "text":
                print(f"🤖 Claude: {block['text']}")
                
            elif block["type"] == "tool_use":
                tool_name = block["name"]
                tool_args = block["input"]
                
                print(f"\n🛠️  Claude executing: '{tool_args['command']}'...")
                
                # --- THE REAL MAGIC HAPPENS HERE ---
                # Even though the LLM is fake, this triggers your REAL Docker tool!
                if tool_name == "run_shell_command":
                    result = run_shell_command(
                        container_name=tool_args["container_name"], 
                        command=tool_args["command"]
                    )
                    
                    print(f"📥 [Real Docker Result]:\n{result}\n")
                    print("-" * 40)
        
        # 3. Check if we are done
        if response["stop_reason"] == "end_turn":
            print("\n✅ AGENT LOOP FINISHED")
            
            # Extract and return the final text so the grader can read it!
            for block in response["content"]:
                if block["type"] == "text":
                    return block["text"]
                    
            return "No final answer found."
if __name__ == "__main__":
    run_mock_agent()