import random
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# STEP 1: Application + QoS
# -----------------------------
application = "Smart Factory IoT Network"

QOS = {
    "max_delay": 15,   # ms
    "min_throughput": 85  # %
}

print(f"\nApplication: {application}")
print(f"QoS Requirements: {QOS}\n")

# -----------------------------
# STEP 2 & 3: Nodes + Addresses
# -----------------------------
devices = {
    "Sensor": "192.168.1.1",
    "Router1": "192.168.1.2",
    "Router2": "192.168.1.3",
    "Router3": "192.168.1.4",
    "Server": "192.168.1.10"
}

# -----------------------------
# Network Paths (Routing)
# -----------------------------
paths = [
    ["Sensor", "Router1", "Router2", "Server"],
    ["Sensor", "Router1", "Router3", "Server"]
]

# Traffic load (for congestion)
traffic_load = {
    ("Sensor","Router1"): 1,
    ("Router1","Router2"): 1,
    ("Router1","Router3"): 1,
    ("Router2","Server"): 1,
    ("Router3","Server"): 1
}

# -----------------------------
# STEP 7: AWGN Channel
# -----------------------------
def awgn_noise():
    return np.random.normal(0, 1)  # Gaussian noise

# -----------------------------
# STEP 4: Smart Routing
# -----------------------------
def choose_best_path():
    load1 = traffic_load[("Router1","Router2")] + traffic_load[("Router2","Server")]
    load2 = traffic_load[("Router1","Router3")] + traffic_load[("Router3","Server")]
    
    return paths[0] if load1 < load2 else paths[1]

# -----------------------------
# STEP 5: ARQ (Retransmission)
# -----------------------------
def transmit_packet(path):
    total_delay = 0
    
    for i in range(len(path)-1):
        link = (path[i], path[i+1])
        
        # Base delay + congestion + noise
        base_delay = random.uniform(1,5)
        noise = abs(awgn_noise())
        delay = base_delay * traffic_load[link] + noise
        
        total_delay += delay
        
        # Increase congestion
        traffic_load[link] += 0.05
        
        # Packet loss condition
        if traffic_load[link] > 3 and random.random() < 0.2:
            return False, total_delay
    
    return True, total_delay

# -----------------------------
# Simulation
# -----------------------------
packets = 100
success = 0
loss = 0
delays = []

print("Smart Network Simulation Started\n")

for i in range(packets):
    
    path = choose_best_path()
    
    delivered, delay = transmit_packet(path)
    
    # ARQ: retry once if failed
    if not delivered:
        print(f"Packet {i+1} Lost → Retrying...")
        delivered, delay = transmit_packet(path)
    
    if delivered:
        success += 1
        delays.append(delay)
        print(f"Packet {i+1} Delivered via {path} | Delay = {round(delay,2)} ms")
    else:
        loss += 1
        print(f"Packet {i+1} Failed after retry")

# -----------------------------
# STEP 8: KPI Evaluation
# -----------------------------
avg_delay = sum(delays)/len(delays) if delays else 0
throughput = (success/packets)*100

print("\n--- RESULTS ---")
print("Packets Sent:", packets)
print("Packets Delivered:", success)
print("Packets Lost:", loss)
print("Average Delay:", round(avg_delay,2), "ms")
print("Throughput:", round(throughput,2), "%")

# QoS Check
print("\n--- QoS STATUS ---")
if avg_delay <= QOS["max_delay"]:
    print("✔ Delay Requirement Met")
else:
    print("✘ Delay Requirement NOT Met")

if throughput >= QOS["min_throughput"]:
    print("✔ Throughput Requirement Met")
else:
    print("✘ Throughput Requirement NOT Met")

# -----------------------------
# Graph
# -----------------------------
labels = ["Delivered", "Lost"]
values = [success, loss]

plt.bar(labels, values)
plt.title("Smart Traffic Network Performance")
plt.xlabel("Status")
plt.ylabel("Packets")
plt.show()
