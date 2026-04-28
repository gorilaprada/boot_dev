"""
# Lesson 1
def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]
# Don't edit below this line


def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")


def main():
    test()

main()
# Lesson 5
def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]
    item_index = 1

    return inventory[item_index]
#
run_cases = [
    ("Leather Scraps",),
]

submit_cases = run_cases + [
    ("Leather Scraps",),
]


def test(expected_output):
    print("---------------------------------")
    result = get_leather_scraps()
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
def get_last_index(inventory):
    return len(inventory) - 1
#
run_cases = [
    (["Potion"], 0),
    (["Potion", "Iron Breastplate"], 1),
    (["Potion", "Iron Breastplate", "Bread", "Longsword"], 3),
]

submit_cases = run_cases + [
    ([], -1),
    (["Single item"], 0),
    (["Shield", "Sword", "Bow", "Arrows", "Health Potion"], 4),
    (["Shield", "Sword", "Bow"], 2),
    (["Shield", "Sword"], 1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = get_last_index(input1)
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
# Lesson 7
def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory
#
run_cases = [
    (
        ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
        ["Potion", "Iron Bar", "Iron Sword", "Leather Armor"],
    ),
    ([None, None, None, None], [None, None, None, None]),
    (["Potion", "Iron Ore", None, None], ["Potion", "Iron Bar", None, None]),
]

submit_cases = run_cases + [
    (
        [None, "Iron Ore", None, "Leather Armor"],
        [None, "Iron Bar", None, "Leather Armor"],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = smelt_ore(input1)
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
# Lesson 8
def generate_user_list(num_users):
    player_ids = []

    for i in range(0, num_users):
        player_ids.append(i)

    return player_ids
#
run_cases = [
    (5, list(range(5))),
    (10, list(range(10))),
]

submit_cases = run_cases + [
    (0, []),
    (1, [0]),
    (100, list(range(100))),
    (25, list(range(25))),
    (50, list(range(50))),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = generate_user_list(input1)
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
# Lesson 9
def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()
# Lesson 10
def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0
    #
    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1
        else :
            print(f"The item was not a potion, bread or a shortsword")

    return potion_count, bread_count, shortsword_count
#
run_cases = [
    (["Bread", "Potion", "Shortsword", "Bread"], (1, 2, 1)),
    (["Potion", "Potion", "Shortsword", "Buckler", "Iron Mace"], (2, 0, 1)),
]

submit_cases = run_cases + [
    ([], (0, 0, 0)),
    (
        [
            "Potion",
            "Leather Scraps",
            "Bread",
            "Iron Ore",
            "Light Leather",
            "Bread",
            "Shortsword",
            "Longsword",
            "Ironwood Branch",
            "Shortsword",
            "Shortsword",
        ],
        (1, 2, 3),
    ),
    (["Bread", "Bread", "Bread", "Bread"], (0, 4, 0)),
    (["Shortsword", "Shortsword", "Shortsword", "Shortsword"], (0, 0, 4)),
    (["Potion"], (1, 0, 0)),
    (["Potion", "Bread", "Shortsword"], (1, 1, 1)),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    result = get_item_counts(input)
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
# Lesson 13
def contains_leather_scraps(items):
    found = False
    # don't touch above this line
    for item in items:
        if item == "Leather Scraps":
            found = True
    # don't touch below this line
    return found
#
run_cases = [
    (["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"], True),
    (["Potion", "Shortsword", "Buckler", "Iron Mace"], False),
]

submit_cases = run_cases + [
    ([], False),
    (["Leather Scraps"], True),
    (["Potion", "Leather Scraps", "Leather Scraps"], True),
    (["Potion", "Healing Potion"], False),
    (["Leather scraps"], False),
    (["Leather", "Scraps"], False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = contains_leather_scraps(input1)
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
# Lesson 14
def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]
    # don't touch above this line
    for i in range(0, len(old_character_levels)):
        if old_character_levels[i] < new_character_levels[i]:
            print(i)
# don't touch below this line
def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")

def main():
    test()

main()
# Lesson 15
def find_max(nums):
    max_so_far = float("-inf")
    if not nums:
        return max_so_far
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far
#
run_cases = [([1, 2, 3, 4, 5], 5), ([1, 2, 300, 4, 5], 300)]

submit_cases = run_cases + [
    ([1, 20, 3, 4, 5], 20),
    ([-1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 21, 18], 21),
    ([], float("-inf")),
    ([-1, -2, -3, -4, -5], -1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = find_max(input1)
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
# Lesson 16
def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        #
        if (i % 2) != 0:
            odd_numbers.append(i)
    #
    return odd_numbers
#
run_cases = [(10, [1, 3, 5, 7, 9]), (20, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])]

submit_cases = run_cases + [
    (0, []),
    (1, []),
    (2, [1]),
    (300, [i for i in range(1, 300, 2)]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = get_odd_numbers(input1)
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
# Lesson 17
def get_champion_slices(champions):
    return champions[2:], champions[:-1], champions[0:len(champions):2]
#
run_cases = [
    (
        ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad", "Gilforn"],
        (
            ["Gandolfo", "Thraine", "Norwad", "Gilforn"],
            ["Thrundar", "Morgate", "Gandolfo", "Thraine", "Norwad"],
            ["Thrundar", "Gandolfo", "Norwad"],
        ),
    ),
    (
        ["Frank", "Dennis", "Sweet Dee", "Mac", "Charlie"],
        (
            ["Sweet Dee", "Mac", "Charlie"],
            ["Frank", "Dennis", "Sweet Dee", "Mac"],
            ["Frank", "Sweet Dee", "Charlie"],
        ),
    ),
]

submit_cases = run_cases + [
    (([]), ([], [], [])),
    (
        (["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon", "Tony"]),
        (
            ["Spencer", "Bill", "Matthew", "Brandon", "Tony"],
            ["John", "Sydney", "Spencer", "Bill", "Matthew", "Brandon"],
            ["John", "Spencer", "Matthew", "Tony"],
        ),
    ),
]


def test(input1, expected_output):
    print("-" * 40)
    print(f"Input:\n{input1}")
    print(f"Expected:\n{expected_output}")
    try:
        slice_1, slice_2, slice_3 = get_champion_slices(input1)
        result = (slice_1, slice_2, slice_3)
    except Exception as e:
        print(f"Error: {e}")
        return False
    print(f"Actual:\n{result}")
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
# Lesson 18
def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    favorites = favorite_weapons + favorite_armor + favorite_items
    return favorites
#
run_cases = [
    (
        ["sword", "dagger"],
        ["bracers", "helmet"],
        ["feather", "iron bars"],
        (["sword", "dagger", "bracers", "helmet", "feather", "iron bars"]),
    ),
]

submit_cases = run_cases + [
    (
        ["lance"],
        ["shield"],
        ["potions"],
        (["lance", "shield", "potions"]),
    ),
    (
        ["bow", "staff"],
        ["breastplate"],
        ["scrolls", "bedroll"],
        (["bow", "staff", "breastplate", "scrolls", "bedroll"]),
    ),
    ([], [], [], ([])),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = concatenate_favorites(input1, input2, input3)
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
# Lesson 19
def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]
    return weapon in top_weapons
#
run_cases = [
    ("sword of justice", True),
    ("bronze mace", False),
    ("sword of slashing", True),
]

submit_cases = run_cases + [
    ("", False),
    ("great axe", True),
    ("silver bow", True),
    ("golden spear", False),
    ("spiked knuckles", True),
    ("spellbook", True),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:")
    print(f" * Weapon: {input1}")
    result = is_top_weapon(input1)
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
# Lesson 20
def trim_strongholds(strongholds):
    del strongholds[0:1]
    del strongholds[-2:]
#
# Lesson 21
def get_heroes():
    heroes = [
        ("Glorfindel",
        2093,
        True),
        ("Gandalf",
        1054,
        False),
        ("Gimli",
        389,
        False),
        ("Aragorn",
        87,
        False),
    ]

    return heroes
#
# Lesson 22
def get_first_item(items):
    if not items:
        return "ERROR"
    return items[0]
# 
# Lesson 23
def reverse_list(items):
    new_list = []
    if not items:
        return []
    for i in range(len(items) - 1, -1, -1):
        new_list.append(items[i])
    return new_list
#
# Lesson 24 
def filter_messages(messages):
    # Create lists to return
    filtered_messages = []
    dang_count = []


    # Filter dang out of messages
    for i in range(0, len(messages)):
        good_words = []
        bad_words = []

        words = messages[i].split()
        for word in words:
            if word == "dang":
                bad_words.append(word)
            elif word != "dang":
                good_words.append(word)

        good_words_str = " ".join(good_words)
        filtered_messages.append(good_words_str)

        # Count of dang
        dang_count.append(len(bad_words))

    # print(filtered_messages, dang_count)
    # Returning filtered messages and dang count
    return filtered_messages, dang_count

# 
# Lesson 25 list_name[start : end : step]
def split_players_into_teams(players):
    even_list = players[0: len(players): 2]
    odd_list = players[1: len(players): 2]

    return even_list, odd_list
#
"""
# Lesson 26
def check_ingredient_match(recipe, inventory):
    items_obtained_count = 0
    items_missing = []
    for ingredient in recipe:
        if ingredient in inventory:
            items_obtained_count += 1
        else :
            items_missing.append(ingredient)
    percentage = round(((items_obtained_count / len(recipe)) * 100), 2)

    return(percentage, items_missing)
#
