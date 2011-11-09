try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from fabdeploy import monkey; monkey.patch_all()
from fabric.api import env, task, settings
from fabric.contrib import files

from fabdeploy.api import *


setup_fabdeploy()


@task
def conf(name, **kwargs):
    fabconf(name, {}, kwargs)


@task
def here(**kwargs):
    conf('here', **kwargs)


@task
def localhost(**kwargs):
    conf('localhost', **kwargs)


@task
def install():
    users.create.run()
    ssh.push_key.run(pub_key_file='~/.ssh/id_rsa.pub')

    system.setup_backports.run()
    system.install_common_software.run()

    with settings(warn_only=True):
        postgres.create_role.run()
        postgres.create_db.run()
        postgres.grant.run()

    nginx.install.run()


@task
def setup():
    fabd.mkdirs.run()

    gunicorn.push_config.run()
    nginx.push_gunicorn_config.run()
    nginx.restart.run()


@task
def clean():
    fabd.remove_src.run()
    virtualenv.remove.run()


@task
def deploy():
    fabd.mkdirs.run()
    postgres.dump.run()

    git.init.run()
    git.push.run()
    django.push_settings.run()
    supervisor.push_configs.run()

    if not files.exists('%(env_path)s/bin' % env.conf):
        virtualenv.create.run()
    virtualenv.pip_install_req.run()
    virtualenv.pip_install.run(app='gunicorn')

    supervisor.d.run()
    supervisor.update.run()
    supervisor.restart_program.run()

    django.syncdb.run()
