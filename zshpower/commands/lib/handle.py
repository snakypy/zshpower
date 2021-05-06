from zshpower.prompt.sections.gulp import Gulp
from zshpower.prompt.sections.zig import Zig
from zshpower.prompt.sections.vagrant import Vagrant
from zshpower.prompt.sections.ocaml import Ocaml
from zshpower.prompt.sections.nim import Nim
from zshpower.prompt.sections.kotlin import Kotlin
from zshpower.prompt.sections.helm import Helm
from zshpower.prompt.sections.erlang import Erlang
from zshpower.prompt.sections.deno import Deno
from zshpower.prompt.sections.crystal import Crystal
from zshpower.prompt.sections.cmake import CMake
from zshpower.prompt.sections.perl import Perl
from zshpower.prompt.sections.julia import Julia
from zshpower.prompt.sections.elixir import Elixir
from zshpower.prompt.sections.dotnet import Dotnet
from zshpower.prompt.sections.docker import Docker
from zshpower.prompt.sections.golang import Golang
from zshpower.prompt.sections.java import Java
from zshpower.prompt.sections.scala import Scala
from zshpower.prompt.sections.dart import Dart
from zshpower.prompt.sections.nodejs import NodeJs
from zshpower.prompt.sections.php import Php
from zshpower.prompt.sections.ruby import Ruby
from zshpower.prompt.sections.rust import Rust
from concurrent.futures import ThreadPoolExecutor


def records(action) -> None:
    with ThreadPoolExecutor(max_workers=8) as executor:
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

# Thread(target=Dart().set_version, kwargs={"action": action}).start()
# Thread(target=Docker().set_version, kwargs={"action": action}).start()
# Thread(target=Dotnet().set_version, kwargs={"action": action}).start()
# Thread(target=Elixir().set_version, kwargs={"action": action}).start()
# Thread(target=Golang().set_version, kwargs={"action": action}).start()
# Thread(target=Gulp().set_version, kwargs={"action": action}).start()
# Thread(target=Java().set_version, kwargs={"action": action}).start()
# Thread(target=Julia().set_version, kwargs={"action": action}).start()
# Thread(target=NodeJs().set_version, kwargs={"action": action}).start()
# Thread(target=Php().set_version, kwargs={"action": action}).start()
# Thread(target=Ruby().set_version, kwargs={"action": action}).start()
# Thread(target=Rust().set_version, kwargs={"action": action}).start()
# Thread(target=Scala().set_version, kwargs={"action": action}).start()
# Thread(target=Perl().set_version, kwargs={"action": action}).start()
# Thread(target=CMake().set_version, kwargs={"action": action}).start()
# Thread(target=Crystal().set_version, kwargs={"action": action}).start()
# Thread(target=Deno().set_version, kwargs={"action": action}).start()
# Thread(target=Erlang().set_version, kwargs={"action": action}).start()
# Thread(target=Helm().set_version, kwargs={"action": action}).start()
# Thread(target=Kotlin().set_version, kwargs={"action": action}).start()
# Thread(target=Nim().set_version, kwargs={"action": action}).start()
# Thread(target=Ocaml().set_version, kwargs={"action": action}).start()
# Thread(target=Vagrant().set_version, kwargs={"action": action}).start()
# Thread(target=Zig().set_version, kwargs={"action": action}).start()
