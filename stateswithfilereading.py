
with open("statespyclass.csv", "r") as states_file:		
		states = states_file.read().split("\n")

		for index, state in  enumerate(states):
				states[index] = state.split(",")

		print "<select= name='states'>"

		for state in states:
			print """\n \t <option value= "{0}">"{1}"</option> \n""" .format(state[0], state[1]) 

print "</select>"

