import sys, os, wget
import datetime
from pytz import timezone

def uctnow():
    return datetime.datetime.utcnow()
def now():
    return datetime.datetime.now(timezone('Asia/Seoul'))
def info(message=''):
    log(message,'info')
def error(message=''):
    log(message,'error')
def log(message,level):
    fmt='%Y-%m-%d %H:%M:%S'
    print('[%s] [%s] %s' % (now().strftime(fmt),level, message))
def join(var1, var2, delim='/'):
    
    if var1.endswith(delim) and not var2.startswith(delim):
        return var1+var2
    elif not var1.endswith(delim) and var2.startswith(delim):
        return var1+var2
    elif var1.endswith(delim) and var2.startswith(delim):
        return var1+var2[1:]
    else:
        return var1+delim+var2
    
    
# const
url = 'https://s3-eu-west-1.amazonaws.com/public.bitmex.com/data'
oneday = datetime.timedelta(days=1)
# variables
utcnow = uctnow()
today = utcnow.strftime('%Y%m%d')
yesterday = (utcnow - oneday).strftime('%Y%m%d')

# options(default)
out_dir = '.'
target = yesterday
target_url = join(url,'quote')

# get parameters
for i,arg in enumerate(sys.argv):
    if arg.startswith('--out') or arg.startswith('-o'):
        out_dir = sys.argv[i+1]
    if arg.startswith('--target') or arg.startswith('-t'):
        target = sys.argv[i+1]
    if arg.startswith('--data') or arg.startswith('-d'):
        target_url = join(sys.argv[i+1],'quote')

# error check
if not os.path.isdir(out_dir):
    print('error : out_dir is not exists')
    sys.exit(-1)
        
def is_skip(url,out_dir):
    fpath = join(out_dir,'skip.txt')
    if not os.path.exists(fpath):
        open(fpath,'w').close()
    f = open(fpath,'r')
    lines=f.read().splitlines()
    f.close()
    
    if url in lines:
        return True
    else:
        return False
def add_skip(url,out_dir):
    fpath = join(out_dir,'skip.txt')
    f = open(fpath,'a')
    f.write(url+'\n')
    f.close()
    
def download(fname, target_url, out_dir):
    ofilename = fname+'.csv.gz'
    ofilepath = join(out_dir, ofilename)
    url = join(target_url,ofilename)
    is_skip(url,out_dir)
    
    info('== DOWNLOAD ==')
    info(' * params : ')
    info('  - ofilepath : ' + ofilepath)
    info('  - url : ' + url)
    info('==============')
    info()
    
    if is_skip(url,out_dir):
        info('SKIP : url exists')
    elif os.path.exists(ofilepath):
        log('SKIP : file exits')
    else:
        try:
            fname=wget.download(url, out=out_dir)
            info('DOWNLOAD OK : ' + ofilename)
            add_skip(url,out_dir)
        except Exception as e:
            if '404' in str(e):
                error('NOT FOUND : ' + ofilename)
if __name__ == '__main__':
    
    # print options
    info('== START ==')
    info(' * params : ')
    info('  - out_dir : ' + out_dir)
    info('  - target : ' + target)
    info('  - target_url : ' + target_url)
    info('===========')
    info()
    download(target, target_url, out_dir)
    info('=== END ===')
    info()
