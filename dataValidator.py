class DataValidator:
    def validate_data(self, input_list):
        valid_numbers = []
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                valid_numbers.append(int(item))
        return valid_numbers
