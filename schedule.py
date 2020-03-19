import os
import re
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from django.core.management import execute_from_command_line


def read_env():
    try:
        with open('.env') as f:
            content = f.read()
            # raise Exception(content)
    except IOError:
        content = ''

    for line in content.splitlines():
        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))
            os.environ.setdefault(key, val)


read_env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "source.settings." + os.environ.get('APP_ENVIRONMENT'))


async def email_requeue():
    execute_from_command_line(["manage.py", "email_requeue"])


sched = AsyncIOScheduler()
sched.add_job(email_requeue, 'interval', minutes=1)
sched.start()

try:
    asyncio.get_event_loop().run_forever()
except (KeyboardInterrupt, SystemExit):
    pass
