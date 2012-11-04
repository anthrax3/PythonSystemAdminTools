import re
import sys
import urllib2

def get_video_url(content):
    pattern = re.search('(?<=fmt_url_map=).*', content)
    match = pattern.group(0).split('&amp;')
    vurls = urllib2.unquote(match[0])
    video_url = None
    for vurl in vurls.split('|'):
        if vurl.find('itag=5') > 0:
            return vurl
    return None

def get_title(content):
    title = content.split('</title>', 1)[0].split('<title>')[1]
    return sanitize_title(title)

def sanitize_title(rawtitle):
    rawtitle = urllib2.unquote(rawtitle)
    lines = rawtitle.split('\n')
    title = ''
    for line in lines:
        san = unicode(re.sub('[^\w\s-]', '', line).strip())
        san = re.sub('[-\s]+', '_', san)
        title = title + san
    ffr = title[:4]
    title = title[5:].split(ffr, 1)[0]
    return title

def download_video(f, resp):
    totalSize = int(resp.info().getheader('Content-Length').strip())
    currentSize = 0
    CHUNK_SIZE = 32768

    while True:
        data = resp.read(CHUNK_SIZE)

        if not data:
            break
        currentSize += len(data)
        f.write(data)

        print('============> ' + \
                  str(round(float(currentSize*100)/totalSize, 2)) + \
                  '% of ' + str(totalSize) + ' bytes')
        if currentSize >= totalSize:
            break
    return

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python youTubeDownloader.py \"<youtube-url>\"")
        exit(1)
    urlname = sys.argv[1].split('&', 1)[0]
    print('Downloading: ' + urlname)
    try: 
        resp = urllib2.urlopen(urlname)
    except urllib2.HTTPError:
        print('Bad URL: 404')
        exit(1)
    content = resp.read()
    video_url = get_video_url(content)
    if not video_url:
        print('Video URL cannot be found')
        exit(1)
    title = get_title(content)
    filename = title + '.flv'
    print('Creating file: ' + filename)
    f = open(filename, 'wb')
    print('Download begins...')

    # Download video
    video = urllib2.urlopen(video_url)
    download_video(f, video)
    f.flush()
    f.close()
    exit(0)
    
    
    
    
