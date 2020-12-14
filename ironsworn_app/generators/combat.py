import random
import os
import csv

from generators.table_handler import random_table_handler

class Combat():

    def __init__(self):
        pass

    def generate_combat(self):

        combat_method_output = random_table_handler("combat_methods", random.randint(1, 100))
        combat_target_output = random_table_handler("combat_targets", random.randint(1, 100))

        output = "[COMBAT] \nCombat Method : {combat_method_output} \n" \
                 "Combat Target : {combat_target_output} \n".format(**locals())

        return output

    def generate_pay_the_price(self):
        pay_the_price_output = random_table_handler("pay_the_price", random.randint(1, 100))

        output = "[PAY THE PRICE] \n{pay_the_price_output} \n".format(**locals())

        return output