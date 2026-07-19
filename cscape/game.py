import time
import requests
import cscape


class Game:
    title = "CodeScape: Das Programmierquiz"

    def get_status_url(self):
        raw_url = cscape.get("replit_status_url")

        if not raw_url:
            return ""

        url = str(raw_url).strip()

        if not url:
            return ""

        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        if not url.rstrip("/").endswith("/status"):
            url = url.rstrip("/") + "/status"

        return url

    def get_status(self):
        status_url = self.get_status_url()

        if not status_url:
            return {
                "q1": False,
                "q2": False,
                "q3": False,
                "all": False,
                "errors": ["No Replit status URL configured."]
            }

        separator = "&" if "?" in status_url else "?"
        url = status_url + separator + "cachebust=" + str(time.time_ns())

        response = requests.get(
            url,
            timeout=5,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0",
            }
        )
        response.raise_for_status()
        return response.json()

    def check_replit_url_done(self):
        status_url = self.get_status_url()

        if not status_url:
            return False

        try:
            status = self.get_status()
        except Exception as error:
            print("Replit status URL failed:", error)
            return False

        return isinstance(status, dict) and all(
            key in status for key in ["q1", "q2", "q3", "all"]
        )

    def check_q1_done(self):
        return self.get_status().get("q1") is True

    def check_q2_done(self):
        return self.get_status().get("q2") is True

    def check_q3_done(self):
        return self.get_status().get("q3") is True

    def check_all_done(self):
        return self.get_status().get("all") is True


if __name__ == "__main__":
    cscape.run(Game())