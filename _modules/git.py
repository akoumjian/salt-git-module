'''
Manage git repositories.
'''
import logging
logger = logging.getLogger(__name__)


def clone(repo='', dest=''):
    '''
    Clone a git repository

    repo : None
        The repository source.
    dest : None
        The destination directory. Uses the default from git if none.
        (Probably ~/myrepo)

    CLI Example::

        salt '*' git.clone git@github.com:username/myrepo.git \\
                /path/to/destination/myrepo
    '''
    result = ''
    try:
        cmd = 'git clone {repo} {dest}'.format(
            repo=repo,
            dest=dest)
        result = __salt__['cmd.run'](cmd)
    except:
        logger.debug("Something went wrong while cloning.")

    return result


def pull(remote='', dest=''):
    '''
    Pull the updates from a git repository.

    remote : None
        The remote repository to pull from.

    dest : None
        The location of the git repository to updates
    '''
    cmd = 'git pull {remote}'.format(remote=remote)
    return __salt__['cmd.run'](cmd, dest)


def fetch(remote='', dest=''):
    '''
    Fetches from a remote git repository.

    remote : None
        Specify a remote to fetch from

    dest : None
        Location of local git repository
    '''
    cmd = 'git fetch {remote}'.format(remote=remote)
    return __salt__['cmd.run'](cmd, dest)


def checkout(dest='', files='.'):
    '''
    Checkout files from local repository, overwriting changes

    dest : None
        Location of working directory
    files : .
        String of files to checkout. All ('.') by default.
    '''
    cmd = 'git checkout {files}'.format(files=files)
    return __salt__['cmd.run'](cmd, dest)