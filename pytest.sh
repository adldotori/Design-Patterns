for f in */*/test.py ; do
    echo "Running tests in $f"
    pytest $f
done