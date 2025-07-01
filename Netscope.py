import ipaddress

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 254:
        return "Class E (Experimental)"
    else:
        return "Invalid or Reserved"

def subnet_mask_to_cidr(mask):
    try:
        return ipaddress.IPv4Network(f"0.0.0.0/{mask}").prefixlen
    except ValueError:
        return None

def main():
    print("🔍 CIDR & IP Class Finder Tool")
    ip = input("Enter IP Address (e.g. 192.168.1.10): ")
    mask = input("Enter Subnet Mask (e.g. 255.255.255.0): ")

    try:
        ip_obj = ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        print("❌ Invalid IP address!")
        return

    cidr_prefix = subnet_mask_to_cidr(mask)
    if cidr_prefix is None:
        print("❌ Invalid Subnet Mask!")
        return

    print("\n📌 Results:")
    print(f"IP Address      : {ip}")
    print(f"Subnet Mask     : {mask}")
    print(f"CIDR Notation   : {ip}/{cidr_prefix}")
    print(f"IP Class        : {get_ip_class(ip)}")

if __name__ == "__main__":
    main()

