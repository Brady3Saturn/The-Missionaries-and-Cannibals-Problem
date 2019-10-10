def move(vertex, edge, init_missionary=3, init_cannibal=3):
    if vertex[2] == 1:
        missionary = vertex[0] + edge[0]
        cannibal = vertex[1] + edge[1]
        state_of_boat = 1 - vertex[2]
    else:
        missionary = vertex[0] - edge[0]
        cannibal = vertex[1] - edge[1]
        state_of_boat = 1 - vertex[2]
    if missionary != 0 and missionary < cannibal:
        return False
    elif (init_missionary - missionary) != 0 and ((init_missionary - missionary) < (init_cannibal - cannibal)):
        return False
    elif missionary < 0 or cannibal < 0 or (init_missionary - missionary) < 0 or (init_cannibal - cannibal) < 0:
        return False
    else:
        return [missionary, cannibal, state_of_boat]
