from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version


class Ocaml(Version):
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

    def set_version(self, key="ocaml", action=None) -> bool:
        version = run("ocaml -version 2>&1", capture_output=True, shell=True, text=True)

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.split()[-1]
            return super().set(version_format, key, action)

        return False
