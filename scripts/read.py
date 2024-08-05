import pyshark

def extract_packets(pcap_file, request_file, response_file, port):
    # Read the pcap file
    cap = pyshark.FileCapture(pcap_file, display_filter=f'tcp.port == {port}')
    
    with open(request_file, 'w') as req_file, open(response_file, 'w') as res_file:
        for packet in cap:
            # Check if the packet is a request or response
            if 'HTTP' in packet:
                # HTTP request packets typically have the field http.request
                if 'http.request' in packet.http.field_names:
                    req_file.write(str(packet) + '\n')
                # HTTP response packets typically have the field http.response
                elif 'http.response' in packet.http.field_names:
                    res_file.write(str(packet) + '\n')
    
    cap.close()

# Specify the paths to your files
pcap_file = 'path_to_your_pcap_file.pcap'
request_file = 'requests.txt'
response_file = 'responses.txt'
port = 8085

extract_packets(pcap_file, request_file, response_file, port)
