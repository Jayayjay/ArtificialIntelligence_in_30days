# Pyhton Flow COntrol

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    
except ValueError:
    #handles when the input can't be converted to an integer
    print("please enter a valid number")

except ZeroDivisionError as e:
    print(f"Cannot devide by zero! Error :{e}")

except Exception as e:
    # Catches any other exceptions not caught above
    print(f"An unexpected error occurred: {e}")

finally:
    print("Calculation attemot completed")
    
    
# Raising exceptions in user code
# Creating custom exception code
class InsufficientFundsError(Exception):
    pass

def withdraw_money(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise InsufficientFundsError("Not enough balance")
    return balance - amount
withdraw_money(1000, 900)


# Assertion statements for debugging and testing
def calculate_square_root(number):
    assert number >= 0, "Square root of negative number is underfined"
    return number ** .5

# Realistic Example
def process_user_data(filename):
    try:
        # Attempt to open and process the file
        with open(filename, 'r') as file:
            data = file.read()
            # Validate the data
            if len(data) == 0:
                raise ValueError("File is empty")
            # Process the data
            processed_data = data.upper()
            
            assert len(processed_data) == len(data), "Data lenght changed unexpectedly"
            return processed_data
    except FileNotFoundError:
        print(f"Could not find file: {filename}")
        # Logic to gain permission or use alternative location
        return None
    
    except Exception as e:
        # Log unexpected errors for debugging
        print(f"Unexoected Error: {e}")
        # Logic here
        return None
    
    finally:
        print("File processing attempt Completed")
        
""" Some key points
* more specific exceptions should come before more general ones
* Finally block is useful for cleanup operations that must happen regardless whether an exception occurred
* Custom exceptions should inherit from the exception class and typically go in a separate module if they are used accross multiple files
* Using raise with out and argument in an exception block with re-reise the caught exception """

""" try:
    risky_operation()
except:
    log_error("ValueError occurred")
    raise # Reraises the value error """