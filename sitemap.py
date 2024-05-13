import csv

data = list(csv.reader(open("trottermathURls.csv")))

priorityMap = {
    "Homepage": "1.00",
    "Activities with simple operations": "0.80",
    "Number Theory & Primes": "0.80",
    "Math with calculators": "0.80",
    "Activities involving recursive operations": "0.80",
    "Problem Solving": "0.80",
    "Solve Trotter's Own Problems (STOP) Math": "0.80",
    "Digital Expressions": "0.80",
    "Pythagorean Theorem": "0.80",
    "Games in Elementary Math": "0.80",
    "Number Trivia": "0.80",
    "Basic Algebra": "0.80",
    "Humor or items of lighthearted math": "0.60",
    "Personal and/or Miscellaneous": "0.80",
}

header = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset
  xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">"""

footer = "</urlset>"

print(header)
for row in data:
    item = "  <url>\n"
    item += "    <loc>" + row[1] + "</loc>\n"
    item += "    <lastmod>2024-05-13T10:49:42+00:00</lastmod>\n"
    item += "    <priority>" + priorityMap[row[0]] + "</priority>\n"
    item += "  </url>"
    print(item)
print(footer)
