Learning_Map = {"1" : "Java" , "2" : "Python", "3": "Ruby"}
def view_skills(Learning_Map):
	print(Learning_Map)

def add_skills(Learning_Map):
	calls = view_skills()
	return calls
	new_skill = input ("Add another skill: ")

	Learning_Map[new_skill] = not_done
print(view_skills(Learning_Map))