import os

def create_test_directory(base_dir="test"):
    # Create the base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create the .cache, .tmp, and .log files
    cache_file = os.path.join(base_dir, "test.cache")
    tmp_file = os.path.join(base_dir, "test.tmp")
    log_file = os.path.join(base_dir, "test.log")
    
    with open(cache_file, "w") as f:
        f.write("This is a .cache file.")
    
    with open(tmp_file, "w") as f:
        f.write("This is a .tmp file.")
    
    with open(log_file, "w") as f:
        f.write("This is a .log file.")

    # Create directories tmp and .cache
    tmp_dir = os.path.join(base_dir, "tmp")
    cache_dir = os.path.join(tmp_dir, ".cache")
    
    os.makedirs(tmp_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)

    # Create files that should NOT be removed
    txt_file = os.path.join(base_dir, "file.txt")
    pdf_file = os.path.join(base_dir, "document.pdf")
    
    with open(txt_file, "w") as f:
        f.write("This is a text file that should not be removed.")
    
    with open(pdf_file, "w") as f:
        f.write("This is a PDF file that should not be removed.")
    
    print(f"Test directory '{base_dir}' initialized with test files and folders.")

create_test_directory()

