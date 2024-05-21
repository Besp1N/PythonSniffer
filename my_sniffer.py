from scapy.all import sniff
from scapy.all import wrpcap


def sniff_packets(interface, count=10):
    print(f"Przechwytywanie pakietów z interfejsu {interface}...")

    packets = sniff(iface=interface, count=count)

    for packet in packets:
        print("----------- Pakiet -----------")
        print("Adres źródłowy:", packet.src)
        print("Adres docelowy:", packet.dst)
        print("Typ protokołu:", packet.payload.name)
        # Tutaj możesz dodać więcej informacji w zależności od potrzeb
        print("Zawartość:", packet.summary())  # Wyświetla krótkie podsumowanie pakietu
        print()

    save_packets_to_file(packets)


def save_packets_to_file(packets, filename="captured_packets.txt"):
    with open(filename, 'w') as file:
        for packet in packets:
            file.write("----------- Pakiet -----------\n")
            file.write(f"Adres źródłowy: {packet.src}\n")
            file.write(f"Adres docelowy: {packet.dst}\n")
            file.write(f"Typ protokołu: {packet.payload.name}\n")
            file.write("Zawartość: " + packet.summary() + "\n\n")
    print(f"Pakiety zapisane do pliku {filename}")
