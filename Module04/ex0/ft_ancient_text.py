def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    try:
        vault = open(filename, "r", encoding="utf-8")
        print("Connection established...")
        recovered_data = vault.read()
        print("RECOVERED DATA:")
        print(recovered_data)
        vault.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
