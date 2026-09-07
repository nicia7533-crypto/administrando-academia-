# -*- mode: python ; coding: utf-8 -*-
# Spec do PyInstaller para o Corpo Dinamico - ARQUIVO UNICO (onefile).
#
# VERSAO DE DIAGNOSTICO: console=True de proposito, para qualquer erro
# aparecer numa janela de texto em vez do programa fechar em silencio.
# Depois de confirmar que abre certinho, troque console=True para
# console=False (ou console='minimal-console', no PyInstaller 6+) para
# esconder essa janela no dia a dia.
#
# Tudo o que o programa precisa (templates, CSS, logo, SQL das migrations)
# fica embutido dentro do proprio CorpoDinamico.exe. Os DADOS da academia
# ficam em %LOCALAPPDATA%\CorpoDinamico (nunca dentro do .exe).

import os

block_cipher = None
BASE = os.path.abspath(os.path.dirname(SPEC))

a = Analysis(
    ['main.py'],
    pathex=[BASE],
    binaries=[],
    datas=[
        (os.path.join(BASE, 'app', 'templates'), 'app/templates'),
        (os.path.join(BASE, 'app', 'static'), 'app/static'),
        (os.path.join(BASE, 'app', 'migrations'), 'app/migrations'),
        (os.path.join(BASE, 'assets', 'logo'), 'assets/logo'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CorpoDinamico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(BASE, 'assets', 'logo', 'logo-icone.ico'),
    onefile=True,
)
