import random

def transmit_packet(path, traffic_load, physical_layer):
    total_delay = 0

    for i in range(len(path)-1):
        link = (path[i], path[i+1])

        base_delay = random.uniform(1,5)
        delay = physical_layer.transmit_signal(base_delay, traffic_load[link])

        total_delay += delay

        # increase congestion
        traffic_load[link] += 0.05

        # packet loss condition
        if traffic_load[link] > 3 and random.random() < 0.2:
            return False, total_delay

    return True, total_delay


def arq_transmission(path, traffic_load, physical_layer):
    delivered, delay = transmit_packet(path, traffic_load, physical_layer)

    # retry once
    if not delivered:
        delivered, delay = transmit_packet(path, traffic_load, physical_layer)

    return delivered, delay
