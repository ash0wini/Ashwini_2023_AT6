class DataValidator:
    def validate_data(self, input_list):
        valid_numbers = []
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                valid_numbers.append(int(item))
        print (valid_numbers)

class ListPrinter:
    def print_list(self, valid_numbers):
        print("Validated Numbers:", valid_numbers)