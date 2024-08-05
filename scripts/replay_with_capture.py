from scapy.all import rdpcap, sendp, sniff, wrpcap
import threading
def capture_responses(interface, timeout, output_file):
    packets = sniff(iface=interface, timeout=timeout)
    wrpcap(output_file, packets)
def replay_packets(pcap_file, iface):
    packets = rdpcap(pcap_file)

    capture_thread = threading.Thread(target=capture_responses, args=(iface, 60, '../captures/responses.pcapng'))
    capture_thread.start()

    # Replay the packets
    for packet in packets:
        sendp(packet, iface=iface)

    # Wait for the capture thread to finish
    capture_thread.join()
    

if __name__ == "__main__":
    replay_packets('../captures/capture1.pcapng', 'en0') 
