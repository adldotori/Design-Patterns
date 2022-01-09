from main import Application
import pytest


class Test(object):
    def test_windows(self):
        app = Application("windows")
        app.run()

    def test_html(self):
        app = Application("html")
        app.run()

    def test_other(self):
        with pytest.raises(KeyError):
            app = Application("other")
            app.run()
