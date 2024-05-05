from scapy.all import sniff


def sniff_packets(interface, count=10):
    print(f"Przechwytywanie pakietów z interfejsu {interface}...")

    # Wywołanie funkcji sniff() z podanym interfejsem i liczbą pakietów do przechwycenia
    packets = sniff(iface=interface, count=count)

    for packet in packets:
        print("----------- Pakiet -----------")
        print("Adres źródłowy:", packet.src)
        print("Adres docelowy:", packet.dst)
        print("Typ protokołu:", packet.payload.name)
        # Tutaj możesz dodać więcej informacji w zależności od potrzeb
        print("Zawartość:", packet.summary())  # Wyświetla krótkie podsumowanie pakietu
        print()
