#Challenge 4: The Global Modifier
# Concepts: global, importingfrom_module_file, module

# Create a variable called execution_count = 0 at the top level of a file.
# Write a function run_task() that increments this global variable every time it is called.

execution_count = 0

def run_task():
    global execution_count
    execution_count +=1
    return execution_count

print(run_task())
print(run_task())
print(run_task())
print(run_task())