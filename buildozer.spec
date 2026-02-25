[app]
title = System Update
package.name = sysupdate
package.domain = org.system
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a

# --- CONFIGURAÇÕES DE LOG E LICENÇA (SEM DUPLICATAS) ---
log_level = 2
warn_on_root = 0
android.accept_sdk_license = True
android.skip_update = False
android.enable_androidx = True
