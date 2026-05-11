# Lesson 1
def destroy_walls(walls_health):
    health = []
    for wall in walls_health:
        if wall > 0:
            health.append(wall)
    return health
# Lesson 4
def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"

def get_soldier_dps(soldier):
    soldier_dps = soldier["damage"] * soldier["attacks_per_second"]
    return soldier_dps
# 
