import matplotlib.pyplot as plt

from plotting import simple_plot


def test_simple_plot(monkeypatch):
    monkeypatch.setattr(plt, "show", lambda: None)
    data = [[1, 2, 3], [1, 2, 3]]
    simple_plot(data)
