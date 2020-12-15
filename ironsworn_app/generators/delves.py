import random
import os
import csv

from generators.table_handler import random_table_handler

class Delves():

    def __init__(self):
        pass

    def generate_features(self, theme, domain):

        feature_dice = random.randint(1, 100)

        if feature_dice < 21:
            feature_output = random_table_handler("theme_{}_features".format(theme), feature_dice)
        else:
            feature_output = random_table_handler("domain_{}_features".format(domain), feature_dice)

        feature_aspect_output = random_table_handler("delves_features_aspect", random.randint(1, 50))
        feature_focus_output = random_table_handler("delves_features_aspect", random.randint(1, 50))

        output = "[Feature] \nFeature : {feature_output} \nFeature Aspect: {feature_aspect_output} \nFeature Focus: {feature_focus_output}\n".format(**locals())

        return output

    def generate_dangers(self, theme, domain):

        danger_dice = random.randint(1, 100)

        if danger_dice <= 30:
            danger_output = random_table_handler("theme_{}_dangers".format(theme), danger_dice)
        if danger_dice >= 31 and danger_dice <= 45:
            danger_output = random_table_handler("domain_{}_dangers".format(domain), danger_dice)
        if danger_dice > 45:
            danger_output = random_table_handler("delves_dangers", danger_dice)

        output = "[Danger] \nDanger : {danger_output} \n".format(**locals())

        return output

    def generate_opportunity(self):

        opportunity_output = random_table_handler("delves_opportunity", random.randint(1, 100))

        output = "[Opportunity] \nOpportunity : {opportunity_output} \n".format(**locals())

        return output

    def generate_trap(self):

        trap_event_output = random_table_handler("delves_trap_event", random.randint(1, 25))
        trap_component_output = random_table_handler("delves_trap_component", random.randint(1, 25))

        output = "[Trap] \nTrap Event : {trap_event_output} \nTrap Component : {trap_component_output} \n".format(**locals())

        return output
