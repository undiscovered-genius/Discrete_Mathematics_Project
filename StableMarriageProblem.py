import collections

preferred_order_boy = {
	'A': 	['3', '2', '4', '1'],
	'B': 	['2', '1', '3', '4'],
	'C': 	['3', '1', '4', '2'],
	'D': 	['3', '1', '4', '2']
}

preferred_order_girl = {
	'1': 	['A', 'B', 'D', 'C'],
	'2': 	['C', 'A', 'D', 'B'],
	'3':  	['C', 'B', 'D', 'A'],
	'4':	['B', 'A', 'C', 'D'] 
}

boys_engage = []
girl_engage = []

free_boy = []
free_girl = []

def init_free_boy():
	
	for boy in preferred_order_boy.keys():
		free_boy.append(boy)

def init_free_girl():
	
	for girl in preferred_order_girl.keys():
		free_girl.append(girl)

def start_matching_boy(boy):

	for girl in preferred_order_boy[boy]:
		taken_match = [couple for couple in boys_engage if girl in couple]

		if (len(taken_match) == 0):
			boys_engage.append([boy, girl])
			free_boy.remove(boy)
			break

		elif (len(taken_match) > 0):
			current_guy = preferred_order_girl[girl].index(taken_match[0][0])
			potential_guy = preferred_order_girl[girl].index(boy)

			if (current_guy < potential_guy):
				pass
			else: 
				free_boy.remove(boy)
				free_boy.append(taken_match[0][0])
				taken_match[0][0] = boy
				break
def start_matching_girl(girl):

	for boy in preferred_order_girl[girl]:
		match_taken = [couple for couple in girl_engage if boy in couple]

		if (len(match_taken) == 0):
			girl_engage.append([girl, boy])
			free_girl.remove(girl)
			break

		elif (len(match_taken) > 0):
			current_girl = preferred_order_boy[boy].index(match_taken[0][0])
			potential_girl = preferred_order_boy[boy].index(girl)

			if (current_girl < potential_girl):
				pass
			else: 
				free_girl.remove(girl)
				free_girl.append(match_taken[0][0])
				match_taken[0][0] = girl
				break

def stable_matching_boy():
	while (len(free_boy) > 0):
		for boy in free_boy:
			start_matching_boy(boy)

def stable_matching_girl():
	while (len(free_girl) > 0):
		for girl in free_girl:
			start_matching_girl(girl)

def main():
	print("")
	stable_matching_boy()
	print(" Boy group is Proposing : ",boys_engage)
	print("")
	stable_matching_girl()
	print(" Girl group is Proposing : ",girl_engage)

init_free_boy()
print(" Boys : ",free_boy)
init_free_girl()
print(" Girls : ",free_girl)
print("\n\n")
print(" Preferred Order for Boys : \n")
for x,y in preferred_order_boy.items():
        print(x,y)
print("\n\n Preferred Order for Girls : \n")
for x,y in preferred_order_girl.items():
        print(x,y)
main()
print("")
girl_eng = []
for rlp in girl_engage:
        rlp.reverse()
        girl_eng.append(rlp)
girl_eng.sort()
boys_engage.sort()

if(boys_engage == girl_eng):
        print(" This Marriage Problem is STABLE")
else:        
        print(" This Marriage Problem is UNSTABLE")
