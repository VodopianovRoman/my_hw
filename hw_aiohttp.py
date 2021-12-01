from aiohttp import web
import asyncio
import aiohttp
import datetime
import ssl
import json
import pprint

api_dict = {
    'chuk_api': {
        'url': "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random",
        'headers': {'accept': "application/json",
                    'x-rapidapi-key': "2f3130e1d0msh00771bcd8dd1c6ep1e7046jsnc993e624bbf3",
                    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"}
    },
    'pokemon_api': {
        'url': "https://pokemon-go1.p.rapidapi.com/pokemon_stats.json",
        'headers': {'x-rapidapi-key': "2f3130e1d0msh00771bcd8dd1c6ep1e7046jsnc993e624bbf3",
                    'x-rapidapi-host': "pokemon-go1.p.rapidapi.com"}
    },
    'flight_data_api': {
        'url': "https://dev132-cricket-live-scores-v1.p.rapidapi.com/matches.php",
        'params': {"completedlimit": "5", "inprogresslimit": "5", "upcomingLimit": "5"},
        'headers': {'x-access-token': "undefined",
                    'x-rapidapi-key': "2f3130e1d0msh00771bcd8dd1c6ep1e7046jsnc993e624bbf3",
                    'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"}
    }
}


async def fetch_urls():
    res_dict_two = {}

    for api in api_dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=api_dict[api]['url'], headers=api_dict[api]['headers'],
                                   params=api_dict[api]['params'] if api_dict[api].get('params') else None) as response:
                now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                result = await response.text()
                res_dict_two[api] = result
                res_dict_two['time'] = now
    return str(res_dict_two)


loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_urls())


async def handle(request):
    text = await fetch_urls()
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/collect_info', handle)])

if __name__ == '__main__':
    web.run_app(app)


#another another variant

# HEADERS = {'x-rapidapi-key': "key"}
#
#
# async def fetch_url(session, url):
#     async with session.get(url, headers=HEADERS) as response:
#         return await response.text()
#
#
# async def fetch_all(session, urls):
#     tasks = []
#     for url in urls:
#         task = asyncio.create_task(fetch_url(session, url))
#         tasks.append(task)
#     results = await asyncio.gather(*tasks)
#     return results
#
#
# async def async_fetch_urls(request):
#     urls = ["https://mashape-community-urban-dictionary.p.rapidapi.com/define?term=python",
#             "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UA/UAH/en-GB/"
#             "?query=Barcelona",
#             "https://hotels4.p.rapidapi.com/locations/search?query=London"]
#     async with aiohttp.ClientSession() as session:
#         htmls = await fetch_all(session, urls)
#         return htmls
#
#
# async def handler(request):
#     text = await async_fetch_urls(request)
#     print(text)
#     return web.Response(text=str(text))
#
#
# app = web.Application()
# app.add_routes([web.get('/collect_info', handler)])
# web.run_app(app, host='127.0.0.1', port=8080)