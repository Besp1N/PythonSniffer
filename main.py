from scapy.all import sniff, get_if_list


def get_interfaces():
    interfaces = get_if_list()
    return interfaces


def packet_callback(packet):
    if packet.haslayer("IP") and packet.haslayer("TCP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        sport = packet["TCP"].sport
        dport = packet["TCP"].dport
        if packet.haslayer("Raw"):
            payload = packet["Raw"].load
        else:
            payload = None

        print("Packet Info:")
        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}")
        print(f"Source Port: {sport}, Destination Port: {dport}")
        if payload:
            print("Payload:")
            print(payload)
        print("\n")


def main():
    interfaces = get_interfaces()
    print("Available interfaces:")
    for i, interface in enumerate(interfaces, start=1):
        print(f"{i}. {interface}")

    choice = input("Choose an interface by number: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(interfaces):
            print("Invalid choice!")
            return
    except ValueError:
        print("Invalid choice!")
        return

    chosen_interface = interfaces[choice - 1]
    print(f"Sniffing on interface: {chosen_interface}")

    sniff(iface=chosen_interface, prn=packet_callback, store=0)


if __name__ == "__main__":
    main()
