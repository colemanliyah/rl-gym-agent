import docker

def run_shell_command(container_name: str, command: str) -> str:
    """Executes a shell command inside a specific running Docker container."""
    client = docker.from_env()
    
    try:
        container = client.containers.get(container_name)
        print(f"⚡ [Tool] Executing: '{command}' in '{container_name}'")
        
        # THE BULLETPROOF FIX: Pass as a list instead of a formatted string.
        # Docker will natively handle the escaping for you!
        exit_code, output = container.exec_run(cmd=["sh", "-c", command])
        
        result_text = output.decode('utf-8').strip()

        if exit_code != 0:
            return f"Command failed (Exit code {exit_code}). Error:\n{result_text}"

        return result_text if result_text else "Command executed successfully (no output)."

    except docker.errors.NotFound:
        return f"System Error: Container '{container_name}' not found."
    except Exception as e:
        return f"System Error: {str(e)}"