import app


def test_package_imports():
    assert callable(app.main)
