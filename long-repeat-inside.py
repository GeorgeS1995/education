def repeat_inside(line):
    framies = dict()
    max_right_border = len(line) // 2
    length = len(line)
    longest_repeate = ""
    for frame_size in range(1,max_right_border + 1):
        for i in range(length - (frame_size*2)+1):
            frame = line[i:frame_size + i]
            try:
                framies[frame]
            except KeyError:
                framies[frame] = 1
            max_repeate = 1
            for y in range(i, length - (frame_size*2)+1, frame_size):
                if frame == line[frame_size + y:2*frame_size + y]:
                    max_repeate += 1
                else:
                    break
            if framies[frame] < max_repeate:
                framies[frame] = max_repeate
    for key in framies.keys():
        temp = key * framies[key]
        if framies[key] != 1 and len(longest_repeate) < len(temp):
            longest_repeate = temp
    return longest_repeate

repeat_inside("abcabcabab")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')
