import json
import configparser
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

import requests
import cscape

config = configparser.ConfigParser()
config.read("config.ini")
class Game:
    title = "JavaScape: Die Teemaschine"

    REPLIT_STATUS_URL = config["replit"]["status_url"]

    STATUS_KEYS = ("q1", "q2", "q3", "q4", "q5", "q6", "all")

    def get_status_url(self):
        url = str(self.REPLIT_STATUS_URL or "").strip()

        if not url:
            return ""

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        if not url.rstrip("/").endswith("/status"):
            url = url.rstrip("/") + "/status"

        return url

    def empty_status(self, error=None):
        status = {key: False for key in self.STATUS_KEYS}

        if error:
            status["error"] = str(error)

        return status

    def get_status(self):
        status_url = self.get_status_url()

        if not status_url or "YOUR_STATUS_URL" in status_url:
            raise RuntimeError(
                "Bitte REPLIT_STATUS_URL in config.ini eintragen."
            )

        separator = "&" if "?" in status_url else "?"
        request_url = (
            status_url
            + separator
            + "cachebust="
            + str(time.time_ns())
        )

        response = requests.get(
            request_url,
            timeout=8,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0",
            },
        )
        response.raise_for_status()

        raw_status = response.json()

        if not isinstance(raw_status, dict):
            raise ValueError("Die Replit-Statusantwort ist kein JSON-Objekt.")

        # Nur die erwarteten booleschen Werte an das Frontend weitergeben.
        return {
            key: raw_status.get(key) is True
            for key in self.STATUS_KEYS
        }

    def safe_status(self):
        try:
            return self.get_status()
        except Exception as error:
            print("Replit-Statusprüfung fehlgeschlagen:", error)
            return self.empty_status(error)

    def safe_check(self, key):
        return self.safe_status().get(key) is True

    def check_q1_done(self):
        return self.safe_check("q1")

    def check_q2_done(self):
        return self.safe_check("q2")

    def check_q3_done(self):
        return self.safe_check("q3")

    def check_q4_done(self):
        return self.safe_check("q4")

    def check_q5_done(self):
        return self.safe_check("q5")

    def check_q6_done(self):
        return self.safe_check("q6")

    def check_all_done(self):
        return self.safe_check("all")


def start_status_bridge(game, host="127.0.0.1", port=5001):
    """
    Stellt den Replit-Status lokal für index.html bereit.

    Die Replit-URL bleibt ausschließlich in game.py. Die Webseite fragt nur
    http://127.0.0.1:5001/status ab.
    """

    class StatusHandler(BaseHTTPRequestHandler):
        def send_json(self, status_code, payload):
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")

            self.send_response(status_code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Cache-Control")
            self.end_headers()
            self.wfile.write(body)

        def do_OPTIONS(self):
            self.send_response(204)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Cache-Control")
            self.end_headers()

        def do_GET(self):
            path = urlparse(self.path).path

            if path != "/status":
                self.send_json(404, {"error": "Not found"})
                return

            self.send_json(200, game.safe_status())

        def log_message(self, format, *args):
            return

    try:
        server = ThreadingHTTPServer((host, port), StatusHandler)
    except OSError as error:
        raise RuntimeError(
            f"Die lokale Status-Bridge konnte auf Port {port} nicht starten: {error}"
        ) from error

    thread = threading.Thread(
        target=server.serve_forever,
        name="javascape-status-bridge",
        daemon=True,
    )
    thread.start()

    print(f"JavaScape-Status-Bridge läuft auf http://{host}:{port}/status")
    return server


if __name__ == "__main__":
    game = Game()
    status_server = start_status_bridge(game)

    try:
        cscape.run(game)
    finally:
        status_server.shutdown()
        status_server.server_close()
