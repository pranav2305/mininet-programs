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
    h4 = net.addHost("h4", ip="10.0.0.4")
    h5 = net.addHost("h5", ip="10.0.0.5")
    h6 = net.addHost("h6", ip="10.0.0.6")
    h7 = net.addHost("h7", ip="10.0.0.7")
    h8 = net.addHost("h8", ip="10.0.0.8")

    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")

    net.addLink(s1, s2 , intfName1 = "s1-eth1", intfName2 = "s2-eth2")

    net.addLink(s1, h1 , intfName1 = "s1-eth3", intfName2 = "h1-eth0")
    net.addLink(s1, h3 , intfName1 = "s1-eth2", intfName2 = "h3-eth0")
    net.addLink(s1, h5 , intfName1 = "s1-eth4", intfName2 = "h5-eth0")
    net.addLink(s1, h7 , intfName1 = "s1-eth5", intfName2 = "h7-eth0")

    net.addLink(s2, h2 , intfName1 = "s2-eth1", intfName2 = "h2-eth0")
    net.addLink(s2, h4 , intfName1 = "s2-eth3", intfName2 = "h4-eth0")
    net.addLink(s2, h6 , intfName1 = "s2-eth4", intfName2 = "h6-eth0")
    net.addLink(s2, h8 , intfName1 = "s2-eth5", intfName2 = "h8-eth0")

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
