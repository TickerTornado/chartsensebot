import os, json, requests

def get_chartink_results(payload_env):
    # payload_env is a JSON string placed in CHARTINK_SCAN_JSON
    try:
        scan_payload = json.loads(payload_env)
    except Exception:
        return []
    url = "https://chartink.com/api/screener/data"
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, json=scan_payload, headers=headers, timeout=15)
    r.raise_for_status()
    data = r.json()
    rows = data.get("data", {}).get("rows", [])
    return [row.get("n") for row in rows if row.get("n")]
