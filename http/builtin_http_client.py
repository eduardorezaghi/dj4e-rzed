import http.client
import cfgs

def fetch_url(url):
    conn = http.client.HTTPConnection(url)
    conn.request("GET", "/")
    response = conn.getresponse()
    print(f"Status: {response.status}")
    print(f"Reason: {response.reason}")
    data = response.read()
    print(f"Data: {data.decode('utf-8')}")
    conn.close()

if __name__ == "__main__":
    fetch_url(f"{cfgs.local_settings['HOST']}:{cfgs.local_settings['PORT']}")
