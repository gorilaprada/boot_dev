"""
# Lesson 1
def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }
#
# Lesson 2
def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
    }
#
# Lesson 7
def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        elif enemy_name not in enemies_dict:
            enemies_dict[enemy_name] = 1
    return enemies_dict
# 
# Lesson 8
def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    max_count_name = None
    if not enemies_dict:
        return
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]
            max_count_name = enemy
    return max_count_name
# 
# Lesson 10
def get_quest_status(progress):
    return progress["quests"]["bridge_run"]["status"]
#
# Lesson 11
def merge(dict1, dict2):
    new_dict = {}
    for dict in dict1:
        new_dict[dict] = dict1[dict]
    for dict in dict2:
        new_dict[dict] = dict2[dict]
    return new_dict
#
"""




