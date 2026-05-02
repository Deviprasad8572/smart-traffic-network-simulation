#  Smart Traffic Network Simulation

##  Overview

This project implements a **Smart Traffic Network Simulation** using Python. It models how data packets travel across a network with **adaptive routing, congestion handling, retransmission (ARQ), and noise (AWGN channel)**.

The simulation is designed based on **network communication layers and QoS (Quality of Service) requirements**, making it suitable for academic projects and basic research in networking.

---

##  Objectives

* Simulate packet transmission in a smart network
* Implement **adaptive routing** based on congestion
* Model **packet delay, loss, and throughput**
* Apply **ARQ (Automatic Repeat Request)** for reliability
* Simulate **AWGN (Additive White Gaussian Noise)** channel
* Evaluate **QoS performance metrics**

---

##  Key Features

*  Multi-node network (Sensor → Routers → Server)
*  Smart path selection (least congestion routing)
*  Dynamic traffic load and congestion modeling
*  Retransmission mechanism (ARQ)
*  Performance metrics visualization using Matplotlib
*  AWGN noise simulation using NumPy

---

##  Network Architecture

Sensor → Router1 → Router2 → Server
            ↘ Router3 ↗

* Two possible paths
* System selects the **least congested path dynamically**

---

##  Technologies Used

* Python
* NumPy
* Matplotlib

---

##  Performance Metrics (KPI)

The simulation evaluates:

* **Packet Delivery Rate**
* **Packet Loss**
* **Average Delay (ms)**
* **Throughput (%)**

---

##  QoS Requirements

```python
Max Delay ≤ 15 ms  
Throughput ≥ 85%
```

---

##  Simulation Steps

1. Define application (Smart Factory IoT Network)
2. Configure network nodes and addresses
3. Select routing path dynamically
4. Transmit packets across the network
5. Apply ARQ for retransmission
6. Add AWGN noise to simulate real channel conditions
7. Measure performance metrics (KPI)
8. Validate QoS requirements

---

## How to Run

1. Install dependencies:

```bash
pip install numpy matplotlib
```

2. Run the script:

```bash
python simulation.py
```

---

##  Output

* Console logs showing packet delivery/loss
* Performance summary (delay, throughput, loss)
* Bar chart visualization of results

---

##  Example Output

```
Packets Sent: 100  
Packets Delivered: 92  
Packets Lost: 8  
Average Delay: 12.4 ms  
Throughput: 92%
```

---

##  Academic Relevance

This project demonstrates concepts from:

* Computer Networks
* Data Communication
* QoS Management
* Routing Algorithms
* Wireless Communication (AWGN)

---

##  Future Improvements

* AI-based routing (Reinforcement Learning)
* Real-time network visualization (NetworkX)
* Priority-based packet scheduling
* Bandwidth and buffer modeling
* Multi-hop large-scale network simulation

---

## Author
Banothu Devi prasad
Tejavath Bharatth Naik
Gampala Srinivas
Thurram Sandeep
Harshit
