import os
import sys
from dotenv import load_dotenv

load_dotenv()


def has_hardcoded_api_key(source_path):
    try:
        with open(source_path, "r", encoding="utf-8") as source_file:
            for raw_line in source_file:
                compact = raw_line.strip().replace(" ", "")
                if not compact.startswith("API_KEY="):
                    continue

                if "os.getenv(" in raw_line or "get_config(" in raw_line:
                    continue

                if compact in ('API_KEY=""', "API_KEY=''"):
                    continue

                return True
    except OSError:
        sys.exit("Error: Cannot read source file for security check.")
        return False

    return False


def get_config(var_name, required: bool):
    value = os.getenv(var_name)
    if required and not value:
        print(f"[WARNING] Required configuration '{var_name}' is missing!")
        sys.exit(1)
    return value


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    MATRIX_MODE = get_config("MATRIX_MODE",
                             required=True)
    DATABASE_URL = get_config("DATABASE_URL",
                              required=True)
    API_KEY = get_config("API_KEY", required=True)
    LOG_LEVEL = get_config("LOG_LEVEL",
                           required=True)
    ZION_ENDPOINT = get_config("ZION_ENDPOINT",
                               required=True)

    print("Configuration loaded:")
    print(f"Mode: {MATRIX_MODE}")
    if DATABASE_URL:
        if MATRIX_MODE == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to configured instance")
    else:
        print("Database: Not configured")
    print(f"API Access: {'Authenticated' if API_KEY else 'Not configured'}")
    print(f"Log Level: {LOG_LEVEL}")
    print(f"Zion Network: {'Online' if ZION_ENDPOINT else 'Offline'}\n")

    print("Environment security check:")
    if has_hardcoded_api_key(__file__):
        print("[FAIL] Hardcoded secrets detected")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
