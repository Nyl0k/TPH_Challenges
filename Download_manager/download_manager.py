import requests
import threading
import click

from requests.exceptions import HTTPError

def downloadThread(url, target, start, end):

    file_part = requests.get(url, headers={"Range": f"bytes={start}-{end}"}, stream=True)

    with open(target, 'rb+') as target_file:
        target_file.seek(start)
        target_file.write(file_part.content)

@click.command()
@click.argument('url', type=click.Path())
@click.option('--target', type=click.Path())
@click.option('--threads', default=5)
@click.pass_context
def Download(ctx, url, target, threads):
    response = requests.head(
        url
    )
    try:
        response.raise_for_status()
    except HTTPError as err:
        print(f'HTTP error occured: {err}')
    except Exception as err:
        print(f'Non-HTTP error occurred: {err}')
    else:
        print("Request successful")
    
    if target is None:
        target = url.split('/')[-1]
    
    file_size = int(response.headers['content-length'])

    with open(target, 'wb') as target_file:
        target_file.write(b'\0' * file_size)
        target_file.close()
    
    part_size = int(file_size/threads)

    threadPool = []

    for i in range(threads):
        start = part_size*i
        end = start+part_size

        threadPool.append(threading.Thread(target=downloadThread, daemon=True, kwargs={'url':url, 'target':target, 'start':start, 'end':end}))
    
    for thread in threadPool:
        thread.start()
    
    for thread in threadPool:
        thread.join()
    
    print("Download complete")

Download(obj={})