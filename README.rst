Quickstart
==========

We are going to deploy using:

- Empty Django project.
- Nginx server.
- Gunicorn daemonized via supervisord.
- Postgres database.

Create virtual env::

    virtualenv --no-site-packages ve
    . ve/bin/activate
    pip install -r requirements.txt

Manually apply patch from to
https://github.com/fabric/fabric/issues/471 to fabric. That's
annoying, I know!

Create settings::

    cp fabconf.py.def fabconf.py
    cd fabdeploy_example
    cp local_settings.py.def local_settings.py

Read fabfile.py tasks to be aware of changes that will be made to your system.

Install packages, create user and DB::

    fab localhost install

Check your deploy settings::

    fab localhost fabd.debug

Setup software::

    fab localhost setup

Deploy::

    fab localhost deploy

Site should be running on http://localhost/ or
http://fabdeploy_example/ (you need to add appropriate line to your
/etc/hosts). Site sources should be under /home/fabdeploy_example/src.
Python virtual env, configs, DB backups and logs should be under
/home/fabdeploy_example/envs.

Get list of available tasks::

    fab -l

Enjoy!
