def test_ci_trigger():
    # This is intentionally failing
    assert 1 == 0  # Agent should fix this

if __name__ == "__main__":
    test_ci_trigger()
