from typing import List, Dict, Any

def parse_server_logs(logs: List[str]) -> Dict[str, Any]:
    # 1. Siapkan penampung: total ping (float), hari sukses (set()), log gagal (int)
    
    # 2. Looping setiap baris di dalam logs
    
    # 3. Lakukan try...except di dalam loop untuk memproses pemecahan string 
    #    dan type casting float().
    
    # 4. Return dictionary laporannya.
    pass

# --- EKSEKUSI ---
server_logs = [
    "2026-09-09 | LOGIN | player_one | 45.5",
    "2026-09-09 | LOGIN | player_two | 12.0",
    "2026-09-10 | ERROR | Connection Timeout", 
    "2026-09-10 | LOGIN | player_three | err_ping", 
    "2026-09-11 | LOGIN | player_four | 30.0"
]

# report = parse_server_logs(server_logs)
# print(report)