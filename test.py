from AFD import AFD


def main():
    M4 = AFD(alphabet={'0', '1'}, final_states={1}, transitions={
             0: {'0': 0, '1': 1},
             1: {'0': 2, '1': 1},
             2: {'0': 1, '1': 1}
             })

    words = ('00001', '0100', '00100000', '010101010')

    for word in words:
        states = ""
        M4.word = word

        for idx, state in enumerate(M4):
            if idx == 0:
                states += str(state)
            else:
                states += f"/{state}"

        print(M4, end=" on M4\n")
        print(states)

    M5 = AFD(alphabet={'a', 'b'}, final_states={1, 3}, transitions={
        0: {'a': 3, 'b': 1}, 1: {'a': 2, 'b': 1}, 2: {'a': 2, 'b': 1}, 3: {'a': 3, 'b': 4}, 4: {'a': 3, 'b': 4}
    })

    words = ('aabba', 'bababab', 'abaaab', 'aababb')
    for word in words:
        states = ""
        M5.word = word

        for idx, state in enumerate(M5):
            if idx == 0:
                states += str(state)
            else:
                states += f"/{state}"

        print(M5, end=" on M5\n")
        print(states)


if __name__ == '__main__':
    main()
