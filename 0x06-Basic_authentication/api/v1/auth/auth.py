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
        if excluded_paths is not None and len(excluded_paths) > 0:
            for i in excluded_paths:
                if i.__contains__(path):
                    return False
        if path is None or path not in excluded_paths:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """ Authorization Header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User
        """
        return None
