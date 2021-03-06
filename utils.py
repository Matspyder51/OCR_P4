def to_boolean(value):
	if type(value) == str and value.lower() == "y":
		return True

	if type(value) == int and value == 1:
		return True

	return False

def ask_data(message: str, data_condition: list):
	result = input(message)

	try:
		if data_condition.count(result) > 0:
			return result
		else:
			return ask_data(message, data_condition)
	except ValueError:
		return ask_data(message, data_condition)