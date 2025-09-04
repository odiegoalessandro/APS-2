import os

ALLOWED_ENV_FILES = {".env", ".env.local",
                     ".env.production", ".env.development"}


def readenv():
    for filename in os.listdir("."):
        if not os.path.isfile(filename):
            continue

        if filename not in ALLOWED_ENV_FILES:
            continue

        with open(filename, "r") as file:
            for line in file:
                if line.strip() == "" or line.startswith("#"):
                    continue

                key, value = line.strip().split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")

                os.environ[key] = value

            file.close()
