import re

def cleanse(str):
    return str.replace("#", "").replace("*", "").strip().lower().replace(" ","-")
with open("notes.md", encoding="utf-8") as file:
    text = file.read()
    with open("Source\MD Rendering\\notes.bak", 'w', encoding="utf-8")  as backup_file:
        backup_file.write(text)
TOC_append = "# Table of Contents\n"
if TOC_append in text:
    text = text.replace(TOC_append, "")
    print("Removed existing TOC")
# Oh, scary regex!
regex_op = r"(^# +.*$)"
match_obj = re.findall(regex_op, text, re.MULTILINE)
if match_obj is None or len(match_obj) ==0:
    print("You must have at least one # header.")
    exit(0)
first_header = match_obj[0]
print("Identified first header: %s" % first_header)
remove_toc = text.split(first_header)[0]
text = text.replace(remove_toc, "")

readme_toc = TOC_append;

for str in match_obj[:]:
    new_str = "%s\n[← Return to Index](#%s)" % (str, cleanse(TOC_append))
    if not new_str in text:
        text = text.replace(str, new_str)
        print(new_str)
    else:
        print("There is already an index specifier for %s, great!"% str)

list_h1 = []
new_line_split = text.split("\n")
# Store a list of headers in order
header_dict = {}
for str in new_line_split:
    cleansed = cleanse(str)
    if str.startswith("# ") or str.startswith("## ") or str.startswith("### "):
        header_dict[str] = cleansed

for key,val in header_dict.items():
    output_str = "* [%s](#%s)" % (key.replace("#", "").strip(), val)
    readme_str = "* [%s](notes.md#%s)" % (key.replace("#", "").strip(), val)
    tab_count = key.count("#") - 1
    TOC_append += "\t" * tab_count + output_str + "\n"
    readme_toc += "\t" * tab_count + readme_str + "\n"
text = TOC_append + text

write_conf = input("Write to notes.md file?")
if write_conf.lower().startswith("y"):
    with open("notes.md",'w', encoding="utf-8") as output_file:
         output_file.write(text)

if input("Update README.md? ").strip().lower().startswith("y"):
    with open("readme.md", 'r+', encoding="utf-8") as readme_file:
        existing_text = readme_file.read()
        if "# Table of Contents" in existing_text:
            print("TOC Already Exists in README.md")
            existing_text = existing_text.split("# Table of Contents")[0].strip()
        updated_text = existing_text + "\n" + readme_toc
        readme_file.seek(0)
        readme_file.truncate()
        readme_file.write(updated_text)