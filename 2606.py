"""
    2606. 바이러스
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(num_of_computers, num_of_pairs):
    def set_network():
        for _ in range(num_of_pairs):
            to, frm = map(lambda input : int(input) - 1, read().split())
            network[to][frm] = True
            network[frm][to] = True

    def infect(to):
        targets = set(frm for frm in range(num_of_computers) if network[to][frm] and not frm in connected_computers)
        if not targets:
            return 

        for target in targets:
            connected_computers.add(target)
            infect(target)
        
    network = [[False for _ in range(num_of_computers)] for _ in range(num_of_computers)]
    
    set_network()  

    connected_computers = set([0])

    infect(0)

    print(len(connected_computers) - 1)

if __name__ == "__main__":
    run(int(read()), int(read()))