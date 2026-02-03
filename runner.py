from time import sleep, time
from detection import keep_looking_for_image
from client import Client
import configparser

class Runner:
    FORM_AND_EMBARK_POS = (0.5, 0.8)
    SORTIE_POS = (0.85, 0.9)
    DOOR_POS = (0.3, 0.5)
    BUFF_POS = (0.5, 0.4)
    EMBARK_POS = (0.5, 0.86)
    QUEST_POS = (0.9, 0.95)
    BATTLE_POS = (0.95, 0.85)
    OKAY_POS = (0.5, 0.73)
    RESET_POS = (0.95, 0.64)
    DISCARD_POS = (0.55, 0.85)

    def __init__(self, client: Client):
        self.client = client
        # Parse config
        config = configparser.ConfigParser()
        config.read(r'config.txt')
        self.delay = config.getfloat('Times', 'delay')
        self.normal_fight = config.getfloat('Times', 'normal_fight')
        self.lv5_fight = config.getfloat('Times', 'lv5_fight')
        self.lv10_fight = config.getfloat('Times', 'lv10_fight')

    def start_run(self):
        # Click Form & Embark Button
        print("Form & Embark.")
        self.client.click(self.FORM_AND_EMBARK_POS)
        sleep(self.delay)

        # Click Sortie
        print("Sortie")
        self.client.click(self.SORTIE_POS)
        sleep(3)
    
    def floor_loop(self, floor):
        battleWaitTime = self.normal_fight
        door_image = "normal.png"
        if floor == 5:
           battleWaitTime = self.lv5_fight
           door_image = "lv5boss.png"
        if floor == 10:
            battleWaitTime = self.lv10_fight
            door_image = "lv10boss.png"

        # Select Door
        print("Door")
        location = keep_looking_for_image(self.client, door_image)
        sleep(self.delay)
        self.client.click(location)
        sleep(self.delay)
        
        # Select Buff
        print("Buff")
        self.client.click(self.BUFF_POS)
        sleep(self.delay)

        # Select Embark
        print("Embark")
        self.client.click(self.EMBARK_POS)
        sleep(7)
            
        # Start Battle
        print("Battle")
        location = keep_looking_for_image(self.client, "battle.png")
        sleep(self.delay)
        self.client.click(location)
        
        # Wait for battle to end
        sleep(battleWaitTime)

        # End Battle
        print("Next")
        location = keep_looking_for_image(self.client, "next.png")
        sleep(self.delay)
        self.client.click(location)
        sleep(5)
        print("Quest")
        self.client.click(self.QUEST_POS)
        sleep(10)
    
    def handle_floor_10(self):
        # Handle 10th Floor Reward
        print("Handle 10th Floor Reward")        
        self.client.click(self.OKAY_POS)
        sleep(self.delay)

    def reset_abyss(self):
        # Reset
        print("Reset")        
        self.client.click(self.RESET_POS)
        sleep(self.delay)
        print("Discard")        
        self.client.click(self.DISCARD_POS)
        sleep(self.delay)

