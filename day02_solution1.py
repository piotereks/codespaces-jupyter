import snoop
from functools import reduce
# Specify the file path
file_path = 'day02_input.txt'

# Open the file for reading
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = [line.strip() for line in file.readlines()]

snoop.install(enabled=False)
snoop.install(enabled=True)
snoop.install(out='debug.txt', overwrite=True)
@snoop(watch_explode=('colors_dict'))
def calc():
    data = []
    total = 0
    for line in file_contents:
        # data.append(tuple(line.split(':')))
        game, ssets = line.split(':')
        _, game = game.split(' ')
        game = int(game)

        ssets = ssets.split(';')
        # ssets = [tuple(s.split(',')) for s in ssets]
        # ssets = [[x.split(' ') for x in s.split(',')] for s in ssets]
        colors_dict = {'green':0, 'blue':0, 'red':0}
        # print(ssets)
        for s in ssets:
            # colors_dict = {'green':0, 'blue':0, 'red':0}
            # print(f"{s=}")
            for x in s.split(','):
                _, cnt, color = x.split(' ')
                # print(colors_dict)
                # print(f"{color}:{cnt}")
                # colors_dict[color] += int(cnt)
                if colors_dict.get(color, 0) < int(cnt):
                    colors_dict[color] = int(cnt)
                # print(f"=={colors_dict}")
                # {color:int(cnt)}
                # print({color:int(cnt)})
            # red 12, green 13, blue 14
        # print(game, colors_dict)
            # if not(colors_dict.get('red',0)<=12 \
            #     and colors_dict.get('green',0)<=13 \
            #     and colors_dict.get('blue',0)<=14):
            #         break
        # else:
        #     print(f"---->{game=} {colors_dict}")
        #     total += game
        x=[colors_dict.get('red',0), colors_dict.get('green',0), colors_dict.get('blue',0)]
        total+= reduce(lambda x,y: x *y, filter(lambda x : x!=0, x))
            # print(colors_dict)
        # print(type(game))
        # print(tuple(line.split(':')))
        # print(game, ssets)

    # Now 'file_contents' contains the content of the file
    # print(file_contents)
    # print(data)
    print(total)

calc()