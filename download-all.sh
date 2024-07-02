
if [ -d FlexiSquid ]; then
    # backup
    mv FlexiSquid /tmp
fi
mkdir FlexiSquid
curl -L https://github.com/KnightNight101/Komodo_Hackathon/archive/refs/heads/main.zip > FlexiSquid.zip
unzip FlexiSquid.zip -d FlexiSquid
rm FlexiSquid.zip

o

if [ -d projectfeir ]; then
    # backup
    mv projectfeir /tmp
fi
mkdir projectfeir
curl -L https://github.com/immo-huneke-zuhlke/projectfeir/archive/refs/heads/main.zip > projectfeir.zip
unzip projectfeir.zip -d projectfeir
rm projectfeir.zip

