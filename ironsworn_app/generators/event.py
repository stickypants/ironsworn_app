import random
import os
import csv

from generators.table_handler import random_table_handler

class Event():

    def __init__(self):
        pass

    def generate_event(self):

        event_theme = random.randint(1, 100)
        event_actions = random.randint(1, 100)

        event_theme_output = random_table_handler("themes", event_theme)
        event_actions_output = random_table_handler("actions", event_actions)

        output = "[EVENT] \nTheme : {event_theme_output} \n" \
                 "Action : {event_actions_output} \n".format(**locals())

        return output

    def generate_urban_event(self):
        urban_event = random.randint(1, 12) + random.randint(1, 8)
        urban_event_output = random_table_handler("urban_events", urban_event)

        output = "[EVENT] \n{urban_event_output} \n".format(**locals())
        return output

if __name__ == "__main__":
    w = Event()
    out = w.generate_event()
    print(out)