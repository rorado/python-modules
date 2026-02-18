# ft_crisis_response.py

def handle_crisis(filename: str) -> None:

    print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as vault:
            data = vault.read()
        print(f"SUCCESS: Archive recovered - {data}")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected error - {e}")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    test_files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for file in test_files:
        handle_crisis(file)
        print()


if __name__ == "__main__":
    main()
