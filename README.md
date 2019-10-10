# The-Missionaries-and-Cannibals-Problem
a solution to The Missionaries and Cannibals Problem, using Python; DFS; BFS; heuristic
</br>This is one part of my homework.
<p1>修道士野人问题的Python求解<p1>
一、	问题描述
修道士(Missionaries)和野人(Cannibals)问题：
在河的左岸有N个传教士（M）、N个野人（C）和一条船（Boat)，修道士们想用这条船把所有人都运过河去，但有以下条件限制：
  （1）修道士和野人都会划船，但船每次最多只能运K个人；
  （2）在任何岸边野人数目都不能超过修道士，否则修道士会被野人吃掉。

约束条件：① M≧C 任何时刻两岸、船上都必须满足传教士人数不少于野人数（M=0时除外，既没有传教士）② M+C≦K 船上人数限制在K以内。

二、	状态空间表示
（一）状态空间
在此问题的求解中，选择使用三元组（M, C, S）表示问题的状态，式中M表示起始岸修道士人数，C表示起始岸野人人数，S为0-1变量，表示船的位置，当S为0时表示船在起始岸，为1时表示船在终点岸。如：（0，3，0）表示起始岸有三个野人，没有修道士，船在起始岸。
于是修道士野人问题可以描述为： 从（3，3，0）到（0，0，1）的状态转换。在此问题的状态空间中共有32 种状态，其中12种不合理状态：如（1，0，1）说明右岸有2个M，3个C；4种不可能状态：如（3，3，0）说明所有M和C都在左岸，而船在右岸，所以可用的状态共16种，组成合理的状态空间。可能的问题状态分别为：(0, 0, 1), (0, 1, 1), (0, 2, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1), (1, 2, 0), (1, 2, 1), (1, 3, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1), (2, 2, 0), (2, 2, 1), (2, 3, 0), (3, 1, 0), (3, 2, 0), (3, 3, 0)。

	（二）操作集
在此问题种定义Operation操作算符，用二元组（M, C）表示，式中M表示一次划船过程中船上修道士人数，C表示穿上野人人数。并规定，每一次使用操作算符对问题状态进行操作运算后，问题状态的S必须改变，即船必须从一岸驶向另一岸。例如，当对初始问题状态（3，3，0）使用（1，1）算符后，问题状态变成（2，2，1），这表示一个修道士和一个野人划船驶到终点岸，此时船停留在重点岸。根据左右两岸和穿上都不能出现野人人数大于修道士人数的约束，可以得到可用的操作算符共有5种，分别是（0, 1）, （0, 2）, （1, 0）, (1, 1), (2, 0)。

三、	程序设计
（一）存储结构
1.基本问题状态和操作算符使用列表存储。由于本问题仅需使用到简单的数据插入、提取等功能，因此可用选用Python提供的基本数据结构列表完成。使用列表表示问题的状态空间为：[[0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [1, 3, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1], [2, 3, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0]]；操作集为：[[0, 1], [0, 2], [1, 0], [1, 1], [2, 0]]；
2.节点关系使用字典存储。在找到目标节点后，需要回溯从开始节点走到当前节点的路径，这需要存储节点间的关系。这里使用字典存储节点间的亲属关系，子节点为键，父节点为值。

（二）算法基本思想
1.首先将问题初始状态（initial_state）节点放入OPEN表中（用于临时存储）；
2.从OPEN表中取出首节点，判断是否为目标节点。若为目标节点，则任务完成，输出结果；若不是目标节点，则进行下一步；
３.对从OPEN表中取出的不是目标节点的当前节点进行可扩展性判断，之后根据所使用的搜索策略将其子节点存入OPEN表；若当前节点不可扩展，则程序结束，问题无解。

（三）搜索策略
本次使用广度优先算法、有界深度优先算法和全局启发式搜索算法分别对问题进行求解。其中全局启发式搜索算法所使用的启发式函数为f(n) = d(n) + w(n), d(n)为当前节点深度，w(n)为未渡河人数；有界深度优先算法设置深度阈值为25。

（四）函数设计与调用关系
1.函数设计
此程序共设计并使用到10个自定义函数，其中
（1）create_vertex()和create_edges()用于初始化问题条件，生成相应的节点和边；
（2）move()用于对问题状态执行操作算符并控制移动过程中各状态的合理性（如避免出现不合理状态，控制船只状态等）；
（3）whether_expandable()用于判断当前节点是否可扩展；
（4）get_d(), get_w()和search_heuristic()共同实现启发式搜索。get_d()用于获取当前节点深度，get_w()用于计算当前节点距离目标节点的距离，即还有多少人尚未过河；
（5）search_depth()深度优先搜索算法；
（6）search_breadth()广度优先搜索算法；
（7）heap_adjust(), heap_create()和heap_sort()用于实现堆排序功能，此功能用于给生成的子节点进行排序。

2.函数调用关系
程序中函数调用关系为：
（1）	main()->create_vertex(), create_edges(), 搜索算法（三选一）；
（2）	search_breadth()->whether_expandable()->move()；
（3）	search_ depth ()->whether_expandable()->move()；
（4）	search_heuristic()->whether_expandable()->move()；
search_heuristic()->get_d(), get_w()；
search_heuristic()->heap_sort()->heap_adjust(), heap_create()。

四、	执行结果
（一）	启发式索搜
可用的操作算符为： [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0]]
可能出现的顶点有 16 种, 分别为： [[0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [1, 3, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1], [2, 3, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0]]
渡河成功！路径为：
[3, 3, 0] ->[2, 2, 1] ->[3, 2, 0] ->[3, 0, 1] ->[3, 1, 0] ->[1, 1, 1] ->[2, 2, 0] ->[0, 2, 1] ->[0, 3, 0] ->[0, 1, 1] ->[1, 1, 0] ->[0, 0, 1]

（二）	广度优先搜索
可用的操作算符为： [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0]]
可能出现的顶点有 16 种, 分别为： [[0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [1, 3, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1], [2, 3, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0]]
渡河成功！路径为：
[3, 3, 0] ->[3, 1, 1] ->[3, 2, 0] ->[3, 0, 1] ->[3, 1, 0] ->[1, 1, 1] ->[2, 2, 0] ->[0, 2, 1] ->[0, 3, 0] ->[0, 1, 1] ->[0, 2, 0] ->[0, 0, 1]

（三）	有界深度搜索
可用的操作算符为： [[0, 1], [0, 2], [1, 0], [1, 1], [2, 0]]
可能出现的顶点有 16 种, 分别为： [[0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [1, 3, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1], [2, 3, 0], [3, 1, 0], [3, 2, 0], [3, 3, 0]]
渡河成功！路径为：
[3, 3, 0] ->[3, 1, 1] ->[3, 2, 0] ->[3, 0, 1] ->[3, 1, 0] ->[1, 1, 1] ->[2, 2, 0] ->[0, 2, 1] ->[0, 3, 0] ->[0, 1, 1] ->[0, 2, 0] ->[0, 0, 1]
