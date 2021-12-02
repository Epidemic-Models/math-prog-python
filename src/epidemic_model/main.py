import src.epidemic_model as sem


def main():
    height = 15
    width = 15
    num_agent = 100
    model = sem.EpidemicModel(num_agent=num_agent, height=height, width=width)

    timespan = 100
    for t in range(0, timespan):
        model.step()


if __name__ == "__main__":
    main()
