# build.spec
block_cipher = None

a = Analysis(
    ['src/security_scanner.py'],
    pathex=['D:\应急\姜小文应急工具第一版\pro\promax\ruyan'],  # 改为您的实际路径
    binaries=[],
    datas=[
        ('src/icon.ico', '.'),  # 包含图标文件
        ('yara_rules', 'yara_rules')  # 包含YARA规则目录
    ],
    hiddenimports=[
        'yara',
        'psutil',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
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
    name='SecurityScanner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # 使用UPX压缩
    console=False,  # 不显示控制台窗口
    icon='src/icon.ico',  # 图标路径
    uac_admin=True  # 请求管理员权限
)