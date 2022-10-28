
# ==========================================

def main():
    data = load_data("C:/folder/data.dat")
    
    process_data(data)

    output_data(data)

# ==========================================

def load_data(filePath):
    data = read(filePath)
    return(data)

# ==========================================

def process_data(data):
    some_function(data)
    other_function(data)

# ==========================================

def output_data(data):
    write(data, "C:/folder/cleaned_data.dat")

# ==========================================
if __name__ == '__main__':
    main()