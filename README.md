#  Smart Factory Network Simulation

##  Overview

This project simulates **packet transmission in a Smart Factory communication network** using Python. It models real-world networking conditions such as delay, packet loss due to noise, and throughput between industrial devices like sensors, robots, cameras, and a central server.

The purpose of this simulation is to analyze network performance and understand Quality of Service (QoS) in industrial automation systems.

---

##  Objectives

- Simulate communication between smart factory devices
- Analyze packet transmission performance
- Measure network delay and throughput
- Study packet loss under noisy conditions
- Visualize network performance using graphs

---

##  Devices in Simulation

| Device | IP Address |
|--------|------------|
| Sensor | 192.168.1.1 |
| Robot | 192.168.1.2 |
| Camera | 192.168.1.3 |
| Server | 192.168.1.10 |

---

##  Features

- Simulates 100 packets transmission  
- Random delay between 1 ms to 10 ms  
- Noise-based packet loss (10%)  
- Real-time packet delivery logs  
- Throughput calculation  
- Average delay measurement  
- Graphical output using Matplotlib  

---

##  Performance Metrics

- **Packets Sent** – Total transmitted packets  
- **Packets Received** – Successfully delivered packets  
- **Packets Lost** – Dropped packets due to noise  
- **Average Delay** – Mean packet delay  
- **Throughput** – Delivery success percentage  

---

##  Sample Output

```text
Packets Sent: 100
Packets Received: 88
Packets Lost: 12
Average Delay: 5.44 ms
Throughput: 88.0 %

## Requirements


Python 3.x

Matplotlib

## Installation
pip install matplotlib

## How to Run
python main.py

## Project Structure
smart-factory-network/├── main.py├── README.md├── Figure_1.png

## Output Graph
The program generates a bar chart showing:


Packets Received


Packets Lost


## Concepts Used


Computer Networks


Packet Switching


QoS Metrics


Delay Analysis

Throughput Calculation

Industrial IoT Communication

## Customization
You can modify these values in main.py:


packets_sent → Number of packets


noise > 0.1 → Packet loss probability


random.uniform(1,10) → Delay range


time.sleep(0.02) → Simulation speed



## Team Members


- Deviprasad
- Srinivas
- Sandeep




