from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version


class Ocaml(Version, Base):
    def __init__(self):
        super(Ocaml, self).__init__()
        self.extensions = (".opam", ".ml", ".mli", ".re", ".rei")
        self.files = (
            "dune",
            "dune-project",
            "jbuild",
            "jbuild-ignore",
            ".merlin",
        )
        self.folders = ("_opam", "esy.lock")

    def get_version(
        self, config, reg_version, key="ocaml", ext="opam-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, exec_="ocaml", key="ocaml", action=None):
        command = run("ocaml -version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[-1]
        return super().set(command, version, exec_, key, action)
