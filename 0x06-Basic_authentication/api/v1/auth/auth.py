#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Requirement for Authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization Header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User
        """
        return None
