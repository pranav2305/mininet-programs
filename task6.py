# Import Mininet classes
from mininet.net import Mininet
from mininet.log import setLogLevel, info, debug
from mininet.cli import CLI
from mininet.node import Controller

# Start network functions
def startNetwork():
    "Creates and starts the network"
    net = Mininet(controller=Controller, waitConnected=True)
    c0 = net.addController("c0")
    h1 = net.addHost("h1", ip="10.0.0.1")
    h2 = net.addHost("h2", ip="10.0.0.2")
    h3 = net.addHost("h3", ip="10.0.0.3")

    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")

    net.addLink(s1, s2 , intfName1 = "s1-eth1", intfName2 = "s2-eth1")
    net.addLink(s1, h1 , intfName1 = "s1-eth2", intfName2 = "h1-eth0")
    net.addLink(s1, h2 , intfName1 = "s1-eth3", intfName2 = "h2-eth0")
    net.addLink(s2, h3 , intfName1 = "s3-eth2", intfName2 = "h3-eth0")

    net.build()
    c0.start()
    net.start()
    info("*** Running CLI ***\n")
    CLI(net)
    info("*** Stopping network ***\n")
    net.stop()


# If run as a script
if __name__ == "__main__":
    # Print useful informations
    setLogLevel("info")
    # Start network
    startNetwork()
