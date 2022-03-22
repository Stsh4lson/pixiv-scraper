from get_proxies import get_proxies

try:
  get_proxies()
except Exception:
  print("Couldnt download proxies, continuing with old list")