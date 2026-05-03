import os
import json
from anthropic import Anthropic
from agent_tools import run_shell_command

client = Anthropic()

# We define the tool using 'container_name'
tools = [
    {
        "name": "run_shell_command",
        "description": "Executes a shell/bash command inside a Docker container. Use this to explore files, read environment variables, and run Linux utilities.",
        "input_schema": {
            "type": "object",
            "properties": {
                "container_name": {"type": "string", "description": "The name of the target container."},
                "command": {"type": "string", "description": "The exact bash command to run."}
            },
            "required": ["container_name", "command"]
        }
    }
]

def run_agent():
    # Your exact prompt!
    user_prompt = "Your target container is escape-room-1. Find the environment variable TARGET_SYSTEM and decode the flag in /tmp."
    
    print(f"--- MISSION: {user_prompt} ---\n")
    
    messages = [{"role": "user", "content": user_prompt}]
    
    # Circuit breaker to prevent infinite loops
    step_count = 0
    MAX_STEPS = 10
    
    while step_count < MAX_STEPS:
        step_count += 1
        print(f"🤔 Agent thinking (Step {step_count})...")
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )
        
        # Save Claude's decision to memory
        messages.append({"role": "assistant", "content": response.content})
        
        # Print Claude's thought process
        for block in response.content:
            if block.type == "text":
                print(f"🤖 Claude: {block.text}")
                
        # Handle the Stop Reasons
        if response.stop_reason == "end_turn":
            print("\n✅ MISSION ACCOMPLISHED")
            break
            
        elif response.stop_reason == "tool_use":
            for block in response.content:
                if block.type == "tool_use":
                    tool_args = block.input
                    
                    # Route to our Python function
                    if block.name == "run_shell_command":
                        result = run_shell_command(
                            container_name=tool_args["container_name"], 
                            command=tool_args["command"]
                        )
                        
                        print(f"📥 [Result]: {result}\n")
                        
                        # Feed the result back to Claude
                        messages.append({
                            "role": "user",
                            "content": [
                                {
                                    "type": "tool_result",
                                    "tool_use_id": block.id,
                                    "content": result
                                }
                            ]
                        })
                        
    if step_count >= MAX_STEPS:
        print("\n🛑 Agent hit maximum iterations and was stopped.")

if __name__ == "__main__":
    run_agent()