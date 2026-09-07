import glob
import os

patch_snippet = """    # Prevent createsuperuser from suggesting default username
    try:
        import django.contrib.auth.management.commands.createsuperuser as csu
        csu.get_default_username = lambda database="default": ""
    except Exception:
        pass

    try:
        from django.core.management import execute_from_command_line"""

target_snippet = """    try:
        from django.core.management import execute_from_command_line"""

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
for root, dirs, files in os.walk(parent_dir):
    if "manage.py" in files:
        file_path = os.path.join(root, "manage.py")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "csu.get_default_username" in content:
            print(f"Already patched: {file_path}")
        elif target_snippet in content:
            content = content.replace(target_snippet, patch_snippet)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully patched: {file_path}")
        else:
            print(f"Target snippet not found: {file_path}")

# Also update Program 11 readme.txt if default credentials are listed
p11_readme = os.path.join(parent_dir, "Program 11", "readme.txt")
if os.path.exists(p11_readme):
    with open(p11_readme, "r", encoding="utf-8") as f:
        r_content = f.read()
    old_text = """   Default Credentials (or use your newly created account):
   - Username: admin
   - Password: admin123"""
    new_text = "   Log in using the Username and Password you created in Step 3."
    if old_text in r_content:
        r_content = r_content.replace(old_text, new_text)
        with open(p11_readme, "w", encoding="utf-8") as f:
            f.write(r_content)
        print("Updated Program 11 readme.txt")
