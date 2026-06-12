#Write a fully type-hinted function called process_readings that accepts a list of strings (representing temperature readings) and returns a list of integers

# Iterate through the items. Use a try...except block to attempt to convert each string to an integer. If it cannot be converted, catch the ValueError and skip it.
# Manually raise a custom exception (or ValueError) with a message if an extracted temperature is below 0, taking priority over saving it.
# Bonus: Try to accomplish as much of the filtering/assignment as possible using the walrus operator (:=) to capture the converted integer immediately.

readings = ["34", "invalid", "102", "-5", "45", "error"]

def process_reading(readings: list[str])->list[int]:
    result : list[int] = []
    for i in readings:
        if isInt(i) is not None:
            result.append(int(i))
        
    return result
        

def isInt(num:str)->str:
    try:
        if int(num):
            return (num)
        else:
            raise ValueError("this is not a valid integer value. ")
    except:
        return None


filtered = process_reading(readings)
print(filtered)


#solved : 
readings = ["34", "invalid", "102", "-5", "45", "error"]

def process_reading(readings: list[str]) -> list[int]:
    result: list[int] = []
    
    for item in readings:
        try:
            # We use the walrus operator to assign AND check the converted int
            temp = int(item)
            
            if temp < 0:
                # Requirement: Raise a custom exception for negatives!
                raise ValueError(f"Temperature cannot be less than 0! Found: {temp}")
                
            result.append(temp)
            
        except ValueError as e:
            # This triggers for both invalid strings (like "invalid") AND our negative raise
            print(f"Skipping -> {e}")
            
    return result

filtered = process_reading(readings)
print(f"Valid outcomes: {filtered}")