#!/bin/bash
set -euo pipefail

function download {
    local TEAM=$1
    local REPO1=$2
    echo "Team $TEAM"

    if [ -d "$TEAM" ]; then
        echo "backing up $TEAM to /tmp/$TEAM"
        rm -rf /tmp/"$TEAM"
        mv "$TEAM" /tmp
    fi

    if [ "$#" -eq 2 ]; then
        mkdir -p "$TEAM"
        curl -L "$REPO1/archive/refs/heads/main.zip" > "$TEAM.zip"

        unzip "$TEAM.zip" -d "$TEAM"
        rm "$TEAM.zip"

    elif [ "$#" -eq 3 ]; then
        local REPO2=$3
        mkdir -p "$TEAM/frontend"
        curl -L "$REPO1/archive/refs/heads/main.zip" > "$TEAM-frontend.zip"

        unzip "$TEAM-frontend.zip" -d "$TEAM/frontend"
        rm "$TEAM-frontend.zip"

        mkdir -p "$TEAM/backend"
        curl -L "$REPO2/archive/refs/heads/main.zip" > "$TEAM-backend.zip"

        unzip "$TEAM-backend.zip" -d "$TEAM/backend"
        rm "$TEAM-backend.zip"

    elif [ "$#" -eq 4 ]; then
        local REPO2=$3
        local REPO3=$4
        local REPO1_NAME=$(echo "$REPO1" | awk -F/ '{print $NF}')
        local REPO2_NAME=$(echo "$REPO2" | awk -F/ '{print $NF}')
        local REPO3_NAME=$(echo "$REPO3" | awk -F/ '{print $NF}')

        download_to_folder "$TEAM" "$REPO1_NAME" "$REPO1"
        download_to_folder "$TEAM" "$REPO2_NAME" "$REPO2"
        download_to_folder "$TEAM" "$REPO3_NAME" "$REPO3"
    fi
}

function download_to_folder {
    local TEAM="$1"
    local FOLDER="$2"
    local URL="$3/archive/refs/heads/main.zip"
    mkdir -p "$TEAM/$FOLDER"
    curl -L "$URL" > "$TEAM-$FOLDER.zip"

    unzip "$TEAM-$FOLDER.zip" -d "$TEAM/$FOLDER"
    rm "$TEAM-$FOLDER.zip"
}

# download "FlexiSquid" https://github.com/KnightNight101/Komodo_Hackathon
# download "FEIR" https://github.com/immo-huneke-zuhlke/projectfeir
# download "OctoWatt" https://github.com/octopus-game/octogame https://github.com/octopus-game/octopus-game-backend

download "Starfish" https://github.com/StarFishEnergy/Website https://github.com/StarFishEnergy/StarFishEnergy https://github.com/StarFishEnergy/StarfishExchange
