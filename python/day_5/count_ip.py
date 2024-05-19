# Let's convert IP address to decimal by converting it to binary 
# after calculating decimal for both of the IP addresses 
# subtrract them 



def ip_to_decimal(ip):
    octets = ip.split('.')

    decimal = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + (int(octets[3]))

    return decimal



def ips_between(start, end):
    

    print(ip_to_decimal(end) - ip_to_decimal(start))








ips_between("10.0.0.0", "10.0.0.50")
# ("20.0.0.10", "20.0.1.0")