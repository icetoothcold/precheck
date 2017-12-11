from . import main as main
from precheck import remoteExec


@main.route('/')
def hello_world():
    return 'Hello World!'

@main.route('/test')
def test():
    remoteExec()
    return 'remoteExec'



