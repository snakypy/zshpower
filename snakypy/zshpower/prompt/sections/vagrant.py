from subprocess import run

from snakypy.zshpower.prompt.sections.utils import Version


class Vagrant(Version):
    def __init__(self):
        super(Vagrant, self).__init__()
        self.files = ("Vagrantfile",)

    def get_version(
        self, config, reg_version, key="vagrant", ext="vag-", space_elem=" "
    ) -> str:
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="vagrant", action=None) -> bool:
        version = run(
            "vagrant --version 2>&1", capture_output=True, shell=True, text=True
        )

        if version.returncode != 127 and version.returncode != 1:
            version_format = version.stdout.split()[1].replace(" ", "")

            return super().set(version_format, key, action)

        return False
