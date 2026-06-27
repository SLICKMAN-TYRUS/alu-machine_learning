cat > pipeline/apis/2-user_location.py << 'EOF'
#!/usr/bin/env python3
"""Script to print the location of a GitHub user via the GitHub API."""
import requests
import sys
import time
import math


if __name__ == '__main__':
    url = sys.argv[1]
    headers = {"User-Agent": "alu-machine_learning"}
    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        reset_time = int(response.headers.get("X-Ratelimit-Reset", 0))
        minutes = math.ceil((reset_time - time.time()) / 60)
        print("Reset in {} min".format(minutes))
    elif response.status_code == 404:
        print("Not found")
    else:
        data = response.json()
        print(data.get("location"))
EOF