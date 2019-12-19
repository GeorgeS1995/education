from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def light(self):
        pass


class GreenLight(State):
    def light(self):
        return "Green"


class RedLight(State):
    def light(self):
        return "Red"


class BlueLight(State):
    def light(self):
        return "Blue"


class YellowLight(State):
    def light(self):
        return "Yellow"

class Lamp:
    def __init__(self):
        self._current_state = None
        self._states = self.get_states()

    def get_states(self):
        return [GreenLight(), RedLight(), BlueLight(), YellowLight()]

    def next_state(self):
        if self._current_state == None:
            self._current_state = self._states[0]
        else:
            index = self._states.index(self._current_state)
            if index == len(self._states) -1:
                self._current_state = self._states[0]
            else:
                self._current_state = self._states[index + 1]
        return self._current_state

    def light(self):
        state = self.next_state()
        return state.light()

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    for i in range(4):
        print(lamp_1.light())

    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")