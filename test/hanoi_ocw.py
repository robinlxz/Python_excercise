


def Hanoi(n,F,T,S):
	""" From/To/Spare """
	if n == 1:
		print 'move 1 disk from ' + F + ' to ' + T
	else:
		Hanoi(n-1,F,S,T)
		Hanoi(1,F,T,S)
		Hanoi(n-1,S,T,F)







1. Flat ping has no packet loss. 
2. Telnet to 7000 port will have response immedieatly. 
3. By tcpdump, the connection is established very fast. But the service is not repond in time. 
4. Because the redis service have multiple instance, and port 7000 is a redis proxy. As we don't know the detail for this proxy, we cannot further check the service side.
Based on above checking, the problem is not on network side.


redis-cli -h 10.84.128.36 -p 7000 -a duuZZU2rrqp7m7pr --scan --pattern sess:*