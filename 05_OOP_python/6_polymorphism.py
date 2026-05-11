"""
# Lesson 1
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
# Lesson 2
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        else:
            return self.__x2
            

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        else:
            return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        else:
            return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        else:
            return self.__y2

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
# Lesson 2
class Rectangle:
    def overlaps(self, rect):
        return (
            self.__x1 <= rect.get_right_x()
            and self.__x2 >= rect.get_left_x()
            and self.__y1 <= rect.get_top_y()
            and self.__y2 >= rect.get_bottom_y()
        )

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
#
# Lesson 4
class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


# don't touch above this line

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.height = height
        self.width = width
        self.fire_range = fire_range
        self.__hit_box = Rectangle((self.pos_x - (width / 2)), (self.pos_y - (height / 2)), (self.pos_x + (width / 2)), (self.pos_y + (height / 2)))
        print(self.__hit_box.get_left_x(), self.__hit_box.get_bottom_y(), self.__hit_box.get_right_x(), self.__hit_box.get_top_y())

    def in_area(self, x1, y1, x2, y2):
        new_box = Rectangle(x1, y1, x2, y2)
        return self.__hit_box.overlaps(new_box)

# don't touch below this line

class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
# Lesson 9
class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        if self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")
        else:
            raise Exception("cannot craft")
# Lesson 11
class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"
# Lesson 12
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return self.rank_index == other.rank_index and self.suit_index == other.suit_index
            

    def __lt__(self, other):
        if self.rank_index == other.rank_index and self.suit_index < other.suit_index:
            return True
        elif self.rank_index < other.rank_index:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.rank_index == other.rank_index and self.suit_index > other.suit_index:
            return True
        elif self.rank_index > other.rank_index:
            return True
        else:
            return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
"""
# Lesson 13
SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            self.rank_index == other.rank_index and self.suit_index == other.suit_index
        )

    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Round:
    def resolve_round(self):
        raise NotImplementedError("Subclasses must implement resolve_round()")


# Don't touch above this line


class HighCardRound(Round):
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        
    def resolve_round(self):
        if self.card1 > self.card2:
            return 1
        elif self.card1 < self.card2:
            return 2
        else:
            return 0


class LowCardRound(Round):
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        
    def resolve_round(self):
        if self.card1 < self.card2:
            return 1
        elif self.card1 > self.card2:
            return 2
        else:
            return 0

