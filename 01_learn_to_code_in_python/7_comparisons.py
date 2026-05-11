"""
# Lesson 1
def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score
#
# Lesson 2
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphone_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphone_same
# Lesson 3
def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage
#
# Lesson 4
def print_status(player_health):
    if player_health <= 0:
        print("dead")
        return
    print("status check complete")

# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()
# Lesson 5
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_soldiers == number_of_swords:
        return("correct amount")
    else: 
        return("incorrect amount")
#
# Lesson 6
def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"
#
# Lesson 7
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"
#
# Lesson 8
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
#
# Lesson 9
def does_attack_hit(attack_roll, armor_class):
    if ((attack_roll != 1) & (attack_roll >= armor_class)) | (attack_roll == 20):
        return True
    else:
        return False
#
# Lesson 11
def should_serve_customer(customer_age, on_break, time):
    return (customer_age >= 21) & (on_break == False) & (5 <= time <= 10)
#
# Lesson 12
def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    else:
        return "no charges yet"

#
"""
# Lesson 13
def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched
#
