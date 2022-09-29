from dataclasses import field
from email import header
from email.base64mime import header_length
from ensurepip import version
from ipaddress import ip_address
import socket
import struct
import textwrap
class PacketSniffer():
    def packsniff(self, input_from_user):
        r = 1
        if r == 1:
            import platform
            my_os=platform.system()
            with open('myOS.txt','w') as file:
                file.writelines(str(my_os))
            with open('myOS.txt','r') as file:
                lines=file.read()
                first=lines.split('\n',1)[0]
                print(first)
                if(first=='Windows'):
                    print("This program cannot run on Windows, please try on Linux")
                else:
                    a = input("Do You want to start Packet Sniffer: (Y/N)")
                    if a == 'Y':
                        conn=socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
                    def ethernet_frame(data):
                        dest_mac, src_mac, protocal=struct.unpack('! 6s 6s H',data[:14])
                        return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(protocal), data[:14]
                    def get_mac_addr(bytes_addr):
                        bytes_str=map('{:02x}'.format, bytes_addr)
                        mac_addr=':'.join(bytes_str).upper()
                        return mac_addr
                    def ipv4_packet(data):
                        version_header_length=data[0]
                        version=version_header_length>>4
                        header_length=(version_header_length & 15)*4
                        ttl,protocal,src,target=struct.unpack('! 8x B B 2x 4s 4s',data[:20])
                        return version, header_length,ttl,protocal,ipv4(src),ipv4(target),data[header_length:]
                    def ipv4(addr):
                        return '.'.join(map(str,addr))
                    def icmp_packet(data):
                        icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
                        return icmp_type,code,checksum,data[4:]
                    def tcp_segment(data):
                        (src_port,dest_port,sequence, acknowledgement, offset_reserved_flags)=struct.unpack('! H H L L H',data[:14])
                        offset=(offset_reserved_flags >> 12)*4
                        flag_urg=(offset_reserved_flags & 32) >> 5
                        flag_ack=(offset_reserved_flags & 16) >> 5
                        flag_psh=(offset_reserved_flags & 8) >> 5
                        flag_rst=(offset_reserved_flags & 4) >> 5
                        flag_syn=(offset_reserved_flags & 2) >> 5
                        flag_fin=(offset_reserved_flags & 1)
                        return src_port,dest_port,sequence, acknowledgement, flag_urg, flag_rst, flag_fin, flag_ack, flag_psh, flag_syn, data[offset:]
                    def udp_segment(data):
                        src_port, dest_port, size=struct.unpack('! H H  2x H', data[:8])
                        return src_port, dest_port, size, data[8:]
                    def format_multi_line(prefix, string, size=80):
                        size -=len(prefix)
                        if isinstance(string, bytes):
                            string=''.join(r'\x[:02x'.format(byte) for byte in string)
                            if size%2:
                                size-=1
                        return  '\n'.join([prefix + line for line in textwrap.wrap(string,size)])


                    while True:
                        raw_data,addr=conn.recvfrom(65536)
                        dest_mac,src_mac, eth_protocal, data=   ethernet_frame(raw_data)
                        print("\n Ethernet Frame :")
                        print('Destination:{} Source:{}, Protocol:{}'.format(dest_mac,src_mac,eth_protocal))

                        if eth_protocal==8:
                            (version,header_length,ttl, protocal,  src,target,data)=ipv4_packet(data)
                            print("\n IPv4 Packets: ")
                            print('Version:{}, Header Length={}, TTL={}'.format(version, header_length, ttl))
                            print("Protocol: {}, Source:{}, Target:{}".format(protocal,src, target))

                            if protocal==1:
                                icmp_type,code, checksum, data=icmp_packet(data)
                                print("ICMP Packets: ")
                                print("ICMP Type:{}, Code:{}, CheckSum:{} ".format(icmp_type,code,checksum))
                            if protocal==6:
                                src_port,dest_port,sequence, acknowledgement, offset_reserved_flags,flag_ack,flag_urg, flag_syn,flag_fin, flag_psh,flag_rst=tcp_segment(ipv4.data)
                                print('TCP segment')
                                print("Source Port:{}, Destination Port:{}".format(src_port,dest_port))
                                print("Sequence: {} Acknowledgement:{}",sequence, acknowledgement)
                                print("offset_reserved_flags",offset_reserved_flags)
                                print("Flags: \n")
                                print("Flag ACK:{} Flag SYN:{} Flag URG:{} ".format(flag_ack, flag_syn, flag_urg))
                                print("Flag FIN:{}, Flag PSH:{}, Flag RST:{}".format(flag_fin,flag_psh,flag_rst))
                            if protocal==17:
                                udp=udp_segment(ipv4.data)
                                print("UDP Segment: ")
                                print("Source Port:{}, Destination Port:{}, Length:{}".format(udp.src_port, udp.dest_port,udp.size))


                
        else:
            r=2
