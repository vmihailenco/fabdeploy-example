Quickstart
==========

We are going to deploy using:

- Empty Django project.
- Nginx server.
- Gunicorn daemonized via supervisord.
- Postgres database.
- Fabdeploy:
  * https://bitbucket.org/vladimir_webdev/fabdeploy
  * https://github.com/vladimir-webdev/fabdeploy

Create virtual env::

    virtualenv --no-site-packages ve
    . ve/bin/activate
    pip install -r requirements.txt

Create settings::

    cp fabconf.py.def fabconf.py
    cd fabdeploy_example
    cp local_settings.py.def local_settings.py

Read fabfile.py tasks to be aware of changes that will be made to your system.

Create fabdeploy sudo user::

    fab fabd.default_conf:address=user@host,sudo_user=user fabd.create_user

Install packages, create user and DB::

    fab fabd.conf:localhost install

Check your deploy settings::

    fab fabd.conf:localhost fabd.debug

Setup software::

    fab fabd.conf:localhost setup

Deploy::

    fab fabd.conf:localhost deploy

Site should be running on http://localhost/ or
http://fabdeploy_example/ (you need to add appropriate line to your
/etc/hosts). Site sources should be under /home/fabdeploy_example/active/src.
Python virtual env, configs, DB backups and logs should be under
/home/fabdeploy_example/active/env.

Get list of available tasks::

    fab -l

Enjoy!
