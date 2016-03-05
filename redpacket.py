from random import randint

redpacket_number = int(raw_input('number of redpackets:'))
current_redpacket_number = redpacket_number
total_redpacket_amount = int(raw_input('total amount:'))
current_redpacket_amount = total_redpacket_amount
redpacket_taken_number = 1
max_amount = current_redpacket_amount / current_redpacket_number

while redpacket_taken_number < redpacket_number:
	money_taken = randint(1, max_amount)
	current_redpacket_amount = current_redpacket_amount - money_taken
	print "%d/%d redpacket are taken" % (redpacket_taken_number, redpacket_number)
	print "Congrats! you got %d RMB" % money_taken
	redpacket_taken_number += 1
	current_redpacket_number -= 1
	max_amount = current_redpacket_amount / current_redpacket_number


money_taken = current_redpacket_amount 
print "This is the last redpacket"
print "Congrats! you got %d RMB" % money_taken
