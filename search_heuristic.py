from whether_expandable import whether_expandable   # 启发函数为f(n) = d(n) + w(n), d(n)为当前节点深度，w(n)为未渡河人数
from heap_sort import heap_sort


def get_d(vertex, init_state, relation):  # 用于计算当前节点的深度
    result = []  # 存储整个路径
    result.append(vertex)
    res = []  # 存储路径中的单个节点
    d = 0
    # print("渡河成功！路径为：")
    while res != init_state:
        d += 1
        res = relation[str(result[-1])]
        if res:
            result.append(res)
        else:
            break
    return d


def get_w(vertex):  # 用于计算当前节点距离目标节点的距离，即还有多少人尚未过河
    return vertex[0] + vertex[1] + 1 - vertex[2]


def search_heuristic(init_state, set_of_operation):
    open_list = []
    relation = {}
    open_list.append(init_state)
    while 1:
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
                sort_list = []
                for i in sons:
                    relation[str(i)] = vertex  # 用字典存储节点间的亲属关系，子节点为键，父节点为值
                    i.append(get_d(i, init_state, relation) + get_w(i))  # 使用启发函数对生成的子节点进行标注，并将标注的权值加到子节点列表内
                    sort_list.append(i)
                heap_sort(sort_list)
                for i in sort_list:
                    i = i[:-1]
                    open_list.append(i)

