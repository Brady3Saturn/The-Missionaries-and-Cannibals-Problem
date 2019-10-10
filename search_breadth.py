from whether_expandable import whether_expandable


def search_breadth(init_state, set_of_operation):  # 广度优先搜索算法
    open_list = []
    relation = {}
    open_list.append(init_state)
    while 1:
        if open_list == []:  # 判断open表是否为空
            print("失败！open表为空，不存在可用节点,无解。")
            return
        vertex = open_list[0]
        open_list = open_list[1: -1]  # 更新open表
        if vertex == [0, 0, 1]:  # 当前节点为目标节点，打印输出
            result = []  # 存储整个路径
            result.append(vertex)
            res = []   # 存储路径中的单个节点
            print("渡河成功！路径为：")
            while res != init_state:
                res = relation[str(result[-1])]
                if res:
                    result.append(res)
                else:
                    break
            for i in result[::-1]:
                if i != result[0]:
                    print(i, '->', end='')
                else:
                    print(i)
            
            return
        else:  # 当前节点不是目标节点时
            if vertex != init_state:
                sons = whether_expandable(vertex, set_of_operation, relation[str(vertex)])
            else:
                sons = whether_expandable(vertex, set_of_operation, [0, 0, 0])
            if sons:  # 判断当前节点是否可扩展
                for i in sons:
                    relation[str(i)] = vertex  # 用字典存储节点间的亲属关系，子节点为键，父节点为值
                    open_list.append(i)
