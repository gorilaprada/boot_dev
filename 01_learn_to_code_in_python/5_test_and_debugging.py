#!/usr/bin/python3
def total_xp(level, xp_to_add):
    lvl_xp = level * 100
    total_xp = lvl_xp + xp_to_add
    return total_xp

run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = run_cases + [
    (0, 0, 0),
    (0, 200, 200),
    (176, 350, 17950),
    (250, 100, 25100),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expected: {expected_output}")
    result = total_xp(input1, input2)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
"""
# Lesson 3
def take_magic_damage(health, resist, amp, spell_power):
    max_damage = spell_power * amp
    damage_after_resist = max_damage - resist
    new_health = health - damage_after_resist
    return new_health

# Lesson 7
def unlock_achievement(before_xp, ach_xp, ach_name):
    final_xp = before_xp + ach_xp
    alert = f"Achievement Unlocked: {ach_name}"
    return final_xp, alert

# Lesson 8
def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg
"""
