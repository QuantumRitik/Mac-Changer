import subprocess
import optparse
import re

def mac_changer(interface, new_mac):
    print("[+] changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def get_argumets():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change its Mac address")
    parser.add_option("-m","--mac",dest="new_mac",help="new mac address")
    return parser.parse_args()

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface]).decode('ascii')
    print(ifconfig_result)

    mac_address_check_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_check_result:
        return mac_address_check_result.group(0)
    else:
        print("[+] could not get mac address [+]")


(options, argumets) = get_argumets()

mac_changer(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] mac address was successfully changed to " + current_mac)
else:
    print("[-] mac address did not changed")