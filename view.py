def add_studied_skills(skills_dict):
	user_input = input("Enter skill studied:")
	for key, value in skills_dict.items():
		if user_input == key:
			skills_dict[user_input] = "done"
			print(user_input + "skills studied!")