
if [ -d team-3-FlexiSquid ]; then
    # backup
    mv team-3-FlexiSquid /tmp
fi
mkdir team-3-FlexiSquid
curl -L https://github.com/KnightNight101/Komodo_Hackathon/archive/refs/heads/main.zip > team3.zip
unzip team3.zip -d team-3-FlexiSquid
rm team3.zip

