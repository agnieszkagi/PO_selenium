class BasePage:
    """
    This class contains the elements used by all pages,
    ex._verify_page(), etc.
    """

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        return


if __name__ == "__main__":
    unittest.main(verbosity=2)
