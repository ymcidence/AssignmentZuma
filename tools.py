import graphviz
import math
import random

COLOURS = ['red', 'yellow', 'lightblue2', 'lightgrey']


def visualize(seq: list, name: str):
    """
    Saves a picture that shows all balls.
    :param seq: a list of numbers indicating different colours of balls
    :param name: the name of the picture to be saved
    :return:
    """
    name_pad_length = math.ceil(math.log10(seq.__len__()))
    this_graph = graphviz.Graph(comment=name, format='png')
    this_graph.node_attr.update(style='filled', shape='doublecircle')

    this_graph.node('0'.zfill(name_pad_length), '', color=COLOURS[seq[0]])
    for i in range(1, seq.__len__()):
        this_node_id = str(i).zfill(name_pad_length)
        last_node_id = str(i - 1).zfill(name_pad_length)
        this_graph.node(this_node_id, '', color=COLOURS[seq[i]])
        this_graph.edge(this_node_id, last_node_id)

    # noinspection PyUnboundLocalVariable
    this_graph.edge('0'.zfill(name_pad_length), this_node_id)
    this_graph.render(name, './pics')


def magic_card(seq: list, colour_from: int, colour_to: int):
    """
    Magic!
    :param seq: a list of numbers indicating different colours of balls
    :param colour_from: an int representing the respective colour to be modified
    :param colour_to: an int representing the respective target colour
    :return:
    """
    return [i if i != colour_from else colour_to for i in seq]


def gen_balls(num: int, dtype='int'):
    """
    Generates a random list of balls with different colours
    :param num: number of balls
    :param dtype: int/str, the type of each output element
    :return:
    """
    if dtype == 'int':
        return [random.randrange(0, COLOURS.__len__()) for _ in range(num)]
    elif dtype == 'str':
        return [COLOURS[random.randrange(0, COLOURS.__len__())] for _ in range(num)]


def get_elimination_length(seq: list):
    """
    Finds the maximum number of connected mono-colour balls.

    HOWTO: This is done by popping out already-read elements and counting upon colour change

    :param seq: a list of numbers indicating different colours of balls
    :return: the length
    """
    current_colour = seq[0]
    current_length = 0

    while seq[-1] == current_colour:
        current_length += 1
        seq.pop()
    max_length = current_length

    while seq.__len__() > 1:
        current_length += 1

        if max_length <= current_length:
            max_length = current_length

        if seq[0] != seq[1]:
            current_length = 0
            current_colour = seq[1]

        seq.pop(0)

    if current_colour == seq[0] and max_length == current_length:
        max_length += 1

    return max_length


def spell_magic(seq: list):
    """

    :param seq: a list of string indicating different colours of balls
    :return:
    """
    try:
        seq = [COLOURS.index(i) for i in seq]
    except ValueError:
        print('Please check the colours of the balls.')
        return -1

    visualize(seq, 'before')

    max_elimination_length = get_elimination_length(seq.copy())
    colour_from = -1
    colour_to = -1

    for i in range(COLOURS.__len__()):
        magic_candidate = [ii for ii in range(COLOURS.__len__())]
        magic_candidate.remove(i)

        for j in magic_candidate:
            new_seq = magic_card(seq, colour_from=i, colour_to=j)
            elimination_length = get_elimination_length(new_seq)

            if elimination_length >= max_elimination_length:
                colour_from = i
                colour_to = j
                max_elimination_length = elimination_length

    if colour_from >= 0 and colour_to >= 0:
        print('Best cast: {} ===> {}'.format(COLOURS[colour_from], COLOURS[colour_to]))
        final_seq = magic_card(seq, colour_from, colour_to)
        visualize(final_seq, 'after')
    else:
        print('Best cast: doing nothing')
        visualize(seq, 'after')

    return max_elimination_length


if __name__ == '__main__':
    _seq = gen_balls(14)
    visualize(_seq, 'try')
    print(get_elimination_length(_seq))
