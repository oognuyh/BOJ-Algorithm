"""
    42583. 다리를 지나는 트럭
"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    def is_full():
        return current_bridge_weight + truck > weight

    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    current_bridge_weight = 0
    time = bridge_length

    while truck_weights:
        truck = truck_weights.popleft()

        if is_full():
            while is_full():
                current_bridge_weight -= bridge.popleft()
                bridge.append(0)
                time += 1
            
            bridge[-1] = truck
        else:
            current_bridge_weight -= bridge.popleft()
            bridge.append(truck)
            time += 1
        
        current_bridge_weight += truck

    return time