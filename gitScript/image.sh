#! / Bin / bash
echo "Mettre la description de l'update"
read update
cd ..
git checkout image
git add .png
git commit -m "$update"
git push origin image