import atexit
import argparse
import logging
import subprocess
import os
import random

# Import Mininet classes
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel, info, debug
from mininet.cli import CLI
from mininet.node import RemoteController, Controller
from mininet.util import irange

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

# Global vars
net = None

# Define the topology class
class SimpleTopology(Topo):
    """Simple Mininet Topology"""

    def __init__(self, **opts):

        # Initialize object argument
        super(SimpleTopology, self).__init__(*opts)
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")
        s3 = self.addSwitch("s3")

        h1 = self.addHost("h1", ip="10.0.0.1")
        h2 = self.addHost("h2", ip="10.0.0.2")
        h3 = self.addHost("h3", ip="10.0.0.3")
        h4 = self.addHost("h4", ip="10.0.0.4")

        self.addLink(s1, h1, bw=args.bw, loss=args.loss, delay=args.delay)
        self.addLink(s1, h2, bw=args.bw, loss=args.loss, delay=args.delay)
        self.addLink(s2, h3, bw=args.bw, loss=args.loss, delay=args.delay)
        self.addLink(s2, h4, bw=args.bw, loss=args.loss, delay=args.delay)
        self.addLink(s3, s1, bw=args.bw, loss=args.loss, delay=args.delay)
        self.addLink(s3, s2, bw=args.bw, loss=args.loss, delay=args.delay)


# Start network functions
def startNetwork():
    "Creates and starts the network"

    global net
    info(" *** Creating Overlay Network Topology ***\n")

    # Create the topology object
    topo = SimpleTopology()
    net = Mininet(topo=topo, link=TCLink, controller=Controller, autoSetMacs=True)
    net.addController("c0")
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
