#! / Bin / bash
echo "Mettre la description de l'update"
read update
git checkout dev
git add .py
git commit -m "$update"
git push origin dev