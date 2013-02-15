from fabric.api import local
from fabric.api import lcd

#--------------------------------------------------------------
# Run tests - commit branch change - and merge them into master
#--------------------------------------------------------------
def prepare_deployment(branch_name):
    local('python manage.py test myapp')
	local('git add -p && git commit')
	local('git checkout master && git merge' + branch_name)

#--------------------------------------------------------------
# - Pull changes from development master branch
# - Run any migrations made
# - Run tests
# - Restart webserver
#--------------------------------------------------------------
def deploy():
    with lcd('/path/to/my/prod/area/'):
        local('git pull /my/path/to/dev/area/')
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')
