
graph = {'me': ['alice', 'bob', 'claire'], 'bob': ['anuj', 'peggy'], 'alice': ['peggy'], 'claire': ['thom', 'jonny'], 'anuj': [], 'peggy': [], 'thom': [], 'jonny': []}

def searching_seller(search_queue):
    while search_queue:
        person = search_queue.pop(0)
        searched = []
        if not person in searched:
            if person_is_seller(person):
                print('{} is a seller'.format(person))
                return True
            else:
                search_queue += graph[person]
                print(search_queue)
                searched.append(person)
    return False

def person_is_seller(person):
    return person[-1] == 'm'

# создаю очередь, очередь структура данных где элеметы добавляются и исключаются в порядке добавления (первый вошел первый вышел
search_queue = []
search_queue += graph['me']

searching_seller(search_queue)