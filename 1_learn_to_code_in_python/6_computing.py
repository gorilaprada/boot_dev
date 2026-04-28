"""
# Lesson 1 
def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage

run_cases = [
    (3, 5, 2, 1, 4, (15, 3.0)),
    (5, 5, 5, 5, 5, (25, 5.0)),
]

submit_cases = run_cases + [
    (1, 2, 3, 4, 5, (15, 3.0)),
    (0, 0, 0, 0, 10, (10, 2.0)),
    (0, 0, 0, 0, 0, (0, 0.0)),
    (10, 20, 30, 40, 50, (150, 30.0)),
    (2, 2, 2, 2, 2, (10, 2.0)),
    (1, 1, 1, 1, 1, (5, 1.0)),
]


def test(sword, arrow, spear, dagger, fireball, expected_output):
    print("---------------------------------")
    print(f"Inputs: {sword}, {arrow}, {spear}, {dagger}, {fireball}")
    result = calculate_damage(sword, arrow, spear, dagger, fireball)
    print(f"Expected: {expected_output}")
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
# Lesson 5
def update_player_score(current_score, increment):
    player_score = current_score + increment
    return player_score

run_cases = [
(0, 100, 100),
(100, 200, 300),
]

submit_cases = run_cases + [
    (300, 300, 600),
    (600, 50, 650),
    (0, 0, 0),
    (1, 1, 2),
    (100, -50, 50),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = update_player_score(input1, input2)
    print(f"Expected: {expected_output}")
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
# Lesson 6
def get_hurt(current_health, damage):
    current_health -= damage
    return current_health

run_cases = [
    (1000, 100, 900),
    (900, 60, 840),
]

submit_cases = run_cases + [
    (840, 10, 830),
    (830, 3, 827),
    (0, 0, 0),
    (1, 1, 0),
    (100, 2, 98),
    (2500, 3, 2497),
]


def test(current_health, damage, expected_output):
    print("---------------------------------")
    print(f"Inputs: {current_health}, {damage}")
    print(f"Expected:  {expected_output}")
    result = get_hurt(current_health, damage)
    print(f"Actual: {result}")
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
# Lesson 7
def max_players_on_server():
    small_server = 1.024e18
    medium_server = 1.024e19
    large_server = 1.024e20
    return small_server, medium_server, large_server

run_cases = [
    (1.024e18, 1.024e19, 1.024e20),
]

submit_cases = run_cases


def test(expected1, expected2, expected3):
    print("---------------------------------")
    result = max_players_on_server()
    print(f"Expected: {(expected1, expected2, expected3)}")
    print(f"Actual:   {result}")
    if result == (expected1, expected2, expected3):
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
# Lesson 13
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    return user_permissions & can_create_guild


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild

# Lesson 14
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond
# Lesson 15
def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()
"""
# Lesson 16
def binary_string_to_int(num_servers, num_players, num_admins):
    servers_int = int(num_servers, 2)
    players_int = int(num_players, 2)
    admins_int = int(num_admins, 2)
    return servers_int, players_int, admins_int
