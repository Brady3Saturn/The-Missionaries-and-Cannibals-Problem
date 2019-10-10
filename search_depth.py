from whether_expandable import whether_expandable


def search_depth(init_state, set_of_operation, layer):  # 深度有界搜索算法
    open_list = []
    relation = {}
    open_list.append(init_state)
    layer_count = 0
    while 1:
        layer_count += 1
        if layer_count > layer:  # 使用layer来判断迭代深度，当深度超过预设值时，停止循环
            print("深度超过最大限度（%d），未找到解！", layer)
            break
        if open_list == []:  # 判断open表是否为空
            print("失败！open表为空，不存在可用节点,无解。")
            return
        vertex = open_list[0]
        open_list = open_list[1: -1]  # 更新open表
        if vertex == [0, 0, 1]:
            result = []  # 存储整个路径
            result.append(vertex)
            res = []  # 存储路径中的单个节点
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
        else:
            if vertex != init_state:
                sons = whether_expandable(vertex, set_of_operation, relation[str(vertex)])
            else:
                sons = whether_expandable(vertex, set_of_operation, [0, 0, 0])
            if sons:  # 判断当前节点是否可扩展
                for i in sons:
                    relation[str(i)] = vertex  # 用字典存储节点间的亲属关系，子节点为键，父节点为值
                    open_list.append(i)
