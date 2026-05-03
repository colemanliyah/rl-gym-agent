# Local Testing Guide

## Build the Gym

```bash
cd gym-escape-room
docker build -t ultimate-gym .
```

## Run the Container

```bash
docker run -d --name ultimate-escape-room ultimate-gym
```

## Enter the Container

```bash
docker exec -it ultimate-escape-room bash
```

## Verify the Puzzles

1. File System + Base 64

``` bash
cat /tmp/encoded_flag.txt | base64 --decode
# Expected: secret_agent_password_123
```

2. Environment Variables

``` bash
env | grep TARGET_SYSTEM
# Expected: TARGET_SYSTEM=production_db
```

3. SQLite Query
```
sqlite3 my_database.db "SELECT secret_code FROM employees WHERE role='Admin';"
# Expected: AGENT_DB_FLAG_999
```

## Exit

```bash
exit
```
