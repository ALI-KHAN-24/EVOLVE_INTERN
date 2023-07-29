import requests

def shorten_link(full, link):
    API_KEY ='7a01a64fda21ae91f17920a5e29de71805daf'
    BASE_URL ='https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full, 'name': link}
    response = requests.get(BASE_URL, params=payload)
    data = response.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink'] 

        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)

link = input('Enter a link:>>')
name = input('Give your link a name:>>')

shorten_link(link, name)
