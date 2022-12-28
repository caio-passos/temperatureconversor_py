# Initialize the stop condition and the temperature variable
stop_loop = False
result = 0

while not stop_loop:

    receive_celsius = input("\nInsert a temperature value number in Celsius to be converted to Fahrenheit: ")

    if receive_celsius.isdigit():

        receive_celsius = int(receive_celsius)

        if -100 <= receive_celsius <= 60:
            stop_loop = True

            result = (9 / 5) * receive_celsius + 32
    else:
        print("\nError! Please insert a valid numeric format")
        print("Invalid temperature: please type a numeric value between -100 and 60")

print("Current temperature inserted is:", result, "Fº")
