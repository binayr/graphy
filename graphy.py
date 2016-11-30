"""Graph traversal."""


def data_collector():
    """Method to Collect data from the user and evaluate."""
    cases = input('Enter Number of Test Cases: ')
    data = {i: {} for i in range(cases)}

    for i in range(cases):
        edges = []
        node_and_edges = map(int, raw_input(
            'Enter number of Nodes and Edges separated by space: ').split(' '))

        for j in range(node_and_edges[1]):
            edge_detail = map(int, raw_input(
                'Enter start & end point of edge separated by space: ').split(' '))
            edges.append(tuple(edge_detail))

        start = input('Enter Starting Point: ')

        nodes = range(1, node_and_edges[0] + 1)
        nodes.remove(start)

        data[i]['nodes'] = nodes
        data[i]['start'] = start
        data[i]['edges'] = edges

    evaluator(data, cases)


def evaluator(data, cases):
    """Method to evaluate the data from the the user and print result."""
    for case in range(cases):
        temp_data = data[case]

        for node in temp_data['nodes']:
            if (temp_data['start'], node) in temp_data['edges']:
                print 6,
            else:
                print -1,
        print


if __name__ == '__main__':
    data_collector()
