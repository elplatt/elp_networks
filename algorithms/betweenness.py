from shortest_paths import floyd_warshall

def betweenness(weights_from_to):
    distances, paths = floyd_warshall(weights_from_to)
    result = dict([(n, 0.0) for n in paths.keys()])
    for source, targets in paths.iteritems():
        for target, pair_paths in targets.iteritems():
            count = float(len(pair_paths))
            for p in pair_paths:
                for node in p:
                    try:
                        result[node] += 1.0/count
                    except KeyError:
                        result[node] = 1.0/count
    return result
