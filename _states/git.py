'''
Git Management
================

Manage git repositories:

.. code-block:: yaml

    /path/to/dest/:
      git:
        - exists
        - repo: git://github.com/user/repo.git
'''
import os


def exists(name, repo):
    """
    Clone a git repository

    name
        The destination on the minion filesystem to clone to

    repo
        The URL of the repository to clone
    """

    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''}

    try:
        if not os.path.exists(name):
            ret['changes'] = __salt__['git.clone'](repo=repo, dest=name)
        else:
            ret['changes'] = __salt__['git.checkout'](dest=name)
            ret['changes'].append(__salt__['git.pull'](dest=name))
    except:
        ret['result'] = False
        ret['comment'] = 'Failed to get repository.'

    return ret
