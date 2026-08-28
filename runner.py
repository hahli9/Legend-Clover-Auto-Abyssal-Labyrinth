from time import sleep, time
from detection import *
from client import Client
import configparser

class Runner:
    FORM_AND_EMBARK_POS = (0.5, 0.8)
    BUFF_POS = (0.5, 0.4)
    EMBARK_POS = (0.5, 0.86)

    def __init__(self, client: Client):
        self.client = client
        # Parse config
        config = configparser.ConfigParser()
        config.read(r'config.txt')
        self.delay = config.getfloat('Times', 'delay')
        self.normal_fight = config.getfloat('Times', 'normal_fight')
        self.lv5_fight = config.getfloat('Times', 'lv5_fight')
        self.lv10_fight = config.getfloat('Times', 'lv10_fight')
        self.timeout = config.getint('Times', 'timeout')

    def start_run(self):
        # Click Form & Embark Button
        print(f"Form & Embark")
        if keep_looking_for_image(self.client, "abyssal.png"):
            self.client.click(self.FORM_AND_EMBARK_POS)
        sleep(self.delay)
        
        # Click Sortie
        print(f"Sortie")
        locate_and_click_image(self.client, "sortie.png")
        sleep(3)

    def handle_door(self, floor):
        door_image = "normal.png"
        if floor == 5:
            door_image = "lv5boss.png"
        if floor == 10:
            door_image = "lv10boss.png"

        print(f"Door")
        locate_and_click_image(self.client, door_image)        
        sleep(self.delay)

        print(f"Buff")
        self.client.click(self.BUFF_POS)
        sleep(self.delay)

        print(f"Embark")
        self.client.click(self.EMBARK_POS)
        sleep(self.delay)

        print(f"Handle Heal/Revive Prompt")
        location = keep_looking_for_image(self.client, "ok.png", 4)
        if location is not None:
            self.client.click(location)
        sleep(3)

    def handle_battle(self, floor):
        battleWaitTime = self.normal_fight
        if floor == 5:
            battleWaitTime = self.lv5_fight
        if floor == 10:
            battleWaitTime = self.lv10_fight

        print(f"Battle")
        locate_and_click_image(self.client, "battle.png")        
        # Wait for battle to end
        sleep(battleWaitTime)

        # End Battle
        print(f"Next")
        locate_and_click_image(self.client, "next.png")
        sleep(self.delay)
        print(f"Quest")
        locate_and_click_image(self.client, "quests.png")
        sleep(5)
    
    def handle_floor_10_reward(self):
        print(f"Handle Floor 10 Reward")
        locate_and_click_image(self.client, "ok.png")
        sleep(self.delay)

    def reset_abyss(self):
        print(f"Reset")
        locate_and_click_image(self.client, "reset.png")
        sleep(self.delay)
        print(f"Discard")
        locate_and_click_image(self.client, "discard.png")
        sleep(5)