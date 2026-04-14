from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI
import time

class TrafficTopo(Topo):
    def build(self):
        # 1 switch, 4 hosts
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)

def run():
    setLogLevel('info')
    topo = TrafficTopo()
    net = Mininet(topo=topo,
                  controller=RemoteController('c0', ip='127.0.0.1', port=6633))
    net.start()
    print("\n=== Topology Ready: 1 Switch, 4 Hosts ===")
    print("Run your test scenarios in the CLI")
    print("Scenario 1: h1 ping h2  (normal traffic)")
    print("Scenario 2: iperf h1 h3  (bulk traffic measurement)")
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()