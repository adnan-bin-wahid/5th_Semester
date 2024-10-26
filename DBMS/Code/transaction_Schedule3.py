def parse_input(file_path):
    transactions = {}
    with open(file_path, "r") as file:
        for line in file:
            if line.strip() and line.startswith("T"):
                parts = line.strip().split(": ")
                transaction_id = parts[0]
                operations = parts[1].split()
                transactions[transaction_id] = operations
    return transactions

def build_dependency_graph(transactions):
    graph = {}
    data_access = {}  # Track all operations on each data item

    for step in range(len(next(iter(transactions.values())))):
        for t_id, ops in transactions.items():
            operation = ops[step]
            if operation != "-" and operation != "COM":
                op_type, data_item = operation[0], operation[2]

                if data_item not in data_access:
                    data_access[data_item] = []

                # Check all previous accesses to this data item for conflicts
                for last_t_id, last_op_type in data_access[data_item]:
                    if last_t_id != t_id:  # Only check conflicts with different transactions
                        if (op_type == "W" or last_op_type == "W"):
                            if last_t_id not in graph:
                                graph[last_t_id] = []
                            if t_id not in graph[last_t_id]:  # Avoid duplicate edges
                                graph[last_t_id].append(t_id)

                # Append the current operation to data_access for future conflict checking
                data_access[data_item].append((t_id, op_type))

    return graph


def detect_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(node)
        
        return False

    for node in graph:
        if dfs(node):
            return True  # Cycle found
    return False  # No cycle found

def is_conflict_serializable(graph):
    if detect_cycle(graph):
        print("\nCycle found in the graph.")
        return False
    else:
        print("\nNo cycles found in the graph.")
        return True

def main(file_path):
    transactions = parse_input(file_path)
    print("Parsed Transactions:")
    for t_id, ops in transactions.items():
        print(f"{t_id}: {ops}")

    # Build dependency graph
    graph = build_dependency_graph(transactions)
    
    # Display the graph edges
    print("\nDependency Graph Edges:")
    for node, edges in graph.items():
        for edge in edges:
            print(f"{node} -> {edge}")

    # Check for cycles
    if is_conflict_serializable(graph):
        print("The schedule is conflict-serializable.")
    else:
        print("The schedule is not conflict-serializable.")

# Run the program
file_path = "transaction_schedule3.txt"  # Make sure this file has the input in the correct format
main(file_path)