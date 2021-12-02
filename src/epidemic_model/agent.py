from mesa.agent import Agent

import src.epidemic_model as sem


class EpidemicAgent(Agent):
    def __init__(self, unique_id: int, model: sem.EpidemicModel):
        super().__init__(unique_id, model)
        self.state = "S"

    def move(self):
        pass

    def epi(self):
        pass

    def infect(self):
        self.recover()
        self.infect()

    def recover(self):
        pass

    def step(self):
        self.move()
        self.epi()
