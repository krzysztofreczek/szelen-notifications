import http.client

# Miro: https://miro.com/app/board/o9J_lhf0WP8=/
if __name__ == '__main__':
    # this piece of code sends request to szelen repository and retrieves a chunk of events
    conn = http.client.HTTPSConnection("raw.githubusercontent.com")
    payload = ''
    headers = {}
    conn.request("GET", "/krzysztofreczek/szelen/master/db/events.0.js", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
