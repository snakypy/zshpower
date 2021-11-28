from concurrent.futures import ThreadPoolExecutor

from snakypy.helpers.console import loading

from snakypy.zshpower.prompt.sections.cmake import CMake
from snakypy.zshpower.prompt.sections.crystal import Crystal
from snakypy.zshpower.prompt.sections.dart import Dart
from snakypy.zshpower.prompt.sections.deno import Deno
from snakypy.zshpower.prompt.sections.docker import Docker
from snakypy.zshpower.prompt.sections.dotnet import Dotnet
from snakypy.zshpower.prompt.sections.elixir import Elixir
from snakypy.zshpower.prompt.sections.erlang import Erlang
from snakypy.zshpower.prompt.sections.golang import Golang
from snakypy.zshpower.prompt.sections.gulp import Gulp
from snakypy.zshpower.prompt.sections.helm import Helm
from snakypy.zshpower.prompt.sections.java import Java
from snakypy.zshpower.prompt.sections.julia import Julia
from snakypy.zshpower.prompt.sections.kotlin import Kotlin
from snakypy.zshpower.prompt.sections.nim import Nim
from snakypy.zshpower.prompt.sections.nodejs import NodeJs
from snakypy.zshpower.prompt.sections.ocaml import Ocaml
from snakypy.zshpower.prompt.sections.perl import Perl
from snakypy.zshpower.prompt.sections.php import Php
from snakypy.zshpower.prompt.sections.ruby import Ruby
from snakypy.zshpower.prompt.sections.rust import Rust
from snakypy.zshpower.prompt.sections.scala import Scala
from snakypy.zshpower.prompt.sections.vagrant import Vagrant
from snakypy.zshpower.prompt.sections.zig import Zig


def records(action, header, foreground, timer=0.090):
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(
            loading,
            set_time=timer,
            bar=False,
            header=header,
            foreground=foreground,
        )
        executor.submit(Dart().set_version, action=action)
        executor.submit(Docker().set_version, action=action)
        executor.submit(Dotnet().set_version, action=action)
        executor.submit(Elixir().set_version, action=action)
        executor.submit(Golang().set_version, action=action)
        executor.submit(Gulp().set_version, action=action)
        executor.submit(Java().set_version, action=action)
        executor.submit(Julia().set_version, action=action)
        executor.submit(NodeJs().set_version, action=action)
        executor.submit(Php().set_version, action=action)
        executor.submit(Ruby().set_version, action=action)
        executor.submit(Rust().set_version, action=action)
        executor.submit(Scala().set_version, action=action)
        executor.submit(Perl().set_version, action=action)
        executor.submit(CMake().set_version, action=action)
        executor.submit(Crystal().set_version, action=action)
        executor.submit(Deno().set_version, action=action)
        executor.submit(Erlang().set_version, action=action)
        executor.submit(Helm().set_version, action=action)
        executor.submit(Kotlin().set_version, action=action)
        executor.submit(Nim().set_version, action=action)
        executor.submit(Ocaml().set_version, action=action)
        executor.submit(Vagrant().set_version, action=action)
        executor.submit(Zig().set_version, action=action)
