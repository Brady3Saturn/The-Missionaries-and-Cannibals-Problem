from initial import create_edges
from initial import create_vertex
from search_breadth import search_breadth
from search_depth import search_depth
from search_heuristic import search_heuristic

capacity = 2  # 小船容载量，过低则可能导致问题无解
Missionaries = 3  # 修道士的人数
Cannibals = 3  # 野人人数
init_state = [Missionaries, Cannibals, 0]    # 问题初始状态，表示三个修道士、三个野人和小船都在初始岸
layer = 25  # 设置有界深度算法深度阈值
set_of_operation = create_edges(capacity)  # 生成所有可用的运算符，即图中存在的边
set_of_vertex = create_vertex(Missionaries, Cannibals)  # 生成所有可能的问题状态，即图中存在的顶点

# search_breadth(init_state, set_of_operation)  # 利用广度优先算法求解
search_depth(init_state, set_of_operation, layer)   # 利用有界深度算法求解
# search_heuristic(init_state, set_of_operation)   # 利用有界深度算法求解