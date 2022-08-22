import requests
import os



urls = ['https://media.doterra.com/ru-otg/ru/ebooks/essential-oil-and-children.pdf?_ga=2.152647161.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/brochures/ebook-concentration-motivation.pdf?_ga=2.52032233.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/brochures/ebook-new-wellness-advocates.pdf?_ga=2.52032233.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/ebooks/cooking-with-essential-oils.pdf?_ga=2.52032233.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/flyers/essential-oil-recipes.pdf?_ga=2.143783413.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/ebooks/cuisine-blends-collection-cookbook.pdf?_ga=2.143783413.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/ebooks/100-uses-for-essential-oils.pdf?_ga=2.143783413.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/ebooks/essential-oils-and-sleep.pdf?_ga=2.119110345.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/ebooks/essential-oils-and-personal-care.pdf?_ga=2.119110345.1315934299.1658132663-1779979984.1658132663',
        'https://media.doterra.com/ru-otg/ru/ebooks/essential-oils-and-fitness.pdf?_ga=2.119110345.1315934299.1658132663-1779979984.1658132663'
        ]


output_dir = '/Users/bujikuh/Desktop/Books'

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        name = url.split('?')[0]
        file_path = os.path.join(output_dir, os.path.basename(name))
        with open(file_path, 'wb') as f:
            f.write(response.content)









