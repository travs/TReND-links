from flask import url_for

# helper functions for the test suite

def has_no_empty_params(rule):
    """
    Helper function for `list_URLs`.
    """
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def list_URLs():
    """
    Get a list of URLs that can be navigated to in a browser.
    Helper function for `test_URLs_render`.
    """
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint)
            links.append(url)
    return links


