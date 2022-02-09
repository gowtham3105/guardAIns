from Environment import Environment
from Player import Player


def run():
    """
    Main function
    """

    env = Environment(20, 20, 30, 1, 1)
    env.create_graph()

    # print()
    # for i in env.get_graph()[1][1].get_neighbour_cells():
    #     print("Neig:",i)
    env.print_graph()
    print(env.is_connected())

    # env.place_special_cells(3, 2, 2, 2)

    print(env.get_graph()[0][0].get_cell_type())

    player1 = Player(1, env.get_graph()[0][0])
    env.set_player1(player1)
    player2 = Player(1, env.get_graph()[0][0])
    env.set_player2(player2)
    print(env.get_player1().get_guardians())
    neigh = env.movegen(env.get_player1())
    print(neigh)
    print(env.get_player1().get_guardians())

    env.update_rounds()

    print(env.get_player1().get_guardians())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
