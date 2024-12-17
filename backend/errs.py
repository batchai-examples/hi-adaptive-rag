from abc import ABC
from enum import StrEnum, unique

from fastapi import HTTPException


@unique
class ErrorCode(StrEnum):
    CANNOT_CHANGE_TENANT = "CANNOT_CHANGE_TENANT"
    ENTITY_NOT_FOUND = "ENTITY_NOT_FOUND"
    PATH_NOT_FOUND = "PATH_NOT_FOUND"

    NOT_ALLOWED_FOR_ANONYMOUS = "NOT_ALLOWED_FOR_ANONYMOUS"

    MEMBERSHIP_CHANGED = "MEMBERSHIP_CHANGED"
    ADMIN_CHANGED = "ADMIN_CHANGED"
    CANNOT_DELETE_LAST_ADMIN = "CANNOT_DELETE_LAST_ADMIN"
    SUPER_ADMIN_CHANGED = "SUPER_ADMIN_CHANGED"
    NOT_A_MEMBER = "NOT_A_MEMBER"
    MEMBERSHIP_DUPLICATES = "MEMBERSHIP_DUPLICATES"

    MUST_BE_SUPER_ADMIN = "MUST_BE_SUPER_ADMIN"
    MUST_BE_TENANT_ADMIN = "MUST_BE_TENANT_ADMIN"
    NO_PERMISSION_ON_TENANT = "NO_PERMISSION_ON_TENANT"
    NO_PERMISSION_ON_SUBJECT = "NO_PERMISSION_ON_SUBJECT"
    NO_PERMISSION_ON_MODEL = "NO_PERMISSION_ON_MODEL"
    NO_PERMISSION_ON_VENDOR = "NO_PERMISSION_ON_VENDOR"
    NO_PERMISSION_ON_PROXY = "NO_PERMISSION_ON_PROXY"

    OAUTH_CLIENT_ID_DUPLICATES = "OAUTH_CLIENT_ID_DUPLICATES"
    WRONG_PASSWORD = "WRONG_PASSWORD"
    EMAIL_DUPLICATES = "EMAIL_DUPLICATES"
    NAME_DUPLICATES = "NAME_DUPLICATES"
    KEY_DUPLICATES = "KEY_DUPLICATES"
    CODE_DUPLICATES = "CODE_DUPLICATES"
    NONE = "NONE"
    ID_CANNOT_BE_NULL = "ID_CANNOT_BE_NULL"

    PROXY_IS_USED_BY_VENDOR = "PROXY_IS_USED_BY_VENDOR"
    PROXY_IS_USED_BY_MODEL = "PROXY_IS_USED_BY_MODEL"

    PARAMETER_NOT_VALID = "PARAMETER_NOT_VALID"
    CONSTRAINT_VIOLATION = "CONSTRAINT_VIOLATION"
    WRONG_DATA_FORMAT = "WRONG_DATA_FORMAT"
    FIELD_NOT_UPDATEABLE = "FIELD_NOT_UPDATEABLE"
    FIELD_NOT_ASSIGNABLE = "FIELD_NOT_ASSIGNABLE"
    FIELD_NOT_EXISTS = "FIELD_NOT_EXISTS"

    INVALID_ENUM = "INVALID_ENUM"
    INVALID_PROPERTY = "INVALID_PROPERTY"


class BaseError(HTTPException, ABC):
    def __init__(self, status_code: int, detail: str, code):
        super().__init__(status_code=status_code, detail=detail)
        self.code = code


class Internal(BaseError):
    def __init__(self, detail: str, code: ErrorCode = ErrorCode.NONE):
        super().__init__(500, detail, code)


class BadRequest(BaseError):
    def __init__(self, detail: str, code: ErrorCode = ErrorCode.NONE):
        super().__init__(400, detail, code)


class Unauthorized(BaseError):
    def __init__(self, detail: str, code: ErrorCode = ErrorCode.NONE):
        super().__init__(401, detail, code)


class Forbidden(BaseError):
    def __init__(self, detail: str, code: ErrorCode = ErrorCode.NONE):
        super().__init__(403, detail, code)


class NotFound(BaseError):
    def __init__(self, detail: str, code: ErrorCode = ErrorCode.NONE):
        super().__init__(404, detail, code)


class Conflict(BaseError):
    def __init__(self, detail: str, code: ErrorCode = ErrorCode.NONE):
        super().__init__(409, detail, code)
