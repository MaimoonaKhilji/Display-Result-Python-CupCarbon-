import time
while node.loop():
	node.mark()
	node.print("On")
	time.sleep(1)

	node.unmark()
	node.print("Off")
	time.sleep(1)
