#! / Bin / bash
echo "Mettre la description de l'update"
read update
cd ..
git checkout python
git add .py
git commit -m "$update"
git push origin python