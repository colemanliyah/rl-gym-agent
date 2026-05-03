# 1. FOUNDATION
FROM ubuntu:latest

# 2. TOOLS (Notice sqlite3 is included)
RUN apt-get update && apt-get install -y curl jq sqlite3

# Set the working directory
WORKDIR /app

# ==========================================
# PUZZLE 1: The File System & Base64
# ==========================================
RUN echo "c2VjcmV0X2FnZW50X3Bhc3N3b3JkXzEyMw==" > /tmp/encoded_flag.txt

# ==========================================
# PUZZLE 2: The Environment Variable
# ==========================================
ENV TARGET_SYSTEM="production_db"

# ==========================================
# PUZZLE 3: The SQLite Database
# ==========================================
RUN sqlite3 my_database.db "CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, role TEXT, secret_code TEXT);" \
    && sqlite3 my_database.db "INSERT INTO employees (name, role, secret_code) VALUES ('Alice', 'Engineer', 'fake_code_1');" \
    && sqlite3 my_database.db "INSERT INTO employees (name, role, secret_code) VALUES ('Bob', 'Admin', 'AGENT_DB_FLAG_999');"

# 3. LIFE SUPPORT
CMD ["tail", "-f", "/dev/null"]