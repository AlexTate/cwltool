from py._path import common 
from py._path.common import  iswin32 
from typing import Any, Optional


def map_as_list(func: Any, iter: Any): ...

ALLOW_IMPORTLIB_MODE: Any

class Stat:
    def __getattr__(self, name: Any): ...
    path: Any = ...
    def __init__(self, path: Any, osstatresult: Any) -> None: ...
    @property
    def owner(self): ...
    @property
    def group(self): ...
    def isdir(self): ...
    def isfile(self): ...
    def islink(self): ...

class PosixPath(common.PathBase):
    def chown(self, user: Any, group: Any, rec: int = ...): ...
    def readlink(self): ...
    def mklinkto(self, oldname: Any) -> None: ...
    def mksymlinkto(self, value: Any, absolute: int = ...) -> None: ...

FSBase = PosixPath #or common.PathBase

def getuserid(user: Any): ...
def getgroupid(group: Any): ...

class LocalPath(FSBase):
    class ImportMismatchError(ImportError): ...
    sep: Any = ...
    class Checkers(common.Checkers):
        def dir(self): ...
        def file(self): ...
        def exists(self): ...
        def link(self): ...
    strpath: Any = ...
    def __init__(self, path: Optional[Any] = ..., expanduser: bool = ...) -> None: ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def samefile(self, other: Any): ...
    def remove(self, rec: int = ..., ignore_errors: bool = ...) -> None: ...
    def computehash(self, hashtype: str = ..., chunksize: int = ...): ...
    def new(self, **kw: Any): ...
    def dirpath(self, *args: Any, **kwargs: Any): ...
    def join(self, *args: Any, **kwargs: Any): ...
    def open(self, mode: str = ..., ensure: bool = ..., encoding: Optional[Any] = ...): ...
    def islink(self): ...
    def check(self, **kw: Any): ...
    def listdir(self, fil: Optional[Any] = ..., sort: Optional[Any] = ...): ...
    def size(self): ...
    def mtime(self): ...
    def copy(self, target: Any, mode: bool = ..., stat: bool = ...): ...
    def rename(self, target: Any): ...
    def dump(self, obj: Any, bin: int = ...) -> None: ...
    def mkdir(self, *args: Any): ...
    def write_binary(self, data: Any, ensure: bool = ...) -> None: ...
    def write_text(self, data: Any, encoding: Any, ensure: bool = ...) -> None: ...
    def write(self, data: Any, mode: str = ..., ensure: bool = ...) -> None: ...
    def ensure(self, *args: Any, **kwargs: Any): ...
    def stat(self, raising: bool = ...): ...
    def lstat(self): ...
    def setmtime(self, mtime: Optional[Any] = ...): ...
    def chdir(self): ...
    def as_cwd(self) -> None: ...
    def realpath(self): ...
    def atime(self): ...
    def chmod(self, mode: Any, rec: int = ...) -> None: ...
    def pypkgpath(self): ...
    def pyimport(self, modname: Optional[Any] = ..., ensuresyspath: bool = ...): ...
    def sysexec(self, *argv: Any, **popen_opts: Any): ...
    def sysfind(cls, name: Any, checker: Optional[Any] = ..., paths: Optional[Any] = ...): ...
    @classmethod
    def get_temproot(cls): ...
    @classmethod
    def mkdtemp(cls, rootdir: Optional[Any] = ...): ...
    def make_numbered_dir(cls, prefix: str = ..., rootdir: Optional[Any] = ..., keep: int = ..., lock_timeout: int = ...): ...

def copymode(src: Any, dest: Any) -> None: ...
def copystat(src: Any, dest: Any) -> None: ...
def copychunked(src: Any, dest: Any) -> None: ...
def isimportable(name: Any): ...
