from mesa.model import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

import src.epidemic_model as sem


class EpidemicModel(Model):
    def __init__(self, num_agent, width, height):
        super().__init__()
        self.num_gent = num_agent
        # Create the living space(grid)
        self.grid = MultiGrid(width=width,
                              height=height,
                              torus=True)
        self.schedule = RandomActivation(model=self)
        # Create the agents
        for agent_id in range(0, self.num_gent):
            a = sem.EpidemicAgent(unique_id=agent_id,
                                  model=self)
            self.schedule.add(agent=a)
            # Place the agent
            x = self.random.randrange(start=0, stop=self.grid.width)
            y = self.random.randrange(start=0, stop=self.grid.height)
            self.grid.place_agent(agent=a,
                                  pos=(x, y))

        # Pick one agent and infect them
        agent_to_infect = self.random.choice(self.schedule.agents)
        agent_to_infect.state = "I"

    def step(self):
        self.schedule.step()
