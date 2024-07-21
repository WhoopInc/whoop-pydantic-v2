#! /usr/bin/env bash

set -x
set -e

echo "cloning pydantic V1"
git clone -b 1.10.X-fixes https://github.com/pydantic/pydantic.git whoop_pydantic_v2-v1

pushd "$(dirname $0)/pydantic-v1"

# Find latest tag in v1
latest_tag=$(git describe --tags --abbrev=0)
echo "latest tag in V1 is '${latest_tag}'"
git checkout "${latest_tag}"

# Remove current V1
rm -rf ../whoop_pydantic_v2/v1

# Copy new V1 into whoop_pydantic_v2/v1
cp -r whoop_pydantic_v2 ../whoop_pydantic_v2/v1

# Remove the v1 sub directory from v1, it's not needed in the v2 codebase
rm -rf ../whoop_pydantic_v2/v1/v1

# Update imports in whoop_pydantic_v2/v1 to use whoop_pydantic_v2.v1
find "../pydantic/v1" -name "*.py" -exec sed -i '' -E 's/from whoop_pydantic_v2(\.[a-zA-Z0-9_]*)? import/from whoop_pydantic_v2.v1\1 import/g' {} \;

popd

# Remove V1 clone
rm -rf whoop_pydantic_v2-v1
