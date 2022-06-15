echo "# Python" >> README.md
git init
git add README.md
@rem git add .
git add -A
git commit -m "first commit"
git remote add origin https://github.com/kPlusPlus/Python.git
git branch -M main
git push -u -f origin master


@rem git remote add origin https://github.com/kPlusPlus/kPicola.git
@rem git push -u origin master


@rem bfg --replace-text passwords.txt
@rem git filter-branch --replace-text rockyou.txt