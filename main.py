from version_utils import VersionUtil
import os
import subprocess

def startGame():
    print("starting game!")
    subprocess.Popen(["StandaloneWindows64/StandaloneWindows64.exe"])
    os._exit(0)
    pass

def main():
    versionUtil = VersionUtil("https://api.github.com/repos/HappyMaki/metamochihorrorhouse-Releases/releases")
    if versionUtil.isNewVersionAvailable():
        versionUtil.getLatestVersion()
        versionUtil.promoteTempToMain()

    if not versionUtil.isNewVersionAvailable():
        startGame()
    else:
        raise Exception("Failed to get new version. Please get it directly from https://github.com/HappyMaki/metamochihorrorhouse-Releases")


if __name__ == "__main__":
    main()
