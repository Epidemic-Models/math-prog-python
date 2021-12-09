from mesa.agent import Agent

import src.epidemic_model as sem


class EpidemicAgent(Agent):
    def __init__(self, unique_id: int, model: sem.EpidemicModel):
        super().__init__(unique_id=unique_id,
                         model=model)
        self.state = "S"
        self.model = model

    def move(self):
        possible_cells = self.model.grid.get_neighborhood(
            pos=self.pos,
            moore=True,
            include_center=False,
            radius=6
        )
        new_position = self.random.choice(seq=possible_cells)
        self.model.grid.move_agent(agent=self,
                                   pos=new_position)

    def epi(self):
        self.recover()
        self.infect()

    def infect(self):
        infection_prob = 0.7
        if self.state == "I":
            agents_in_the_same_cell = self.model.grid.get_cell_list_contents([self.pos])
            agents_in_the_same_cell.remove(self)
            if len(agents_in_the_same_cell) > 0:
                for agent in agents_in_the_same_cell:
                    rand = self.random.random()
                    if agent.state == "S":
                        if rand < infection_prob:
                            agent.state = "I"

    def recover(self):
        recovery_prob = 1 / 5.0
        if self.state == "I":
            rand = self.random.random()
            if rand < recovery_prob:
                self.state = "R"

    def step(self):
        self.move()
        self.epi()


def susc(model: sem.EpidemicModel):
    s = 0
    for agent in model.schedule.agents:
        if agent.state == "S":
            s += 1
    return s


def inf(model: sem.EpidemicModel):
    i = 0
    for agent in model.schedule.agents:
        if agent.state == "I":
            i += 1
    return i


def rec(model: sem.EpidemicModel):
    r = 0
    for agent in model.schedule.agents:
        if agent.state == "R":
            r += 1
    return r
