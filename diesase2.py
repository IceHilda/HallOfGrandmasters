"""
Expanded disease simulator
https://www.worldometers.info/coronavirus/
"""

import numpy as np
import pandas as pd
import time
from disease_lib_files import Population
import matplotlib.pyplot as plt


class DiseaseSim:
    def __init__(self):
        # Define parameters that control the simulation
        self.infection_rate = 0.5
        self.death_rate = 0.01
        self.heal_rate = 0.02
        self.vaccination_rate = 0
        self.vaccine_research_time = 50
        self.earth = Population()
        self.day = 0
        self.max_days = 30
        self.record = pd.DataFrame(columns=['Day', 'Healthy', 'Sick', 'Recovered', 'Dead'], index=[0])

    def status_update(self):
        print(f"Day {self.day}:")
        print(f"Healthy people: {self.earth.healthy}")
        print(f"Carriers: {self.earth.sick}")
        print(f"Dead: {self.earth.dead}")
        print(f"Recovered: {self.earth.recovered}")

    def add_to_record(self):
        """
        Method to take data from the current day of the simulation and save it to a dataframe (spreadsheet) of
        all pas information. Otherwise, it would be lost when the next day runs. Needed in order to save our data
        and plot it later.
        """
        new_record_line = pd.Series({
            'Day': self.day,
            'Healthy': self.earth.healthy,
            'Sick': self.earth.sick,
            'Recovered': self.earth.recovered,
            'Dead': self.earth.dead})
        #print("Appending", new_record_line)

        self.record = self.record.append(new_record_line, ignore_index=True)

    def initial_infection(self, starting_people=579):
        self.earth.healthy -= starting_people
        self.earth.sick += starting_people

    # A method to infect healthy people
    def infect(self):
        #incubation period 5.2 days (average)
        #incubation = self.day + 5
        contagious = self.earth.sick
        total_cases = round(np.random.normal(contagious * self.infection_rate))
        if self.earth.healthy < total_cases:
            total_cases = self.earth.healthy

        self.earth.healthy -= total_cases

        np.roll(self.earth.incubating, 1)
        self.earth.sick += self.earth.incubating[0]
        self.earth.incubating[0] = total_cases

    def recover(self):
        newly_recovered = round(np.random.normal(self.earth.sick * self.heal_rate))
        self.earth.recovered += newly_recovered
        self.earth.sick -= newly_recovered

    def die(self):
        newly_dead = round(np.random.normal(self.earth.sick * self.death_rate))
        self.earth.dead += newly_dead
        self.earth.sick -= newly_dead

    def run(self):
        self.initial_infection()
        # Check if 30 days have gone by, if so, print a status update
        while self.day < self.max_days:
            self.day += 1
            if self.day % 2 == 0:
                self.status_update()
            # Pretend quarantine and masks are lowering infection
            if self.day == 15:
                self.infection_rate /= 10
            self.infect()
            self.die()
            self.recover()
            self.add_to_record()

my_simulation = DiseaseSim()
my_simulation.run()

# Print the results


plt.plot(my_simulation.record['Day'], my_simulation.record['Sick']+my_simulation.record['Dead'], label='Cases')
plt.plot(my_simulation.record['Day'], my_simulation.record['Dead'], label='Dead')
plt.xlabel("Day")
plt.ylabel("Total Cases")
plt.legend()
plt.show()

