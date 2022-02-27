def std_input(filename):
    with open(filename) as file_object:
        file_data = file_object.readlines()
    for index in range(0, len(file_data)):
        file_data[index] = file_data[index].split()

    loop = int(file_data.pop(0)[0])
    data = []

    for index in range(loop):
        msg = file_data.pop(0)
        data.append([1 - float(msg[0]), [0.0], [0.0]])
        for mess in range(int(msg[1])):
            mess = file_data.pop(0)
            data[index][1].append(int(mess[0]))
            data[index][2].append(1 - float(mess[1]))

    return data


def mess_dp(messes):
    cap, score, prob = messes[0], messes[1], messes[2]
    num, score_sum, score_max = len(score), int(sum(score)), max(score)
    memo = [1] + [0] * score_sum
    for index in range(1, num):
        for val in range(score_sum, score[index] - 1, -1):
            memo[val] = max(memo[val], memo[val - score[index]] * prob[index])

    for index in range(score_sum, 0, -1):
        if memo[index] >= cap:
            print(index)
            break


if __name__ == '__main__':
    messes_data = std_input('sample0.txt')
    for mess_data in messes_data:
        mess_dp(mess_data)
