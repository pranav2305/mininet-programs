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
from mininet.node import RemoteController
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

        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        h3 = self.addHost("h3")
        h4 = self.addHost("h4")

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

    cwd = os.getcwd()

    info(" *** Creating Overlay Network Topology ***\n")
    # Create the topology object
    topo = SimpleTopology()
    ctl_ip, ctl_port = "127.0.0.1", None
    c1 = RemoteController("c1", ip=ctl_ip, port=ctl_port)
    net = Mininet(topo=topo, link=TCLink, controller=c1, autoSetMacs=True)
    net.start()
    info("*** Running CLI ***\n")
    CLI(net)


# Stop network functions
def stopNetwork():
    "Stops the network"

    if net is not None:
        info("*** Tearing down overlay network ***\n")
        net.stop()
        subprocess.run(["mn", "-c"])


# If run as a script
if __name__ == "__main__":
    # Force cleanup on exit by registering a cleanup function
    atexit.register(stopNetwork)
    # Print useful informations
    setLogLevel("info")
    # Start network
    startNetwork()
