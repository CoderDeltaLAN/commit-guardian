import commit_guardian as cg


def test_ping() -> None:
    assert cg.ping() == "pong"
