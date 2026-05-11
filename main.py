def calculate_tip(bill, tip_percent, people=1, round_up=False):
    tip = bill * (tip_percent / 100)
    total = bill + tip
    per_person = total / people
    if round_up:
        import math
        per_person = math.ceil(per_person * 100) / 100
    return {"tip": tip, "total": total, "per_person": per_person}


def main():
    print("=== Tip Calculator ===")
    bill = float(input("Bill amount: $"))
    tip_percent = float(input("Tip percentage: "))
    people = int(input("Number of people: "))

    result = calculate_tip(bill, tip_percent, people)

    print(f"\nTip:        ${result['tip']:.2f}")
    print(f"Total:      ${result['total']:.2f}")
    print(f"Per person: ${result['per_person']:.2f}")


if __name__ == "__main__":
    main()
