# Make sure the script is executed from the current directory even if it's called from somewhere else.
pushd "${0%/*}" # https://stackoverflow.com/a/207966

./install.sh
./test.sh

# Go back to original directory.
popd
