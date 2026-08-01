import os, re

base = r'C:\Users\kalem\OneDrive\Masaüstü\afz'
html_path = os.path.join(base, 'index.html')

with open(os.path.join(base, 'b64_logo.txt'), 'r', encoding='ascii') as f:
    b64_logo = f.read().strip().replace('\r','').replace('\n','')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Navbar logo icon (emoji 🧸) with <img> tag
# Old nav logo icon: <div class="nav-logo-icon">🧸</div>
new_nav_icon = f'<img src="data:image/jpeg;base64,{b64_logo}" class="nav-logo-icon" style="object-fit:cover; border-radius:12px;" alt="AFZ Oyuncak Logo">'
html = html.replace('<div class="nav-logo-icon">🧸</div>', new_nav_icon)

# Also update footer logo icon if exists
html = html.replace('<div class="nav-logo-icon">🧸</div>', new_nav_icon)

# Update style for .nav-logo-icon to fit image properly
html = html.replace('.nav-logo-icon {\n    width: 44px; height: 44px;', '.nav-logo-icon {\n    width: 50px; height: 50px;')

# Save updated index.html
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Also copy to AFZ_Oyuncak.html
with open(os.path.join(base, 'AFZ_Oyuncak.html'), 'w', encoding='utf-8') as f:
    f.write(html)

print("Logo updated successfully in HTML files!")
