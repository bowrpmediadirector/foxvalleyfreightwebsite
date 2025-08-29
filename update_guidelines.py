import os
import re

# Path to your website folder
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
project_path = os.path.join(desktop, "ProfessionalWebsite")

# Path to guidelines page
guidelines_path = os.path.join(project_path, "guidelines.html")

# Navigation links (matches your site)
nav_links = """
<a href='index.html'>Home</a>
<a href='about-us.html'>About Us</a>
<a href='mods.html'>Mods</a>
<a href='team.html'>Team</a>
<a href='careers.html'>Careers</a>
<a href='terms-and-conditions.html'>Terms & Conditions</a>
<a href='content-creator.html'>Content Creator</a>
<a href='guidelines.html' class='active'>Guidelines</a>
<a href='official-media.html'>Official Media</a>
<a href='freight-we-offer.html'>Freight We Offer</a>
<a href='events-and-announcements.html'>Events & Announcements</a>
"""

# Full HTML content for guidelines
guidelines_content = f"""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>ATS Community Guidelines</title>
<link rel='stylesheet' href='css/style.css'>
</head>
<body>
<header>
<div class='container'>
<h1 class='logo'>My Professional ATS Website</h1>
<nav>
{nav_links}
</nav>
</div>
</header>

<main>
<section class='hero'>
<h1>ATS Community Guidelines</h1>
<p>To ensure a fun, safe, and respectful environment, all members must follow these guidelines.</p>
</section>

<section class='features'>
<div class='feature'>
<h2>1. Respect Everyone</h2>
<p>Treat all members with respect. Harassment, bullying, discrimination, or hate speech will not be tolerated. Comply with <a href='https://discord.com/terms' target='_blank'>Discord Terms of Service</a>.</p>
</div>
<div class='feature'>
<h2>2. No Cheating or Exploits</h2>
<p>Using mods or cheats to gain unfair advantage is prohibited. Comply with <a href='https://www.scssoft.com/tos' target='_blank'>SCS Software Terms of Service</a>.</p>
</div>
<div class='feature'>
<h2>3. Keep Channels Organized</h2>
<p>Use appropriate channels for topics and avoid spamming or off-topic posts.</p>
</div>
<div class='feature'>
<h2>4. Media & Content Sharing</h2>
<p>Share only appropriate content. No pirated software, mods, or illegal material.</p>
</div>
<div class='feature'>
<h2>5. No Self-Promotion</h2>
<p>Advertising other servers, services, or communities without permission is not allowed.</p>
</div>
<div class='feature'>
<h2>6. Voice Chat Etiquette</h2>
<p>Keep voice channels clear and respect all participants.</p>
</div>
<div class='feature'>
<h2>7. Roleplay & Convoy Guidelines</h2>
<p>Follow event rules and staff instructions. Avoid reckless behavior during events.</p>
</div>
<div class='feature'>
<h2>8. Modding & Customization</h2>
<p>Mods are allowed only if they do not break server rules or SCS TOS. Ask staff if unsure.</p>
</div>
<div class='feature'>
<h2>9. Safety & Personal Info</h2>
<p>Do not share personal information. Respect others’ privacy.</p>
</div>
<div class='feature'>
<h2>10. Reporting Issues</h2>
<p>Use designated channels to report rule violations or technical issues. Do not escalate publicly.</p>
</div>
<div class='feature'>
<h2>11. General Conduct</h2>
<p>Keep communication professional, avoid spam, and maintain a positive environment.</p>
</div>
<div class='feature'>
<h2>12. Consequences</h2>
<p>Infractions may result in warnings, timeouts, kicks, temp bans, or permanent bans depending on severity.</p>
</div>
</section>
</main>

<footer>
&copy; 2025 My Professional ATS Website
</footer>

<script src='js/script.js'></script>
</body>
</html>
"""

# Write/update the file
with open(guidelines_path, "w", encoding="utf-8") as f:
    f.write(guidelines_content)

print(f"✅ Guidelines page updated at {guidelines_path}")
