import argparse

# Import Mininet classes
from mininet.net import Mininet
from mininet.log import setLogLevel, info, debug
from mininet.cli import CLI
from mininet.node import Controller

# Create the argparser
parser = argparse.ArgumentParser(description="Mininet WAN Emulator")
parser.add_argument(
    "--bandwidth",
    "-b",
    dest="bw",
    required=False,
    default=1000,
    help="Define the Bandwidth on the links in Mbps (Example: 1000)",
    type=int,
)
parser.add_argument(
    "--delay",
    "-d",
    dest="delay",
    required=False,
    default=None,
    help="Define the Delay on the links in ms (Example 1)",
    type=int,
)
parser.add_argument(
    "--loss",
    "-l",
    dest="loss",
    required=False,
    default=None,
    help="Define the Loss on the links in percentage (Example 1)",
    type=int,
)

args = parser.parse_args()

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

    net.addLink(s1, h1, bw=args.bw, loss=args.loss, delay=args.delay)
    net.addLink(s1, h2, bw=args.bw, loss=args.loss, delay=args.delay)
    net.addLink(s2, h3, bw=args.bw, loss=args.loss, delay=args.delay)
    net.addLink(s2, h4, bw=args.bw, loss=args.loss, delay=args.delay)
    net.addLink(s3, s1, bw=args.bw, loss=args.loss, delay=args.delay)
    net.addLink(s3, s2, bw=args.bw, loss=args.loss, delay=args.delay)

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
