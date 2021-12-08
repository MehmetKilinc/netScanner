import scapy.all as scapy
import optparse


def inputofuser():

	object = optparse.OptionParser()
	object.add_option("-i" , "--ip" , dest = "ip" , help = "enter ip adress")	
	return object.parse_args()

def netscanner(ip):

	request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	combined = broadcast/request
	(answered , unanswered) = scapy.srp(combined , timeout = 1)
	return answered.summary()

(inputs , arguments) = inputofuser()
ip = inputs.ip

if not inputs.ip:
	print("enter ip adres ")

netscanner(ip)

