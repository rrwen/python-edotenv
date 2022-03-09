pushd docs\ || exit \B 1
for /D %%D in ("*") do (
    if /I not "%%~nxD"=="source" rd /S /Q "%%~D"
)
for %%F in ("*") do (
    del "%%~F"
)
popd
rmdir /s /q jupyter_execute\