from dataclasses import dataclass


@dataclass
class Configuration():
    """App credentials"""
    user: str
    password: str

    """App Base URL"""
    url: str
