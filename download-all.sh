#!/bin/bash
set -euo pipefail

function download {
    local TEAM=$1
    local REPO1=$2
    echo "Team $TEAM"

    if [ "$#" -gt 2 ]; then
        local REPO2=$3
        mkdir -p "$TEAM/frontend"
        curl -L "$REPO1/archive/refs/heads/main.zip" > "$TEAM-frontend.zip"

        unzip "$TEAM-frontend.zip" -d "$TEAM/frontend"
        rm "$TEAM-frontend.zip"

        mkdir -p "$TEAM/backend"
        curl -L "$REPO2/archive/refs/heads/main.zip" > "$TEAM-backend.zip"

        unzip "$TEAM-backend.zip" -d "$TEAM/backend"
        rm "$TEAM-backend.zip"

    else
        mkdir -p "$TEAM"
        curl -L "$REPO1/archive/refs/heads/main.zip" > "$TEAM.zip"

        unzip "$TEAM.zip" -d "$TEAM"
        rm "$TEAM.zip"
    fi
}

download "FlexiSquid" https://github.com/KnightNight101/Komodo_Hackathon
download "FEIR" https://github.com/immo-huneke-zuhlke/projectfeir
download "OctoWatt" https://github.com/octopus-game/octogame https://github.com/octopus-game/octopus-game-backend
