
from Environment import Environment
from Player import Player


def run():
    """
    Main function
    """
    env = Environment(15, 15)
    env.create_graph()
    # print()
    # for i in env.get_graph()[1][1].get_neighbour_cells():
    #     print("Neig:",i)
    env.print_graph()
    # graph = env.get_graph()
    player1 = Player(1, env.get_graph()[0][0])
    env.set_player1(player1)
    # env.movgen(env.get_player1())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()