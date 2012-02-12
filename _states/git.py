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
import logging
import os
import shutil

logger = logging.getLogger(__name__)


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
        logger.debug("one")
        shutil.rmtree(name, ignore_errors=True)
        logger.debug("two")
        os.makedirs(name)
        logger.debug("three")
        ret['changes']['clone'] = __salt__['git.clone'](repo=repo, dest=name)
        logger.debug("four")
    except:
        logger.debug("Something went wrong in state module.")
        ret['result'] = False
        ret['comment'] = 'Failed to get repository.'

    return ret
