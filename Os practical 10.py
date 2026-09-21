import random

requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
disk_size = 200


def movement(sequence, start):
    current = start
    total = 0

    for request in sequence:
        total += abs(request - current)
        current = request

    return total


# 1. FCFS
def fcfs(requests, head):
    sequence = requests[:]
    return sequence, movement(sequence, head)


# 2. SSTF
def sstf(requests, head):
    pending = requests[:]
    sequence = []
    current = head

    while pending:
        next_request = min(pending, key=lambda x: abs(x - current))
        sequence.append(next_request)
        pending.remove(next_request)
        current = next_request

    return sequence, movement(sequence, head)


# 3. C-SCAN
def cscan(requests, head, disk_size):
    lower = sorted([r for r in requests if r < head])
    upper = sorted([r for r in requests if r >= head])

    sequence = upper + [disk_size - 1, 0] + lower

    return sequence, movement(sequence, head)


# 4. C-LOOK
def clook(requests, head):
    lower = sorted([r for r in requests if r < head])
    upper = sorted([r for r in requests if r >= head])

    sequence = upper + lower

    return sequence, movement(sequence, head)


# 5. RSS - Random Scheduling
def rss(requests, head):
    sequence = requests[:]
    random.shuffle(sequence)

    return sequence, movement(sequence, head)


def display(name, sequence, total):
    print("S076 Rohan Bhowmick”)
    print(f"{name}")
    print("Order:", sequence)
    print("Total head movement:", total)
    print()


for name, function in [
    ("FCFS", fcfs),
    ("SSTF", sstf),
    ("C-SCAN", lambda r, h: cscan(r, h, disk_size)),
    ("C-LOOK", clook),
    ("RSS", rss)
]:
    sequence, total = function(requests, head)
    display(name, sequence, total)
