zoo = ('python', 'elephan', 'tiger')
print('count of animals in zoo is {}'.format(len(zoo)))
new_zoo = 'monkey', 'zebra' , zoo
print('count of cells in zoo is {}'.format(len(new_zoo)))
print('list of animal in new zoo is {}'.format(new_zoo))
print('Animal from the old zoo is {}'.format(new_zoo[2]))
print('last animal from the old zoo is {}'.format(new_zoo[2][2]))
print('count of animal in new zoo is {}'.format(len(new_zoo) - 1 + len(zoo)))
