import subprocess


def git_tag():
    try:
        return subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).strip().decode('utf-8')
    except:
        return "v0.0.0"


def commit_hash():
    try:
        hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        return hash, hash[:7]
    except:
        return "", ""


def version_processor(request):
    commit, short_commit = commit_hash()
    return {'git_tag': git_tag(), 'commit': commit, 'short_commit': short_commit}
