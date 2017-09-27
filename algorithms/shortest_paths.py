
def floyd_warshall(edges_from):
    '''Find shortest paths between all edge pairs in a weighted graph with no negative cycles.
    edges_from: dict mapping source nodes to to their neighbors.
    returns: (distances, paths) dicst mapping node pairs to their distances and shortest path(s).
    '''
    # Create sorted list of nodes
    nodes = set(edges_from.keys())
    for source, targets in edges_from.iteritems():
        nodes |= set(targets)
    nodes = sorted(nodes)
    # Initialize distances
    dist = [[float("inf") for target in nodes] for source in nodes]
    for k, node in enumerate(nodes):
        dist[k][k] = 0
    # Initialize paths
    # For each source, target, there is a list of shortest paths (there may be multiple of the same length)
    paths = [[[] for taret in nodes] for source in nodes]
    # Use only first k nodes
    for k, node in enumerate(nodes):
        # Loop through pairs
        for i, source in enumerate(nodes):
            for j, target in enumerate(nodes):
                # Find shortest path using k
                dist_k = dist[i][k] + dist[k][j]
                # Find shortest path not using k
                dist_nok = dist[i][j]
                if dist_k < dist_nok:
                    # Set new distance
                    dist[i][j] = dist_k
                    paths_ij = []
                    # Add new paths
                    for ipath in paths[i][k]:
                        for jpath in paths[k][j]:
                            # Merge paths, remove one k
                            newpath = ipath[:-1] + jpath
                            paths_ij.append(newpath)
                    # Replace old paths
                    paths[i][j] = paths_ij
                elif dist_k == dist_nok:
                    # Same distance, but new paths
                    # Store path list for better performance
                    paths_ij = paths[i][j]
                    for ipath in paths[i][k]:
                        for jpath in paths[k][j]:
                            # Merge paths, remove one k
                            newpath = ipath[:-1] + jpath
                            paths_ij.append(newpath)
    return (dist, paths)