[app]
# Nome que aparece no ícone do celular
title = System Update
# Nome interno do pacote (sem espaços ou acentos)
package.name = sysupdate
package.domain = org.system
# Onde está o código (o ponto significa a pasta atual)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Bibliotecas necessárias para rodar o Python no Android
requirements = python3,kivy

# Configurações de tela
orientation = portrait
fullscreen = 0

# Permissões cruciais para o funcionamento do agente
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Versão do Android (API 31 é o Android 12)
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True

# Arquiteturas de processador suportadas (cobre quase todos os celulares)
android.archs = arm64-v8a, armeabi-v7a
