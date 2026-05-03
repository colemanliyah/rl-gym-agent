import json
from agent_tools import run_shell_command

def mock_stubborn_claude():
    """
    Simulates an LLM that is hallucinating or stuck.
    No matter what happens, it keeps trying the exact same command.
    """
    return {
        "stop_reason": "tool_use",
        "content": [
            {
                "type": "text", 
                "text": "I need to read the secret file. I will try again."
            },
            {
                "type": "tool_use",
                "id": "toolu_error_999",
                "name": "run_shell_command",
                "input": {
                    "container_name": "escape-room-1",
                    "command": "cat /root/file_that_does_not_exist.txt"
                }
            }
        ]
    }

def run_resilient_agent():
    print("--- STARTING MISSION (RESILIENCE TEST) ---\n")
    
    # 1. The Circuit Breaker Variables
    MAX_STEPS = 10
    step_count = 0
    
    # This list tracks the "signature" of every action the LLM takes
    action_history = [] 
    
    while step_count < MAX_STEPS:
        step_count += 1
        print(f"--- Step {step_count} ---")
        
        # 1. Get the response from our stubborn LLM
        response = mock_stubborn_claude()
        
        for block in response["content"]:
            if block["type"] == "text":
                print(f"🤖 Claude: {block['text']}")
                
            elif block["type"] == "tool_use":
                tool_name = block["name"]
                tool_args = block["input"]
                command = tool_args["command"]
                
                print(f"🛠️  Claude wants to run: '{command}'")
                
                # ==========================================
                # THE LOOP DETECTOR
                # ==========================================
                # Create a simple string to represent this exact action
                action_signature = f"{tool_name}:{command}"
                action_history.append(action_signature)
                
                # Check if the last 3 actions in history are completely identical
                if len(action_history) >= 3 and action_history[-3:] == [action_signature] * 3:
                    print("\n🚨 CIRCUIT BREAKER TRIPPED! Infinite Loop Detected.")
                    print("🛑 Intercepting tool execution to save system resources...")
                    
                    # Instead of running the Docker command, we forge a system error 
                    # and send it back to the LLM to force it to change its behavior.
                    intercept_message = "SYSTEM ERROR: You have executed this exact command 3 times in a row without success. Stop repeating this action. Run 'ls -la' to survey your environment and formulate a new plan."
                    
                    print(f"📤 Sending System Override to LLM: {intercept_message}\n")
                    
                    # We clear the history so the breaker resets for the next plan
                    action_history.clear() 
                    
                    # In a real API loop, you would append `intercept_message` to the 
                    # messages array as a `tool_result` here and hit `continue`!
                    
                    # For this mock, we will just simulate the agent crashing/stopping 
                    # so you can see the loop terminate safely.
                    print("✅ System successfully protected. Terminating test.")
                    return
                
                # ==========================================
                # NORMAL EXECUTION
                # ==========================================
                # If the circuit breaker didn't trip, run the real Docker tool!
                print(f"⚡ [Tool] Executing in Docker...")
                result = run_shell_command(
                    container_name=tool_args["container_name"], 
                    command=command
                )
                print(f"📥 [Result]: {result}\n")

    if step_count >= MAX_STEPS:
        print("\n🛑 HARD LIMIT REACHED: Agent hit maximum iterations.")

if __name__ == "__main__":
    run_resilient_agent()