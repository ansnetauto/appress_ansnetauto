import difflib

# File names variables
file01 = "httpd.conf .bak"
file02 = "httpd.conf"

# Read the contents of the first file
with open(f'./{file01}', 'r') as f1:
    file1_contents = f1.readlines()

# Read the contents of the second file
with open(f'./{file02}', 'r') as f2:
    file2_contents = f2.readlines()

# Compute the differences between the files with PEP8 column with of 79
differences = difflib.HtmlDiff(wrapcolumn=79).make_file(file1_contents, file2_contents)

# Write the differences to an HTML file
with open(f'./{file01}_{file02}_compared.html', 'w') as html_file:
    html_file.write(differences)
