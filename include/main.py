#!/usr/bin/env python3

from pygit2 import Repository, Branch
import os

def define_env(env):
    # env.variables.gitbranch = Repository('.').head.shorthand  # 'master
    repo = Repository('.')
    head = repo.head
    gitbranchname = head.shorthand

    env.variables.gitbranch = os.environ.get('CI_COMMIT_BRANCH', gitbranchname)
    env.variables.gitdefaultbranch = os.environ.get('CI_DEFAULT_BRANCH', "main")

