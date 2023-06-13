from engine.sternman_engine import SternmanEngine
from utils import needs_service


class Palindrome(SternmanEngine):
    def needs_service(self):
        return needs_service(self)
