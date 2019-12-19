import os, platform, logging


if platform.platform().startswith('Windows'):
    loggin_file = os.path.join(os.getenv('HOMEDRIVE'), \
                               os.getenv('HOMEPATH'), \
                               'test.log')
else:
    loggin_file = os.path.join(os.getenv('HOME'), 'test.log')

print('path to log: {}'.format(loggin_file))

logging.basicConfig(
    level = logging.DEBUG,
    format ='%(asctime)s : %(levelname)s : %(message)s',
    filename = loggin_file,
    filemode = 'a'
)

logging.debug('start')
logging.info('actions')
logging.warning('death')