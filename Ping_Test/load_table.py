
def ten_to_bin(num,count):
    num = bin(num).lstrip('0b')
    if len(num) != count:
        cont = count - len(num)
        num = cont * '0' + num
    return num

ip1=int(ten_to_bin(10,8)+ten_to_bin(0,8)+ten_to_bin(1,8)+ten_to_bin(1,8),2)
ip2=int(ten_to_bin(10,8)+ten_to_bin(0,8)+ten_to_bin(1,8)+ten_to_bin(2,8),2)

Ingress = bfrt.ping_test.pipe.Ingress
Ingress.clear()

Ingress.ipv4_host.add_with_send(ip1,8)
Ingress.ipv4_host.add_with_send(ip2,1)

Ingress.dump()
