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

    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")
    s3 = net.addSwitch("s3")

    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(s3, s1)
    net.addLink(s3, s2)

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
