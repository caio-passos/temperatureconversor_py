# Initialize the stop condition and the temperature variable
stop_loop = False
receive_celsius = 0

# Prompt the user for input
while not stop_loop:
    # Print the message

    receive_celsius = input("\nInsert a temperature value number in Celsius to be converted to Fahrenheit: ")

    # Check if the input can be cast to an integer
    if receive_celsius.isdigit():
        # Cast the input to an integer
        receive_celsius = int(receive_celsius)

        # Check if the temperature value is within the valid range
        if -100 <= receive_celsius <= 60:
            # Set the flag to True and exit the loop
            stop_loop = True
    else:
        print("\nError! Please insert a valid numeric format")
        print("Invalid temperature: please type a numeric value between -100 and 60")

# Print the current temperature
print("Current temperature inserted is:", receive_celsius, "Cº")
