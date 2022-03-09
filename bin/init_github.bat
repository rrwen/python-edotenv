call git init
call git add .
call git commit -a -m "Initial commit"
call git branch -M main
call git remote add origin https://github.com/rrwen/python-edotenv.git
call git pull origin main --allow-unrelated-histories
call git push -u origin main