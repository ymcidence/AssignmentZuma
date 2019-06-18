import tools

# Uncomment to change the colour name
# tools.COLOURS = []


if __name__ == '__main__':
    num_of_balls = 20

    seq = tools.gen_balls(num_of_balls, dtype='str')
    print('The input balls are coloured as:\n{}'.format(seq))

    magic_result = tools.spell_magic(seq)

    print('Max elimination length: {}'.format(magic_result))
