from random import choice, randint

from resources.weapons import Weapons


class Bot:
    def action(self, country_status: dict, world_state: dict):
        weapon = randint(1, 3)

        target = choice(world_state["alive_players"])

        return {
            "Action": weapon,
            "Target": target
        }