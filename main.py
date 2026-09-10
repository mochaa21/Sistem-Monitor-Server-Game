from typing import List, Dict, Any

def parse_server_logs(logs: List[str]) -> Dict[str, Any]:
    total_ping = float('inf')
    unique_days = set()
    failed_log = 0
    for row in logs:
        raw_data = row.split(' | ')
        try:
            total_ping = float(raw_data[3])
            unique_days = set(raw_data[0])
        except ValueError:
            failed_log += 1
        except IndexError:
            failed_log += 1
    new_dict = {
        "total_ping": total_ping,
        "unique_days": unique_days,
        "failed_log": failed_log
    }
    return new_dict

# --- EKSEKUSI ---
server_logs = [
    "2026-09-09 | LOGIN | player_one | 45.5",
    "2026-09-09 | LOGIN | player_two | 12.0",
    "2026-09-10 | ERROR | Connection Timeout", 
    "2026-09-10 | LOGIN | player_three | err_ping", 
    "2026-09-11 | LOGIN | player_four | 30.0"
]

report = parse_server_logs(server_logs)
print(report)