def main(state, desired, len):
    match len:
        case 0:
            pass
        case 1:
            state[0] = desired[0]
            print(f"{'Metti' if desired[0] else 'Togli'} anello {1} -> {state}")
        case _:
            for i in range(len - 1, -1, -1):
                if state[i] == desired[i]:
                    continue
                else:
                    new_desired = [0] * (i - 1)
                    new_desired.append(1)
                    main(state, new_desired, i)
                    state[i] = desired[i]
                    print(
                        f"{'Metti' if desired[i] else 'Togli'} anello {i+1} -> {state}"
                    )


main([1,1,1,1,1,1,1,0,0], [1]*9, 9)
