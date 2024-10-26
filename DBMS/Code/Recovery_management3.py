def parse_log(file_path):
    log = []
    with open(file_path, 'r') as file:
        for line in file:
            log.append(line.strip())
    return log

def analyze_log(log):
    committed = set()  # Committed transactions
    active_transactions = set()  # Active but not committed transactions
    redo_transactions = set()  # Transactions that need to be redone
    undo_transactions = set()  # Transactions that need to be undone
    elements = {}  # Dictionary to hold element updates for all transactions
    checkpoint_found = False
    last_checkpoint_index = -1

    # Step 1: Process log entries
    for i, entry in enumerate(log):
        if entry.startswith('<START'):
            transaction = entry.split(' ')[1].strip('>')
            active_transactions.add(transaction)

        elif entry.startswith('<COMMIT'):
            transaction = entry.split(' ')[1].strip('>')
            committed.add(transaction)
            if transaction in active_transactions:
                active_transactions.remove(transaction)

        elif entry.startswith('<CKPT'):
            # Checkpoint found, mark its position
            checkpoint_found = True
            last_checkpoint_index = i
            # Extract transactions in checkpoint
            checkpoint_transactions = set(entry[entry.index('(')+1:entry.index(')')].split(','))

        elif '<T' in entry and '>' in entry:
            parts = entry.strip('<>').split(' ')
            transaction, element, old_value, new_value = parts[0], parts[1], parts[2], parts[3]
            # Record the updates for each transaction in the elements dictionary
            if transaction not in elements:
                elements[transaction] = []
            elements[transaction].append((element, old_value, new_value))

    # Step 2: Identify redo and undo transactions
    if checkpoint_found:
        # After the checkpoint, we redo only committed transactions that are committed after the checkpoint
        for i in range(last_checkpoint_index + 1, len(log)):
            entry = log[i]
            if entry.startswith('<COMMIT'):
                transaction = entry.split(' ')[1].strip('>')
                redo_transactions.add(transaction)

        # Undo all transactions that are still active and not committed
        undo_transactions = active_transactions - committed
    else:
        # If no checkpoint, redo all committed transactions and undo all active transactions
        redo_transactions = committed
        undo_transactions = active_transactions - committed

    return redo_transactions, undo_transactions, elements

def perform_recovery(redo_transactions, undo_transactions, elements):
    redo = {}
    undo = {}

    # Step 3: Perform redo for committed transactions
    for transaction in redo_transactions:
        if transaction in elements:
            for update in elements[transaction]:
                element, old_value, new_value = update
                # Redo: Apply new values for each committed transaction
                redo[element] = new_value  # Apply redo

    # Step 4: Perform undo for uncommitted transactions
    for transaction in undo_transactions:
        if transaction in elements:
            for update in elements[transaction]:
                element, old_value, new_value = update
                # Undo: Rollback to old value for uncommitted transactions
                undo[element] = old_value  # Apply undo

    return redo, undo

def main():
    log_file = 'log.txt'  # Path to the log file
    log = parse_log(log_file)
    
    # Analyze the log to find redo and undo transactions
    redo_transactions, undo_transactions, elements = analyze_log(log)
    
    # Perform recovery actions (redo and undo)
    redo, undo = perform_recovery(redo_transactions, undo_transactions, elements)
    
    # Display the results
    print("Redo Transactions:", redo_transactions)
    print("Undo Transactions:", undo_transactions)
    
    print("\nRedo Phase:")
    for element, value in redo.items():
        print(f"{element} = {value}")
    
    print("\nUndo Phase:")
    for element, value in undo.items():
        print(f"{element} = {value}")

if __name__ == "__main__":
    main()
