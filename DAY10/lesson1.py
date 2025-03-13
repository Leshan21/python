#Function with output

def format_name(f_name, l_name):
    # Docstring
    """Take first name and last name and format it to first letter in
    in each word to upper case"""
    return f"{f_name.title()} {l_name.title()}"
    
print(format_name("leshan", "pasindu"))    
    
    