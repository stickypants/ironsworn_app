import random

class Weather():

    def __init__(self):
        pass

    def generate_temperature(self):

        dice = random.randint(1, 20)
        temp_varation = random.randint(1, 4) * 10

        if dice >= 1 and dice <= 14:
            output = "Normal for the season"
        if dice >= 15 and dice <= 17:
            output = "{} degrees Fahrenheit colder than normal".format(temp_varation)
        if dice >= 18 and dice <= 20:
            output = "{} degrees Fahrenheit hotter than normal".format(temp_varation)

        return output

    def generate_wind(self):

        dice = random.randint(1, 20)

        if dice >= 1 and dice <= 12:
            output = "None"
        if dice >= 13 and dice <= 17:
            output = "Light"
        if dice >= 18 and dice <= 20:
            output = "Strong"

        return output

    def generate_precipitation(self):

        dice = random.randint(1, 20)

        if dice >= 1 and dice <= 12:
            output = "None"
        if dice >= 13 and dice <= 17:
            output = "Light rain or light snowfall"
        if dice >= 18 and dice <= 20:
            output = "Heavy rain or heavy snowfall"

        return output

    def generate_weather(self):

        temperature = self.generate_temperature()
        wind = self.generate_wind()
        precipitation = self.generate_precipitation()

        output = "[WEATHER] \nTemperature : {temperature} \n" \
                 "Wind : {wind} \nPrecipitation : {precipitation} \n".format(**locals())

        return output


if __name__ == "__main__":
    weather = Weather()
    print(weather.generate_weather())



