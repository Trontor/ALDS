import re

with open("notes.md", encoding="utf-8") as file:
    text = file.read()
    with open("Source\MD Rendering\\notes.bak", 'w', encoding="utf-8")  as backup_file:
        backup_file.write(text)
TOC_append = "# Table of Contents\n"
if TOC_append in text:
    text = text.replace(TOC_append, "")
    print("Removed existing TOC")
regex_op = r"(^# +.*$)"
match_obj = re.findall(regex_op, text, re.MULTILINE)
if match_obj is None or len(match_obj) ==0:
    print("You must have at least one # header.")
    exit(0)
first_header = match_obj[0]
print("Identified first header: %s" % first_header)
remove_toc = text.split(first_header)[0]
text = text.replace(remove_toc, "")
list_h1 = []
new_line_split = text.split("\n")
# Store a list of headers in order
header_dict = {}
for str in new_line_split:
    cleansed = str.replace("#", "").strip().lower().replace(" ","-")
    if str.startswith("# ") or str.startswith("## "):
        header_dict[str] = cleansed
for key,val in header_dict.items():
    output_str = "* [%s](#%s)" % (key.replace("#", "").strip(), val)
    tab_count = key.count("#") - 1
    TOC_append += "\t" * tab_count + output_str + "\n"
text = TOC_append + text

with open("notes.md",'w', encoding="utf-8") as output_file:
     output_file.write(text)