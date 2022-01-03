from datetime import datetime


def log_error(msg):
    with open("errorlog.txt", "a") as f:
        f.write(f"ERR {datetime.now()} | {msg}\n")


if __name__ == "__main__":
    pass
