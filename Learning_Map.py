Learning_Map = {"Java" : "not_done" , "Python" : "not_done", "Ruby": "not_done"}

def add_skills(skills_dict):
	print(Learning_Map)

	new_skill = input("Add another skill: ")
	Learning_Map[new_skill] = "not_done"

	print(new_skill + " skill added!")
	print(Learning_Map)

add_skills(Learning_Map)