from mesa.agent import Agent


class EpidemicAgent(Agent):
    def __init__(self, unique_id: int, model):
        super().__init__(unique_id, model)
