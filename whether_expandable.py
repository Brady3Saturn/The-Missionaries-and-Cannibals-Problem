from move import move


def whether_expandable(vertex, set_of_operation, pre_vertex):  # 判断当前节点是否可扩展
    sons = []
    for operation in set_of_operation:
        m = move(vertex, operation)
        if m:
            if m != pre_vertex:  # 扩展得到的子节点不应该是当前节点的父节点，即应当避免重复
                sons.append(m)
    if sons == []:
        return False
    else:
        return sons