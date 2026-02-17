from typing import Final


LOST_ARCHIVE: Final[str] = "lost_archive.txt"
CLASSIFIED_VAULT: Final[str] = "classified_vault.txt"
STANDARD_ARCHIVE: Final[str] = "standard_archive.txt"


def handle_archive_access(filename: str) -> None:
    if filename == STANDARD_ARCHIVE:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        if filename == CLASSIFIED_VAULT:
            raise PermissionError("Security protocols deny access")

        with open(filename, "r", encoding="utf-8") as archive:
            content = archive.read().strip()

        print(f"SUCCESS: Archive recovered - ''{content}''")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, diagnostics complete")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_archive_access(LOST_ARCHIVE)
    handle_archive_access(CLASSIFIED_VAULT)
    handle_archive_access(STANDARD_ARCHIVE)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
