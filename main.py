from scapy.all import sniff
import threading
import sys


def packet_callback(packet):
    ip_layer = packet.getlayer("IP")
    if ip_layer:
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto_num = ip_layer.proto
        proto_name = ip_layer.get_field("proto").i2repr(ip_layer, proto_num)
        print(f"Źródło: {src_ip} -> Cel: {dst_ip} | Protokół: {proto_name}")


def start_sniffing():
    sniff(iface="en0", prn=packet_callback)


def main():
    sniff_thread = threading.Thread(target=start_sniffing)
    sniff_thread.daemon = True
    sniff_thread.start()
    input("Naciśnij Enter, aby zakończyć...")
    sys.exit()


if __name__ == "__main__":
    main()
