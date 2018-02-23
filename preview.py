from contextlib import closing
from git import Repo
from threading import Timer
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import click
import datetime
import io
import os
import re
import requests
import shutil
import time
import yaml
import zipfile


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PREVIEW_DIR = os.path.join(ROOT_DIR, 'preview/')
REPO = Repo(ROOT_DIR)
BRANCH = REPO.active_branch.name
SOURCE_FILE = os.path.join(ROOT_DIR, 'PITCHME.md')
PREVIEW_FILE = os.path.join(PREVIEW_DIR, BRANCH, 'assets/md/PITCHME.md')
PREVIEW_INDEX = os.path.join(PREVIEW_DIR, BRANCH, 'index.html')

with open(os.path.join(ROOT_DIR, 'PITCHME.yaml'), 'r') as config_stream:
    THEME = yaml.load(config_stream).get('theme')

preprocess_defs = [
    {
        'from': r'^@\[([0-9,\-]+)\](?:\((.*)\))?$',
        'to': r'<span class="code-presenting-annotation fragment current-only" data-code-focus="\1">\2</span>'
    }
]


def _preprocess(source):
    out = source
    for replacement in preprocess_defs:
        out = re.sub(replacement.get('from'), replacement.get('to'), out, flags=re.MULTILINE)
    return out


def _update_preview_file():
    print('Updating preview file...')

    with open(SOURCE_FILE, 'r') as source, open(PREVIEW_FILE, 'w') as destination:
        preprocessed = _preprocess(source.read())
        current = destination.write(preprocessed)


@click.command()
def init():
    """Fetch preview package from gitpitch.com"""

    temp_dir = os.path.join(PREVIEW_DIR, 'PITCHME/')
    target_dir = os.path.join(PREVIEW_DIR, f'{BRANCH}/')

    for _dir in [temp_dir, target_dir]:
        if os.path.isdir(_dir):
            print(f'Removing current {_dir}...')
            shutil.rmtree(_dir)

    preview_url = f'https://gitpitch.com/dsimidzija/presentations/{BRANCH}#/'
    download_url = f'https://gitpitch.com/pitchme/offline/github/dsimidzija/presentations/{BRANCH}/{THEME}/PITCHME.zip'

    with requests.Session() as session:
        print('Getting preview...')
        session.get(preview_url)
        print('Downloading...')
        r = session.get(download_url)
        with closing(r), zipfile.ZipFile(io.BytesIO(r.content)) as archive:
            print('Extracting...')
            archive.extractall(PREVIEW_DIR)
            os.rename(temp_dir, target_dir)

    _update_preview_file()


@click.command()
def start():
    """Start preview server"""

    class Handler(FileSystemEventHandler):
        timer = None

        def on_modified(self, event):
            if event.src_path != SOURCE_FILE:
                return

            if self.timer is not None:
                self.timer.cancel()
                self.timer = None

            self.timer = Timer(0.2, self.handle)
            self.timer.start()

        def handle(self):
            print(f'File change detected at {datetime.datetime.now().isoformat()}')
            _update_preview_file()
            self.timer = None

    _update_preview_file()

    print('Starting watchdog...')
    observer = Observer()
    observer.schedule(Handler(), ROOT_DIR, recursive=False)
    observer.start()

    preview_index = f'file://{PREVIEW_INDEX}'
    print(f'Now listening for changes, open {preview_index} in your browser')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Shutting down...')
        observer.stop()
    observer.join()


@click.command()
def update():
    """Update current preview file"""
    _update_preview_file()


@click.group()
def main():
    pass


main.add_command(init)
main.add_command(update)
main.add_command(start)


if __name__ == '__main__':
    main()
