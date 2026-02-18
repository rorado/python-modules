def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    filename = "new_discovery.txt"
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    print(f"Initializing new storage unit: {filename}")
    archive = open(filename, "w")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    for entry in entries:
        archive.write(entry + "\n")
        print(entry)
    print()
    archive.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
