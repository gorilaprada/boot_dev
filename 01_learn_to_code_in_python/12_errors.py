"""
# Lesson 1
def main():
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
        print(get_player_record(5))
    except Exception as e:
        print(e)
# Lesson 4
def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")
#
# Lesson 7
def process_player_record(player_id):
    try:
        result = get_player_record(player_id)
        return result
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e
# 
"""
# Lesson 11
def purchase_item(price, gold_available):
    if price <= gold_available:
        return gold_available - price
    raise Exception("not enough gold")
# 

