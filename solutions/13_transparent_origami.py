def print_dots(dots):
    x, y = [*zip(*dots)]
    x_axis, y_axis = range(max(x) + 1), range(max(y) + 1)
    canvas = [[" " for _ in x_axis] for _ in y_axis]

    for k, l in dots:
        canvas[l][k] = "#"

    for i in y_axis:
        for j in x_axis:
            try:
                print(canvas[i][j], end="")
            except:
                print(i, j)
        print()

    print()


with open("../inputs/13_transparent_origami.txt", "r") as f:

    contents = [x.strip() for x in f]
    empty_line = contents.index("")

    dots = [tuple(int(n) for n in x.split(",")) for x in contents[:empty_line]]
    folds = [
        (x[eq - 1], int(x[eq + 1 :]))
        for x in contents[empty_line + 1 :]
        if (eq := x.index("="))
    ]

    copy_dots = dots.copy()

    for axis, place in folds:
        unique_dots = set()
        for x, y in copy_dots:
            dot = {"x": x, "y": y}
            will_shift = dot[axis] > place
            if will_shift:
                dot[axis] = dot[axis] - 2 * (dot[axis] - place)

            unique_dots.add((dot["x"], dot["y"]))

        copy_dots = unique_dots
        print(len(copy_dots))

    print_dots(copy_dots)