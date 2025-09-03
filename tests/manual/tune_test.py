import http.client
import json


def send_tts_request(
    host="127.0.0.1",
    port=8000,
    api_rate=150,
    api_volume=0.7,
    api_text="./tunes/fanfar.mp3",
    api_voice="english",
    api_tune=True,
    password="password-1",
):
    conn = http.client.HTTPConnection(host, port)
    payload = {
        "api_rate": api_rate,
        "api_volume": api_volume,
        "api_text": api_text,
        "api_voice": api_voice,
        "api_tune": api_tune,
        "password": password,
    }
    headers = {"Content-Type": "application/json"}

    try:
        conn.request("POST", "/", body=json.dumps(payload), headers=headers)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        print(f"✅ Status: {response.status}")
        print(f"➡️ Response: {data}")
    except Exception as e:
        print(f"⚠️ Kunde inte kontakta servern, men ignorerar fel: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    send_tts_request()
