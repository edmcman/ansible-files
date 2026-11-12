#!/usr/bin/env python3
import configparser
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import urllib.request

URL = 'https://api.beeper.com/desktop/download/linux/x64/stable/com.automattic.beeper.desktop'
GEAR = ['flatpak', 'run', 'it.mijorus.gearlever']
HOME = Path.home()


def gear(*args):
    result = subprocess.run(GEAR + list(args), text=True, capture_output=True)
    if result.stderr:
        print(result.stderr, file=sys.stderr, end='')
    result.check_returncode()
    if args[0] == '--list-updates' and ('ERROR' in result.stderr or 'Traceback' in result.stderr):
        raise RuntimeError('Gear Lever failed to check for updates')
    return result.stdout


def apps(kind):
    data = json.loads(gear(f'--list-{kind}', '--json'))
    if data['schema_version'] != 1:
        raise ValueError('Unsupported Gear Lever JSON schema')
    return [app for app in data[kind] if app['name'].casefold() == 'beeper']


def beeper():
    matches = apps('installed')
    if len(matches) != 1:
        raise ValueError(f'Expected one integrated Beeper, found {len(matches)}')
    return matches[0]


def running(app):
    if app['running'] is not False:
        return True
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            if f"APPIMAGE={app['path']}".encode() in (proc / 'environ').read_bytes().split(b'\0'):
                return True
        except (PermissionError, ProcessLookupError, FileNotFoundError):
            pass
    return False


def autostart(app):
    desktop = app['desktop_id']
    if not desktop or Path(desktop).name != desktop:
        raise ValueError('Beeper has no valid desktop ID')
    source = HOME / '.local/share/applications' / desktop
    if not source.is_file():
        raise FileNotFoundError(source)
    target = HOME / '.config/autostart/beeper.desktop'
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_symlink() and os.readlink(target) == str(source):
        return False
    target.unlink(missing_ok=True)
    target.symlink_to(source)
    return True


def setup():
    matches = apps('installed')
    changed = False
    if not matches:
        with tempfile.TemporaryDirectory(dir=HOME) as tmp:
            image = Path(tmp) / 'Beeper.AppImage'
            urllib.request.urlretrieve(URL, image)
            gear('--integrate', str(image), '-y')
        changed = True
    app = beeper()
    config = configparser.ConfigParser(interpolation=None)
    config.read(HOME / '.var/app/it.mijorus.gearlever/config/gearlever.conf')
    section = 'app.' + hashlib.md5(app['path'].encode()).hexdigest() + '.update_manager'
    if (dict(config[section]) if config.has_section(section) else {}) != {'manager': 'StaticFileUpdater', 'url': URL}:
        gear('--set-update-source', app['path'], '--manager', 'StaticFileUpdater', f'url={URL}')
        changed = True
    changed = autostart(app) or changed
    print('changed' if changed else 'unchanged')


def update():
    app = beeper()
    if running(app):
        print('Beeper is running; skipping update')
        return
    updates = apps('updates')
    if len(updates) > 1 or (updates and updates[0]['path'] != app['path']):
        raise ValueError('Ambiguous Beeper update')
    if updates:
        print(gear('--update', app['path'], '-y'), end='')
        autostart(beeper())
        print('Beeper updated')
    else:
        print('Beeper is up to date')


if __name__ == '__main__':
    {'setup': setup, 'update': update}[sys.argv[1]]()
