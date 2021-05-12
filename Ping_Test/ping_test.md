1. Setup environment variables.
	
	```
	sudo su
	cd /root/bf-sde-9.2.0
	source /root/tools/set_sde.bash
	``` 
2. Compile the sample program.
	
	```
	cd $SDE
	/root/tools/p4_build.sh /root/tools/p4_build.sh /root/Documents/Experiment/ping_test/ping_test.p4
	``` 
3. Run the driver.
	
	```
	./run_switchd.sh -p ping_test
	``` 
4. Load the table:

	```
	./run_bfshell.sh -b file_address of load_table.py
	
	port-del -/-
	port-add -/- 100G NONE
	an-set -/- 2
	port-enb -/-
	``` 
		
	```
	bfrt_python
	bfrt.ping_test.pipe.Ingress.ipv4_host
	
	def ten_to_bin(num,count):
	    num = bin(num).lstrip('0b')
    	if len(num) != count:
            cont = count - len(num)
            num = cont * '0' + num
    	return num

	ip1=int(ten_to_bin(10,8)+ten_to_bin(0,8)+ten_to_bin(1,8)+ten_to_bin(1,8),2)
	ip2=int(ten_to_bin(10,8)+ten_to_bin(0,8)+ten_to_bin(1,8)+ten_to_bin(2,8),2)
	add_with_send(ip1,8)
	add_with_send(ip2,1)
	``` 
	
5. Ping server02 on server01.
	
	```
	changgang@nserver01x:~$ ping 10.0.1.2
	PING 10.0.1.2 (10.0.1.2) 56(84) bytes of data.
	From 10.0.1.1 icmp_seq=1 Destination Host Unreachable
	From 10.0.1.1 icmp_seq=2 Destination Host Unreachable
	From 10.0.1.1 icmp_seq=3 Destination Host Unreachable
	From 10.0.1.1 icmp_seq=4 Destination Host Unreachable
	From 10.0.1.1 icmp_seq=5 Destination Host Unreachable
	From 10.0.1.1 icmp_seq=6 Destination Host Unreachable
	``` 
5. Use scapy to do the test.

	```
	p = sniff(count=1, filter = "ip src 10.0.1.1", iface="enp175s0f1")
       
	p = Ether(type="IPv4") / IP(dst="10.0.1.2")
	sendp(p, iface="eth5")
	```
