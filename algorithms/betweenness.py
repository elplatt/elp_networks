from shortest_paths import floyd_warshall

def betweenness(weights_from_to, normalized=True):
    nodes = set()
    for edge, weight in weights_from_to.iteritems():
        source, target = edge
        nodes.add(source)
        nodes.add(target)
    if normalized:
        norm = float(
            (len(nodes) - 1) * (len(nodes) - 2)
            )
    else:
        norm = 1.0
    distances, paths = floyd_warshall(weights_from_to)
    result = dict([(n, 0.0) for n in paths.keys()])
    for source, targets in paths.iteritems():
        for target, pair_paths in targets.iteritems():
            count = float(len(pair_paths))
            for p in pair_paths:
                for node in p:
                    try:
                        result[node] += 1.0/count/norm
                    except KeyError:
                        result[node] = 1.0/count/norm
    return result