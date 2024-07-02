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
        download_to_folder "$TEAM" "" "$REPO1"

    elif [ "$#" -eq 3 ]; then
        local REPO2=$3
        download_to_folder "$TEAM" frontend "$REPO1"
        download_to_folder "$TEAM" backend "$REPO2"

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
    if [[ "$TEAM" ==  "EcoCompass" ]]; then
        local URL="$3/archive/refs/heads/master.zip"
    elif [[ "$TEAM" ==  "SquidLink" ]]; then
        local URL="$3/archive/refs/heads/master.zip"
    else
        local URL="$3/archive/refs/heads/main.zip"
    fi
    mkdir -p "$TEAM/$FOLDER"
    curl -L "$URL" > "$TEAM-$FOLDER.zip"

    unzip "$TEAM-$FOLDER.zip" -d "$TEAM/$FOLDER"
    rm "$TEAM-$FOLDER.zip"
}

download "FlexiSquid" https://github.com/KnightNight101/Komodo_Hackathon
download "FEIR" https://github.com/immo-huneke-zuhlke/projectfeir
download "OctoWatt" https://github.com/octopus-game/octogame https://github.com/octopus-game/octopus-game-backend
download "Starfish" https://github.com/StarFishEnergy/Website https://github.com/StarFishEnergy/StarFishEnergy https://github.com/StarFishEnergy/StarfishExchange
download "PaybackTime" https://github.com/hkl19/paybacktime
download "Solstice" https://github.com/kraken-hack-24/solstice
download "EcoCompass" https://github.com/moagli/teamtwo
download "SquidLink" https://github.com/SquidyLink/SquidyLinkFE https://github.com/SquidyLink/SquidyLinkBE
