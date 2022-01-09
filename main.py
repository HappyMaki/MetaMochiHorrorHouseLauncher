from version_utils import VersionUtil



def startGame():
    pass

def main():
    versionUtil = VersionUtil("https://api.github.com/repos/HappyMaki/metamochihorrorhouse-Releases/releases")
    if versionUtil.isNewVersionAvailable():
        versionUtil.getLatestVersion()

    # if versionUtil.isNewVersionAvailable():
    #     startGame()
    # else:
    #     raise Exception("Failed to get new version. Please get it directly from https://github.com/HappyMaki/metamochihorrorhouse-Releases")


if __name__ == "__main__":
    main()
