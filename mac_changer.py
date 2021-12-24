#!/usr/bin/env python

#import subprocess
#subprocess.call("ifconfig", shell=True)

#if we input normally user input for Interface and MAC address then we should run this program on python3
#if we want to run on python 2.7 then we should type raw_input instead of input
import subprocess
import optparse
import re

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to : " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

#optparser use tho collect function that we want to use . and OptionParser() is a class that use to handle all function and we can add function and pass its option and argument and we can easily use this by command
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to Change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify an interface, use --help for more info.")
    return  options
#interface = options.interface
#new_mac = options.new_mac

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Couldn't read the mac address!")

#this process have a hazard becuse hacker can interupt our program by shell command so we should use list because in shell command 1st item are check so they can't easily run shell command
#subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up", shell=True)
options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was sucessfully changed to " + current_mac)
else:
    print("[-] MAC address did not get Changed.")