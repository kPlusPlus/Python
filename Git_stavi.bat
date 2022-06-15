echo "# Python" >> README.md
git init
git add README.md
git add .
git commit -m "first commit"
git remote add origin https://github.com/kPlusPlus/Python.git
git push -u origin master


@rem git remote add origin https://github.com/kPlusPlus/kPicola.git
@rem git push -u origin master


@rem bfg --replace-text passwords.txt
@rem git filter-branch --replace-text rockyou.txt