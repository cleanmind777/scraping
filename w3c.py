# import requests
# import json

# # API endpoint
# url = "https://www.3cx.com/resellers/xcx-get-partners/"

# # Data to send in the POST request (as a dictionary)
# data = "country=JP&state=Select+a+State&name=&city="

# # Headers (optional, but often required for APIs)
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Cookie" : '_ga=GA1.1.1421741093.1741052793; _gcl_au=1.1.1016980924.1741052795; xcxWebVisitor={"Country":"JP","Continent":"ASIA","Region":"13","City":"?","CityL":"","Currency":"usd","Hosted":false}; __cf_bm=SS42s4D1xrZkB7Exz3QxtncfeaED3frv9._F5Iio2QU-1741063207-1.0.1.1-yLMrSGxriWQ5XzS4Po5UATH_w1WBzBBQ_429319DYlpUhCiTSIWJKJDUmF8Tm9Ssi59l.i6ax.KLIDVcFKKzK8hES3n80igXZ6zDV5TwV3g; _ga_742CBWE8D7=GS1.1.1741062604.2.1.1741063704.59.0.1649542971',
#     "Origin" : 'https://www.3cx.com',
#     "Referer" : 'https://www.3cx.com/ordering/find-reseller/',
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
#     'x-requested-with' : 'XMLHttpRequest'
# }

# # Send the POST request
# response = requests.post(url, data=data, headers=headers)

# # Check if the request was successful
# if response.status_code == 201:  # 201 means "Created" in HTTP
#     print("POST request successful!")
#     print("Response JSON:", response.json())
#     with open("response.txt", "w") as file:
#             file.write("Response Text:\n")
#             file.write(response.text) 
# else:
#     print(f"Failed to make POST request. Status code: {response.status_code}")
#     print("Response text:", response.text)


import csv
from bs4 import BeautifulSoup

# Sample HTML data (replace this with your actual HTML content)
html_data = """
<h3>
    3CX Platinum Partners <img src='data:image/png;base64,...' alt='Platinum Partners stars'/>
</h3>
<div class='xcx_partner_category_row'>
    <div class="xcx_partner_box">
        <div>
            <a href="https://www.3cx.com/reseller/pbx/hk/xin-jie/hong-kong-kwai-chung/g0kE1SB2dXOHh0HEPs9r14rkifCnXS4T7evZQ4uFlMw">
                <strong>Matrix Technology (HK) Ltd</strong>
            </a>
        </div>
        <div style="display:flex;">
            <span class="xcx_partners_icon">
                <i class="fas fa-phone-alt"></i>
            </span>
            +852 3900 1928
        </div>
        <div style="display:flex;">
            <span class="xcx_partners_icon">
                <i class="fas fa-link"></i>
            </span>
            <a rel="noopener nofollow" href="http://www.28voip.com" target="_blank">http://www.28voip.com</a>
        </div>
        <div style="display:flex;">
            <span class="xcx_partners_icon">
                <i class="fas fa-map-marker-alt"></i>
            </span>
            大連排道35號, Hong Kong, Kwai Chung 100025, 新界
        </div>
        <div style="display:flex;">
            <span>Partner ID:&nbsp;</span>
            202702
        </div>
    </div>
    <!-- Add more partner boxes here -->
</div>
<!-- Add more partner categories here -->
"""

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Define the CSV file name
csv_file = 'partners.csv'

# Open the CSV file for writing
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow([
        'Category', 'Name', 'Phone', 'Website', 'Address', 'Partner ID'
    ])
    
    # Extract and write partner data
    for category in soup.find_all('h3'):
        category_name = category.get_text(strip=True).replace('Partners', '').strip()
        
        for partner_box in category.find_next_sibling('div').find_all('div', class_='xcx_partner_box'):
            name = partner_box.find('strong').get_text(strip=True)
            phone = partner_box.find('span', class_='xcx_partners_icon').find_next_sibling(string=True).strip()
            website = partner_box.find('a', href=True)['href']
            address = partner_box.find('span', class_='xcx_partners_icon').find_next('i', class_='fa-map-marker-alt').find_next_sibling(string=True).strip()
            partner_id = partner_box.find(text='Partner ID:').find_next(string=True).strip()
            
            # Write the row to the CSV file
            writer.writerow([
                category_name, name, phone, website, address, partner_id
            ])