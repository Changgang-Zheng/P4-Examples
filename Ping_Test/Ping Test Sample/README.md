### How to do the ping test.

- Open the terminal windows, connect to the switch.
	- Compile the switch model: ping_test.p4 (the tools folder can be found: [tools](https://drive.google.com/file/d/1r2Azc8Uwsg1XAl1EuxKMiMgjM9FF68V7/view?usp=sharing))

		```
		cd bf-sde-9.2.0
		. ~/tools/set_sde.bash; sde
		~/tools/p4_build.sh ~/Documents/Ping Test Sample/ping_test.p4
		```

	- Run the switch model:

		```
		cd bf-sde-9.2.0
		. ~/tools/set_sde.bash; sde
		./run_switchd.sh -p ping_test
		```

	- Then, in the same window, activate swicth ports:
	
		```
		ucli
		port-del -/-
		port-add -/- 100G NONE
		an-set -/- 2
		port-enb -/-
		```
	- in the same window, load the table:


		```
		exit
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
		add_with_send(ip1,28)
		add_with_send(ip2,56)

		```

- Open the terminal windows.
  - Connect to the server02, Ping server01:
  
	```
	ping 10.0.1.1

	```
	- Or, connect to the server01, Ping server02:
	
	```
	ping 10.0.1.2

	```
