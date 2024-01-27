gunzip -c ../MCB185/data/dictionary.gz | grep -i "R" | grep -v -Ei "[^OZNICAR]+" | grep -E ".{4,}"
gunzip -c ../MCB185/data/dictionary.gz | grep -i "R" | grep -v -Ei "[^OZNICAR]+" | grep -E ".{4,}" | wc -l


