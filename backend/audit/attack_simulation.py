from backend.ledger.bulletin_board import get_ledger
import random

# -----------------------------
# 1️⃣ MANUAL ATTACK (USER INPUT)
# -----------------------------
def interactive_attack():

    ledger = get_ledger()

    if len(ledger) == 0:
        print("Ledger is empty!")
        return False

    print("\n======= MANUAL ATTACK MODE =======")
    print(f"Total Blocks Available: {len(ledger)}")

    try:
        index = int(input("Enter block index to tamper (0-based): "))
    except:
        print("Invalid input!")
        return False

    if index < 0 or index >= len(ledger):
        print("Invalid index!")
        return False

    print("\nOriginal Block:", ledger[index])

    print("\nChoose attack type:")
    print("1 → Modify ciphertext")
    print("2 → Delete block (simulate vote deletion)")

    choice = input("Enter choice: ")

    if choice == "1":
        ledger[index]["ciphertext"] = (999999, 999999)
        print("\n⚠️ Ciphertext modified!")

    elif choice == "2":
        ledger.pop(index)
        print("\n⚠️ Block deleted!")

    else:
        print("Invalid choice!")
        return False

    return True


# -----------------------------
# 2️⃣ AUTOMATIC ATTACK (NO INPUT)
# -----------------------------
def auto_attack():

    ledger = get_ledger()

    if len(ledger) == 0:
        return False

    # randomly pick block
    index = random.randint(0, len(ledger) - 1)

    # randomly choose attack type
    attack_type = random.choice(["modify", "delete"])

    print("\n⚠️ Suspicious activity detected...")
    print(f"[ATTACK TARGET] Block Index: {index}")

    if attack_type == "modify":
        ledger[index]["ciphertext"] = (999999, 999999)
        print("[ATTACK TYPE] Ciphertext modification")

    else:
        ledger.pop(index)
        print("[ATTACK TYPE] Block deletion")

    return True