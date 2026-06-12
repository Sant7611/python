# concepts: dict_merge, multiple_context_mgr, format, enumerate

# Create two dictionaries containing user data:
# user_details = {"name": "Jane Doe", "role": "Admin"}
# system_metadata = {"last_login": "2026-06-09", "role": "SuperAdmin", "id": 101}
# Merge these two dictionaries using the dictionary merge operator (|) in a way that the system_metadata overrides conflicting keys in user_details.
# Assume you have two text files: input.txt (containing multiple lines of raw data) and output.txt.
# Use a multiple context manager (with open(...) as f1, open(...) as f2:) to safely open both files at the same time.
# Loop through the lines of the input file using enumerate() to get line numbers. Write each line to the output file dynamically formatted using .format() or f-strings to include the id from your merged dictionary and the line number.

user_details = {"name": "Jane Doe", "role": "Admin"}
system_metadata = {"last_login": "2026-06-09", "role": "SuperAdmin", "id": 101}

updated_details = user_details | system_metadata
print(updated_details)
try:
    with(
        open('ch13/challenging_questions/challenge3/input.txt', 'r') as f1,
        open('ch13/challenging_questions/challenge3/output.txt', 'w') as f2
    ):
        content1 = f1.read() #thsi takes the cursor to the end.
        f1.seek(0)
        
        for line_no, line in enumerate(f1, start=1):
            f2.write(f"ID: {updated_details['id']} | Line {line_no}: {line}\n")
        
except Exception as e:
    print(e)

# try:
#     with open('ch13/challenging_questions/challenge3/input.txt', 'r') as f1, \
#          open('ch13/challenging_questions/challenge3/output.txt', 'w') as f2:

#         for line_no, line in enumerate(f1, start=1):
#             f2.write(f"ID: {updated_details['id']} | Line {line_no}: {line}")

# except Exception as e:
#     print(e)
with open('ch13/challenging_questions/challenge3/output.txt', 'r') as f3:
    contents = f3.read()
    f3.seek(0)
    print(contents)
