echo "Mettre la description de l'update"
read update
cd ..
git checkout map
git add map.txt
git commit -m "$update"
git push origin map