#! / Bin / bash
echo "Mettre la description de l'update"
read update
cd ..
git checkout script
git add .sh
git commit -m "$update"
git push origin script