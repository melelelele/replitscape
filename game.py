import configparser
import time

import cscape
import requests


config = configparser.ConfigParser()
config.read("config.ini")


class Game:
    title = "JavaScape: Die Teemaschine"

    REPLIT_STATUS_URL = config.get(
        "replit",
        "status_url",
        fallback="",
    )

    STATUS_KEYS = (
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "q6",
        "q7",
        "all",
    )

    def get_status_url(self):
        url = str(
            self.REPLIT_STATUS_URL or ""
        ).strip()

        if not url:
            return ""

        if not url.startswith(
            ("http://", "https://")
        ):
            url = "https://" + url

        if not url.rstrip("/").endswith(
            "/status"
        ):
            url = url.rstrip("/") + "/status"

        return url

    def empty_status(self, error=None):
        status = {
            key: False
            for key in self.STATUS_KEYS
        }

        if error:
            status["error"] = str(error)

        return status

    def get_status(self):
        status_url = self.get_status_url()

        if (
            not status_url
            or "YOUR_STATUS_URL" in status_url
        ):
            raise RuntimeError(
                "Bitte status_url in config.ini eintragen."
            )

        separator = (
            "&"
            if "?" in status_url
            else "?"
        )

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
                "Cache-Control": (
                    "no-cache, no-store, "
                    "must-revalidate"
                ),
                "Pragma": "no-cache",
                "Expires": "0",
            },
        )

        response.raise_for_status()
        raw_status = response.json()

        if not isinstance(raw_status, dict):
            raise ValueError(
                "Die Replit-Statusantwort "
                "ist kein JSON-Objekt."
            )

        return {
            key: raw_status.get(key) is True
            for key in self.STATUS_KEYS
        }

    def safe_status(self):
        try:
            return self.get_status()
        except Exception as error:
            print(
                "Replit-Statusprüfung "
                f"fehlgeschlagen: {error}",
                flush=True,
            )

            return self.empty_status(error)

    def safe_check(self, key):
        return (
            self.safe_status().get(key)
            is True
        )

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

    def check_q7_done(self):
        return self.safe_check("q7")

    def check_all_done(self):
        return self.safe_check("all")


if __name__ == "__main__":
    cscape.run(Game())
