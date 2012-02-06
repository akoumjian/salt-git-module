'''
Clone git repositories.
'''


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
    cmd = 'git clone {repo} {dest}'.format(
        repo=repo,
        dest=dest)

    return __salt__['cmd.run'](cmd)