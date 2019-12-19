def probability(dice_number, sides, target):
    def table_run(coordinates, stoper, dep):
        def counter(y_length, target, coordinates):
            target_counter = 0
            P = 0
            for x in range(1, sides + 1):
                for y in y_length:
                    if x + y == target:
                        target_counter += 1
                        try:
                            P += coordinates[x][y]
                        except TypeError:
                            continue
            return target_counter,P
        y_length = range(dep, sides*dep+1)
        if dep == 2:
            P = 1 / sides ** dep
            coordinates["2d"] = {}
            counter_y_lenght = range(1, sides + 1)
            for y in y_length:
                y_counter, empty = counter(counter_y_lenght, y, coordinates)
                coordinates["2d"][y] = P * y_counter
            if stoper == dep:
                return coordinates
            return table_run(coordinates, stoper, dep + 1)
        dep_str = "{}d".format(dep - 1)
        for y in coordinates[dep_str].keys():
            P = coordinates[dep_str][y] * (1 / sides)
            for x in range(1, sides + 1):
                coordinates[x][y] = P
        dep_str = "{}d".format(dep)
        coordinates[dep_str] = {}
        counter_y_lenght = range(dep-1, sides*(dep-1)+1)
        for y in y_length:
            y_counter, P = counter(counter_y_lenght, y, coordinates)
            coordinates[dep_str][y] = P
        if stoper == dep:
            return coordinates
        return table_run(coordinates, stoper, dep+1)
    if target > dice_number * sides or target < dice_number:
        return 0.0
    if dice_number == 1:
        return 1/sides
    elif dice_number > 1:
        list_sides = range(1,sides + 1)
        coor_x = {}
        for x in list_sides:
            coor_x[x] = {}
            for y in list_sides:
                coor_x[x][y] = None
        dice_str = "{}d".format(dice_number)
        print(table_run(coor_x, dice_number, dep=2))
        return table_run(coor_x, dice_number, dep=2)[dice_str][target]



if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    print(probability(100, 100, 500))
    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"