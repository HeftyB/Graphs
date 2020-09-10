def earliest_ancestor(ancestors, starting_node, current_node=None):

    childict = {}

    if current_node is None:
        current_node = starting_node

    for i in ancestors:
        if i[1] not in childict:
            childict[i[1]] = []
        childict[i[1]].append(i[0])

    if current_node in childict:
        for i in childict[current_node]:
            return earliest_ancestor(ancestors, starting_node, i)

    elif current_node is starting_node:
        return (-1)
        
    else:
        return current_node
