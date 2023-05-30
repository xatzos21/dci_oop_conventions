#!/usr/bin/env python


class Aquarium_app:
    def __init__(self, fish_count, eye_color, skin_color):
        self.skin_color = skin_color
        self._swim_count = 0
        self.eye_color = eye_color
        self.__dead_fish = 0
        self.fish_count = fish_count

    def start(self):
        if self.fish_count == 0:
            print("There are no alive fish left.")
            return
        self._swim_count += 1

        print(
            str(self.fish_count)
            + " fish are swimming. Their eyes are "
            + self.eye_color
            + " and their skin is "
            + self.skin_color
            + "."
        )
        print(
            "There are "
            + str(self.__dead_fish)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(self._swim_count)
            + " times."
        )

    def __die_fish(self, _number):
        if self.fish_count == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return
        self.fish_count -= _number
        self.__dead_fish += _number
        if _number > 1:
            print(str(_number) + " fish have died.")
        else:
            print("A fish has died.")


if __name__ == "__main__":
    my_aquarium_app = Aquarium_app(5, "blue", "red")
    my_aquarium_app.start()
    my_aquarium_app._Aquarium_app__die_fish(2)
    my_aquarium_app.start()
    my_aquarium_app._Aquarium_app__die_fish(1)
    my_aquarium_app.start()
    my_aquarium_app._Aquarium_app__die_fish(2)
    my_aquarium_app.start()
    my_aquarium_app._Aquarium_app__die_fish(1)
