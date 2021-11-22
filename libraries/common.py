import datetime
import shutil
import time

from robot.api import logger
import os


def log_message(message: str, level: str = 'INFO', console: bool = True):
    log_switcher = {
        'TRACE': logger.trace,
        'INFO': logger.info,
        'WARN': logger.warn,
        'ERROR': logger.error
    }
    if not level.upper() in log_switcher.keys() or level.upper() == 'INFO':
        logger.info(message, True, console)
    else:
        if level.upper() == 'ERROR':
            logger.info(message, True, console)
        else:
            log_switcher.get(level.upper(), logger.error)(message, True)


def get_downloaded_file_path(path_to_temp: str, extension: str, error_message: str = '') -> str:
    downloaded_files = []
    timer = datetime.datetime.now() + datetime.timedelta(0, 60 * 1)

    while timer > datetime.datetime.now():
        time.sleep(1)
        downloaded_files = [f for f in os.listdir(path_to_temp) if os.path.isfile(os.path.join(path_to_temp, f))]
        if len(downloaded_files) > 0 and downloaded_files[0].endswith(extension):
            time.sleep(1)
            break
    if len(downloaded_files) == 0:
        if error_message:
            raise Exception(error_message)
        return ''
    file_path = os.path.join(path_to_temp, downloaded_files[0])
    return file_path


def print_version():
    try:
        file = open('VERSION')
        try:
            print('Version {}'.format(file.read().strip()))
        except Exception as ex:
            print('Error reading VERSION file. {}'.format(str(ex)))
        finally:
            file.close()
    except Exception as e:
        log_message('VERSION file not found. {}'.format(str(e)))


def create_or_clean_dir(folder_path: str):
    shutil.rmtree(folder_path, ignore_errors=True)
    try:
        os.mkdir(folder_path)
    except FileExistsError:
        pass

