def prepare_secure_vault(filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as vault:
        vault.write("[CLASSIFIED] Quantum encryption keys recovered\n")
        vault.write("[CLASSIFIED] Archive integrity: 100%\n")


def read_secure_vault(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as vault:
        return vault.read()


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    filename = "secure_vault.txt"
    prepare_secure_vault(filename)

    print("SECURE EXTRACTION:")
    print(read_secure_vault(filename), end="")

    print("SECURE PRESERVATION:")
    with open(filename, "a", encoding="utf-8") as vault:
        vault.write("[CLASSIFIED] New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
