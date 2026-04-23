import random
import time
import matplotlib.pyplot as plt

# Devices
devices = {
    "Sensor": "192.168.1.1",
    "Robot": "192.168.1.2",
    "Camera": "192.168.1.3",
    "Server": "192.168.1.10"
}

packets_sent = 100
packets_received = 0
packets_lost = 0
delays = []

print("Smart Factory Network Simulation Started\n")

for i in range(packets_sent):

    delay = random.uniform(1, 10)   # ms
    noise = random.random()

    time.sleep(0.02)

    if noise > 0.1:     # 90% success
        packets_received += 1
        delays.append(delay)
        print(f"Packet {i+1} Delivered | Delay = {round(delay,2)} ms")
    else:
        packets_lost += 1
        print(f"Packet {i+1} Lost due to Noise")

avg_delay = sum(delays) / len(delays)
throughput = packets_received / packets_sent * 100

print("\n--- RESULTS ---")
print("Packets Sent:", packets_sent)
print("Packets Received:", packets_received)
print("Packets Lost:", packets_lost)
print("Average Delay:", round(avg_delay,2), "ms")
print("Throughput:", round(throughput,2), "%")

# Graph
labels = ['Received', 'Lost']
values = [packets_received, packets_lost]

plt.bar(labels, values)
plt.title("Network Packet Performance")
plt.show()
