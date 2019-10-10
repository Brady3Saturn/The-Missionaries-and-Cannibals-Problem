def create_vertex(missionary, cannibal):  # 生成问题中所有可能的状态，即所有顶点

    init_state = [missionary, cannibal, 0]  # 初始状态
    set_of_state = []  # 存储状态集的列表
    count = 0
    for i in range(missionary+1):  # 生成所有可能的状态，即所有顶点

        for j in range(cannibal+1):

            if init_state[0] == 0 or init_state[0] >= init_state[1]:
                if i != 0 and j != 0:
                    set_of_state.append([i, j, 0])
                if i != missionary and j != cannibal:
                    set_of_state.append([i, j, 1])
                count += 1
    print('可能出现的顶点有', count, '种, 分别为：', set_of_state)


def create_edges(capacity):  # 生成所有的运算子，即边
    set_of_operation = []  # 存储运算子的列表
    for i in range(capacity + 1):
        for j in range(capacity + 1):
            if i + j <= capacity and (i >= j or i == 0):
                if i == 0 and j == 0:
                    continue
                set_of_operation.append([i, j])
    print('可用的操作算符为：', set_of_operation)
    return set_of_operation





