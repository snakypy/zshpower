# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['snakypy/zshpower/draw.py'],
             pathex=[],
             binaries=[],
             datas=[('snakypy/zshpower/commands', 'commands'), ('snakypy/zshpower/config', 'config'), ('snakypy/zshpower/database', 'database'), ('snakypy/zshpower/prompt', 'prompt'), ('snakypy/zshpower/utils', 'utils'), ('snakypy/zshpower/cli.py', '.'), ('snakypy/zshpower/__init__.py', '.'), ('snakypy/zshpower/__main__.py', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='zshpower-draw',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
					uac_admin=False)
