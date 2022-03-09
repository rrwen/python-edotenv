conda env create --prefix ./tmp/linux-env --file ./env.yml
chmod +x ./bin/activate.sh
chmod +x ./bin/deactivate.sh
chmod +x ./bin/uninstall.sh
chmod +x ./bin/build_docs.sh
chmod +x ./bin/rebuild_docs.sh
chmod +x ./bin/remove_docs.sh
chmod +x ./bin/install_package.sh
chmod +x ./bin/uninstall_package.sh
chmod +x ./bin/reinstall_package.sh
source bin/install_package.sh