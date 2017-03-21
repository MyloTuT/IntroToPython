#!/usr/bin/python3

sites_pages = {
    'example.com': [
        'index.html',
        'about_us.html',
        'contact_us.html'
    ],
    'something.com': [
        'index2.html',
        'prizes.html',
        'puppies.html',
    ],
    'whateva.com': [
        'main.html',
        'getting.html',
        'setting.html',
    ],
}

for lines in sites_pages:
    print(lines)
    print(sites_pages[lines][0])
    print(sites_pages[lines][1])
    print(sites_pages[lines][2], '\n')
