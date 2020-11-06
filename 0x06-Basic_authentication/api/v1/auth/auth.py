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
        if path is None or not excluded_paths:
            return True
        if excluded_paths is not None and len(excluded_paths) > 0:
            item = [x[:-1] for x in excluded_paths]
            if path in item or path[:-1] in excluded_paths:
                return False
        if path not in excluded_paths:
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
