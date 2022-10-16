from os import environ

import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

import urllib3
urllib3.disable_warnings()

#<<<<<<< parallel-xdist

browsers = [
    {
        "platform": "Windows 10",
        "browserName": "MicrosoftEdge",
        "version": "18"
    }, {
        "platform": "Windows 10",
        "browserName": "firefox",
        "version": "69"
    }, {
        "platform": "Windows 7",
        "browserName": "internet explorer",
        "version": "11"
    }, {
        "deviceName" : "Galaxy S10"
    }, {
        "deviceName" : "Galaxy Note 9"
    }]


def pytest_generate_tests(metafunc):
    if 'driver' in metafunc.fixturenames:
        metafunc.parametrize('browser_config',
                             browsers,
                             ids=_generate_param_ids('broswerConfig', browsers),
                             scope='function')
=======
@pytest.fixture(scope='function')
def driver(request):
    desired_caps = {}

    browser = {
        "platform": "Windows 10",
        "browserName": "chrome",
        "version": "latest"
    }
 #>>>>>>> master

def _generate_param_ids(name, values):
    return [("<%s:%s>" % (name, value)).replace('.', '_') for value in values]

@pytest.yield_fixture(scope='function')
def driver(request, browser_config):
    # if the assignment below does not make sense to you please read up on object assignments.
    # The point is to make a copy and not mess with the original test spec.
    desired_caps = dict()
    desired_caps.update(browser_config)
    test_name = request.node.name
    build = environ.get('LT_BUILD', "Sample PY Build")
    tunnel_id = environ.get('LT_TUNNEL', False)
    username = environ.get('LT_USERNAME', None)
    access_key = environ.get('LT_ACCESS_KEY', None)

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    desired_caps['build'] = build
    # we can move this to the config load or not, also messing with this on a test to test basis is possible :)
    desired_caps['tunnel'] = tunnel_id
    desired_caps['name'] = test_name
#<<<<<<< parallel-xdist
    desired_caps['visual']= True
    desired_caps['network']= True
    desired_caps['console']= True
#=======
    desired_caps['video'] = True
    desired_caps['visual'] = True
    desired_caps['network'] = True
    desired_caps['console'] = True
    caps = {"LT:Options": desired_caps}
#>>>>>>> master

    executor = RemoteConnection(selenium_endpoint)
    browser = webdriver.Remote(
        command_executor=executor,
#<<<<<<< parallel-xdist
        desired_capabilities=desired_caps, 
        keep_alive=True
=======
        desired_capabilities=caps
#>>>>>>> master
    )

#<<<<<<< parallel-xdist
    if browser is not None:
        print("LambdaTestSessionID={} TestName={}".format(browser.session_id, test_name))
    else:
        raise WebDriverException("Never created!")

    yield browser
    # Teardown starts here
    # report results
    # use the test result to send the pass/fail status to LambdaTest
    result = "failed" if request.node.rep_call.failed else "passed"
    browser.execute_script("lambda-status={}".format(result))
    browser.quit()

=======
    def fin():
        # browser.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else
        # "failed").lower()))
        if request.node.rep_call.failed:
            browser.execute_script("lambda-status=failed")
        else:
            browser.execute_script("lambda-status=passed")
            browser.quit()

    request.addfinalizer(fin)
#>>>>>>> master


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
