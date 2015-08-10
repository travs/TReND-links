from flask import url_for
import thing as trendlinks

# helper functions for the test suite

def has_no_empty_params(rule):
    """
    Helper function for `list_URLs`.
    """
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def list_URLs(app):
    """
    Get a list of URLs that can be navigated to in a browser.
    Helper function for `test_URLs_render`.
    """
    with app.application.app_context():
        links = []
        for rule in app.application.url_map.iter_rules():
            # Filter out rules we can't navigate to in a browser
            # and rules that require parameters
            if 'GET' in rule.methods and has_no_empty_params(rule):
                url = get_url_for(rule.endpoint)
                links.append(url)
        return links

def get_url_for(route):
    """Wraps url_for() using a test request context"""
    with trendlinks.app.test_request_context():
        url = url_for('members', _external=True)
    return url

